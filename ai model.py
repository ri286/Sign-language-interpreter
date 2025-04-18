import tensorflow as tf
print("TensorFlow version:", tf.__version__)  # Print the installed TensorFlow version
import os

# Suppress TensorFlow logs (Only show ERROR messages)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

# Ensure TensorFlow is properly imported
try:
    import tensorflow as tf
except ModuleNotFoundError:
    print("TensorFlow is not installed. Run 'pip install tensorflow' manually.")

print("TensorFlow version:", tf.__version__)  # Print the installed TensorFlow version
# -*- coding: utf-8 -*-
"""AI sign language model interpreter.py

Automatically generated by Colab.

Original file is located at
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from google.colab import drive
drive.mount('/content/drive')

import os
from PIL import Image
import numpy as np

main_folder = "/content/drive/MyDrive/Sign language interpreter.jpg/signs"
data = []  # Store image data

# Loop through each subfolder (a, b, c, etc.)
for subfolder in os.listdir(main_folder):
    folder_path = os.path.join(main_folder, subfolder)  # Full path to subfolder

    # Get the first 400 images only
    file_names = sorted(os.listdir(folder_path))[:30]  # Sorting ensures consistent order

    for file_name in file_names:
        if file_name.endswith(".jpg"):  # Ensure it's a JPG file
            img_path = os.path.join(folder_path, file_name)
            img = Image.open(img_path).convert("RGB")  # Convert to RGB
            img = img.resize((128, 128))  # Resize for consistency
            img_array = np.array(img)  # Convert to NumPy array
            data.append(img_array)

data = np.array(data)  # Convert list to NumPy array
print("Total images loaded:", len(data))  # Check how many were processed

import os
data_dir = "/content/drive/MyDrive/Sign language interpreter.jpg/signs"
print(os.listdir(data_dir))  # Should display different sign categories

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Define the model architecture
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(128, 128, 3)),
    MaxPooling2D(pool_size=(2,2)),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(24, activation='softmax')  # 24 classes
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# ipython-input-3-7da7fd5d4a53
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
datagen= ImageDataGenerator(rescale=1./255, validation_split=0.2)
data_dir = "/content/drive/MyDrive/Sign language interpreter.jpg/signs"
# The model is already defined and compiled earlier; no need to redefine here.
# Instead, just use the existing 'model' variable
# model=Sequential([
#     Conv2D(32, (3,3), activation='relu', input_shape=(128, 128, 3)),
#     MaxPooling2D(pool_size=(2,2)),
#     Conv2D(64, (3,3), activation='relu'),
#     MaxPooling2D(pool_size=(2,2)),
#     Flatten(),
#     Dense(128, activation='relu'),
#     Dense(24, activation='softmax')  # 24 classes
# ])
#Compile the model (this was missing)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
train_generator = datagen.flow_from_directory(
    data_dir,
    target_size=(128, 128),
    batch_size=1,
    class_mode='categorical',
    subset='training'
)

val_generator = datagen.flow_from_directory(
    data_dir,
    target_size=(128, 128),
    batch_size=1,
    class_mode='categorical',
    subset='validation'
)

model.fit(train_generator, validation_data=val_generator, epochs=2)

import tensorflow as tf # Import tensorflow
from tensorflow import keras # and keras

model = keras.Sequential([
    keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
    keras.layers.MaxPooling2D(2,2),
    keras.layers.Conv2D(64, (3,3), activation='relu'),
    keras.layers.MaxPooling2D(2,2),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')  # Adjust number of classes
])

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# ... (your previous code) ...

# Define the model architecture
model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    keras.layers.MaxPooling2D(2, 2),
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.MaxPooling2D(2, 2),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(24, activation='softmax')  # Adjust to 24 classes
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Create data generators within the same cell
datagen = ImageDataGenerator(rescale=1. / 255, validation_split=0.2)
data_dir = "/content/drive/MyDrive/Sign language interpreter.jpg/signs"

train_generator = datagen.flow_from_directory(
    data_dir,
    target_size=(128, 128),
    batch_size=1,  # Consider increasing batch size if possible
    class_mode='categorical',
    subset='training'
)

val_generator = datagen.flow_from_directory(
    data_dir,
    target_size=(128, 128),
    batch_size=1,  # Consider increasing batch size if possible
    class_mode='categorical',
    subset='validation'
)

# Fit the model
# Reduced number of epochs to potentially reduce training time
history = model.fit(train_generator, validation_data=val_generator, epochs=1)

# Save the model
model.save("/content/drive/MyDrive/sign_language_model.h5")
