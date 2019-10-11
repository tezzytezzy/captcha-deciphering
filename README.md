# captcha-deciphering

## Objective
Practical implementation of:
1. Convolutional Neural Network (Deep Learning) via [Keras](https://keras.io/) with [TensorFlow](https://www.tensorflow.org/) backend (default), and
2. Web Data Mining via [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)*

*I mulled over [Scrapy](https://scrapy.org/) and [Selenium](https://www.seleniumhq.org/), but settled on Beautiful Soup for its simplicity and ease of use.

## Installation
The following packages to be installed:

```bash
beautifulsoup4            4.8.1                    pypi_0    pypi
captcha                   0.3                      pypi_0    pypi
glob2                     0.7                        py_0  
keras                     2.2.4                         0  
opencv-python             4.1.1.26                 pypi_0    pypi
scikit-learn              0.21.3           py37hd81dba3_0  
```

## Procedure
1. Use the CAPTCHA library to generate and save 1,000 sample files under the _generated_images_ sub-directory.
2. Using the OpenCV library to separate the images into each alphanumeric character by means of thresholding, opening, and contour detection. Save that character in a directory named after its correposding character under the _letters_ sub-directory.
3. Using the Keras library to train a model with the letter samples collected above for each letter.

## Result
58% of accuracy.

```bash
1432/1432 [==============================] - 34s 24ms/step - loss: 2.9809 - acc: 0.2556 - val_loss: 2.2488 - val_acc: 0.4561
Epoch 2/10
1432/1432 [==============================] - 33s 23ms/step - loss: 1.5028 - acc: 0.6229 - val_loss: 1.7459 - val_acc: 0.5879
Epoch 3/10
1432/1432 [==============================] - 34s 24ms/step - loss: 0.6440 - acc: 0.8387 - val_loss: 1.9391 - val_acc: 0.5732
Epoch 4/10
1432/1432 [==============================] - 34s 24ms/step - loss: 0.1497 - acc: 0.9588 - val_loss: 2.5291 - val_acc: 0.5816
Epoch 5/10
1432/1432 [==============================] - 35s 25ms/step - loss: 0.0699 - acc: 0.9784 - val_loss: 2.6889 - val_acc: 0.5565
Epoch 6/10
1432/1432 [==============================] - 35s 25ms/step - loss: 0.0241 - acc: 0.9916 - val_loss: 2.9378 - val_acc: 0.5544
Epoch 7/10
1432/1432 [==============================] - 36s 25ms/step - loss: 0.0317 - acc: 0.9888 - val_loss: 2.7667 - val_acc: 0.5858
Epoch 8/10
1432/1432 [==============================] - 36s 25ms/step - loss: 0.0250 - acc: 0.9944 - val_loss: 2.7805 - val_acc: 0.5941
Epoch 9/10
1432/1432 [==============================] - 36s 25ms/step - loss: 0.0114 - acc: 0.9986 - val_loss: 2.7468 - val_acc: 0.6025
Epoch 10/10
1432/1432 [==============================] - 36s 25ms/step - loss: 0.0022 - acc: 0.9993 - val_loss: 2.9266 - val_acc: 0.5816
```

## Reference
[Practical Web Scraping for Data Science Best Practices and Examples with Python (ISBN 978-1-4842-3582-9)](https://www.apress.com/us/book/9781484235812)
