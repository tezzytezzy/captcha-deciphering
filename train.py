import cv2
import pickle
from os import listdir
import os.path
import numpy as np
from glob import glob
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Flatten, Dense
from constants import *

data = []
labels = []
nr_labels = len(listdir(LETTERS_FOLDER))

# Convert each image to a data matrix
for label in listdir(LETTERS_FOLDER):
    for image_file in glob(os.path.join(LETTERS_FOLDER, label, '*.png')):
        image = cv2.imread(image_file)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Resize the image so all images have the same input shape
        image = cv2.resize(image, MODEL_SHAPE)
        # Expand dimensions to make Keras happy
        image = np.expand_dims(image, axis=2)
        data.append(image) # pixel matrix
        labels.append(label) # answer


# Normalize the data so every value lies between zero and one, easier processing by the neural network
data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)

# Create a training-test split
(X_train, X_test, Y_train, Y_test) = train_test_split(data, labels, 
                                                      test_size=0.25, random_state=0)

# Binarize the labels
# Keras can’t work with “Q”, “W”,… labels directly, we need to binarize these:
# every label is converted to an output vertex with each index corresponding to
# one possible character, with its value set to one or zero, so that “Q” would become
# “[1, 0, 0, 0,…],” “W” would become “[0, 1, 0, 0,…],” and so on.
lb = LabelBinarizer().fit(Y_train)
Y_train = lb.transform(Y_train)
Y_test = lb.transform(Y_test)

# Save the binarization for later
# We’ll also need it to perform the conversion back to characters again during application of the model
with open(LABELS_FILE, "wb") as f:
    pickle.dump(lb, f)

# Construct the model architecture
model = Sequential()
model.add(Conv2D(20, (5, 5), padding="same", 
          input_shape=(MODEL_SHAPE[0], MODEL_SHAPE[1], 1), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Conv2D(50, (5, 5), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Flatten())
model.add(Dense(500, activation="relu"))
model.add(Dense(nr_labels, activation="softmax"))
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Train and save the model
model.fit(X_train, Y_train, validation_data=(X_test, Y_test), 
          batch_size=32, epochs=10, verbose=1)
model.save(MODEL_FILE)
