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
63% of accuracy.

```bash
Train on 2876 samples, validate on 959 samples
Epoch 1/10
2876/2876 [==============================] - 69s 24ms/step - loss: 2.2493 - acc: 0.4360 - val_loss: 1.6329 - val_acc: 0.6163
Epoch 2/10
2876/2876 [==============================] - 69s 24ms/step - loss: 1.0487 - acc: 0.7406 - val_loss: 1.7075 - val_acc: 0.5912
Epoch 3/10
2876/2876 [==============================] - 72s 25ms/step - loss: 0.4068 - acc: 0.8873 - val_loss: 2.0714 - val_acc: 0.6246
Epoch 4/10
2876/2876 [==============================] - 76s 27ms/step - loss: 0.1239 - acc: 0.9677 - val_loss: 2.4089 - val_acc: 0.6131
Epoch 5/10
2876/2876 [==============================] - 75s 26ms/step - loss: 0.0793 - acc: 0.9812 - val_loss: 2.5761 - val_acc: 0.6027
Epoch 6/10
2876/2876 [==============================] - 77s 27ms/step - loss: 0.0281 - acc: 0.9924 - val_loss: 2.6144 - val_acc: 0.6173
Epoch 7/10
2876/2876 [==============================] - 78s 27ms/step - loss: 0.0249 - acc: 0.9941 - val_loss: 2.6915 - val_acc: 0.6236
Epoch 8/10
2876/2876 [==============================] - 76s 26ms/step - loss: 0.0348 - acc: 0.9927 - val_loss: 2.6212 - val_acc: 0.6194
Epoch 9/10
2876/2876 [==============================] - 76s 27ms/step - loss: 0.0247 - acc: 0.9944 - val_loss: 2.6898 - val_acc: 0.6298
Epoch 10/10
2876/2876 [==============================] - 75s 26ms/step - loss: 0.0128 - acc: 0.9983 - val_loss: 2.8467 - val_acc: 0.6319
```

## Reference
[Practical Web Scraping for Data Science Best Practices and Examples with Python (ISBN 978-1-4842-3582-9)](https://www.apress.com/us/book/9781484235812)
