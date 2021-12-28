# -*- coding: utf-8 -*-
"""REVIEW2-OWNMODEL.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uExqL_OkWww5eqqoDqPQbEjVvLh9HTAt
"""

from google.colab import drive
drive.mount('/content/drive')



import tensorflow as tf
from tensorflow.keras.applications import InceptionV3,VGG19
# from tensorflow.keras.applications import VGG19
from tensorflow.keras.layers import Input, Lambda, Dense, Flatten,Conv2D, MaxPooling2D,Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img
from tensorflow.keras.models import Sequential,load_model
import numpy as np
import matplotlib.pyplot as plt

train_datagen = ImageDataGenerator(rescale = 1./255,validation_split=0.2,horizontal_flip=True, zoom_range=0.2, vertical_flip=True,shear_range=0.2)

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.1))
model.add(Conv2D(48, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.1))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(80, activation='relu'))
model.add(Dense(4, activation='softmax'))

model.compile(optimizer= 'adam', loss= 'categorical_crossentropy', metrics=['accuracy'])

h1=model.fit(training_set, validation_data=validation_set, epochs=50)

plt.plot(h1.history['loss'])
plt.plot(h1.history['val_loss'])
plt.title('Loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['loss', 'val_loss'], loc='upper left')
plt.show()

plt.plot(h1.history['accuracy'])
plt.plot(h1.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.5))
model.add(Conv2D(48, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.5))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.1))
model.add(Flatten())
model.add(Dense(80, activation='relu'))
model.add(Dense(4, activation='softmax'))

model.compile(optimizer= 'adam', loss= 'categorical_crossentropy', metrics=['accuracy'])

h2=model.fit(training_set, validation_data=validation_set, epochs=50)

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.05))
model.add(Conv2D(48, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.05))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.1))
model.add(Flatten())
model.add(Dense(80, activation='relu'))
model.add(Dense(4, activation='softmax'))

model.compile(optimizer= 'adam', loss= 'categorical_crossentropy', metrics=['accuracy'])

h3=model.fit(training_set, validation_data=validation_set, epochs=100)

plt.plot(h3.history['accuracy'])
plt.plot(h3.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

plt.plot(h3.history['loss'])
plt.plot(h3.history['val_loss'])
plt.title('Loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['loss', 'val_loss'], loc='upper left')
plt.show()

plt.plot(h3.history['accuracy'])
plt.plot(h3.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(48, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.05))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(80, activation='relu'))
model.add(Dense(4, activation='softmax'))

model.compile(optimizer= 'adam', loss= 'categorical_crossentropy', metrics=['accuracy'])

h4=model.fit(training_set, validation_data=validation_set, epochs=100)

plt.plot(h3.history['loss'])
plt.plot(h3.history['val_loss'])
plt.title('Loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['loss', 'val_loss'], loc='upper left')
plt.show()

plt.plot(h3.history['accuracy'])
plt.plot(h3.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()



model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(48, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.05))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.1))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(80, activation='relu'))
model.add(Dense(4, activation='softmax'))



model.compile(optimizer= 'adam', loss= 'categorical_crossentropy', metrics=['accuracy'])

h5=model.fit(training_set, validation_data=validation_set, epochs=50)

plt.plot(h5.history['accuracy'])
plt.plot(h5.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

"""# FINAL VANILLA CNN

"""

train_datagen = ImageDataGenerator(rescale = 1./255,validation_split=0.2,horizontal_flip=True, zoom_range=0.2, vertical_flip=True,shear_range=0.2)

training_set = train_datagen.flow_from_directory('/content/drive/MyDrive/GGG/',
                                                 target_size = (100, 100),
                                                 batch_size = 128,
                                                 class_mode = 'categorical',
                                                 subset = 'training')
validation_set = train_datagen.flow_from_directory('/content/drive/MyDrive/GGG/',
                                                 target_size = (100, 100),
                                                 batch_size = 128,
                                                 class_mode = 'categorical',
                                                 subset = 'validation')

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(48, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.1))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.1))
model.add(Flatten())
model.add(Dense(80, activation='relu'))
model.add(Dense(4, activation='softmax'))

model.compile(optimizer= 'adam', loss= 'categorical_crossentropy', metrics=['accuracy'])

h6=model.fit(training_set, validation_data=validation_set, epochs=100)

plt.plot(h6.history['accuracy'])
plt.plot(h6.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

import tensorflow as tf
from tensorflow.keras.applications import InceptionV3,VGG19
# from tensorflow.keras.applications import VGG19
from tensorflow.keras.layers import Input, Lambda, Dense, Flatten,Conv2D, MaxPooling2D,Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img
from tensorflow.keras.models import Sequential,load_model
import numpy as np
import matplotlib.pyplot as plt

def histogram_equalization(img_in):
# segregate color streams
    b,g,r = cv2.split(img_in)
    h_b, bin_b = np.histogram(b.flatten(), 256, [0, 256])
    h_g, bin_g = np.histogram(g.flatten(), 256, [0, 256])
    h_r, bin_r = np.histogram(r.flatten(), 256, [0, 256])
# calculate cdf    
    cdf_b = np.cumsum(h_b)  
    cdf_g = np.cumsum(h_g)
    cdf_r = np.cumsum(h_r)
    
# mask all pixels with value=0 and replace it with mean of the pixel values 
    cdf_m_b = np.ma.masked_equal(cdf_b,0)
    cdf_m_b = (cdf_m_b - cdf_m_b.min())*255/(cdf_m_b.max()-cdf_m_b.min())
    cdf_final_b = np.ma.filled(cdf_m_b,0).astype('uint8')
  
    cdf_m_g = np.ma.masked_equal(cdf_g,0)
    cdf_m_g = (cdf_m_g - cdf_m_g.min())*255/(cdf_m_g.max()-cdf_m_g.min())
    cdf_final_g = np.ma.filled(cdf_m_g,0).astype('uint8')
    cdf_m_r = np.ma.masked_equal(cdf_r,0)
    cdf_m_r = (cdf_m_r - cdf_m_r.min())*255/(cdf_m_r.max()-cdf_m_r.min())
    cdf_final_r = np.ma.filled(cdf_m_r,0).astype('uint8')
# merge the images in the three channels
    img_b = cdf_final_b[b]
    img_g = cdf_final_g[g]
    img_r = cdf_final_r[r]
  
    img_out = cv2.merge((img_b, img_g, img_r))
# validation
    equ_b = cv2.equalizeHist(b)
    equ_g = cv2.equalizeHist(g)
    equ_r = cv2.equalizeHist(r)
    equ = cv2.merge((equ_b, equ_g, equ_r))
    #print(equ)
    #cv2.imwrite('output_name.png', equ)
    return img_out
datagen = ImageDataGenerator(validation_split=0.2,rotation_range=30, horizontal_flip=0.5, preprocessing_function=histogram_equalization)



training_set = train_datagen.flow_from_directory('/content/drive/MyDrive/GGG/',
                                                 target_size = (100, 100),
                                                 batch_size = 128,
                                                 class_mode = 'categorical',
                                                 subset = 'training')
validation_set = train_datagen.flow_from_directory('/content/drive/MyDrive/GGG/',
                                                 target_size = (100, 100),
                                                 batch_size = 128,
                                                 class_mode = 'categorical',
                                                 subset = 'validation')



model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(48, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.1))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.1))
model.add(Flatten())
model.add(Dense(80, activation='relu'))
model.add(Dense(4, activation='softmax'))

model.compile(optimizer= 'adam', loss= 'categorical_crossentropy', metrics=['accuracy'])