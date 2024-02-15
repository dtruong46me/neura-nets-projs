
import tensorflow as tf
from tensorflow import keras

import os
import numpy as np
import matplotlib.pyplot as plt

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
vgg16_model_path = os.path.join(project_path, 'saved', 'cat_dog_vgg16_model.h5')

img_width, img_height = 224, 224

img_file_name = 'Juvenile_Ragdoll.jpg'
image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), img_file_name))

model = tf.keras.models.load_model(vgg16_model_path)