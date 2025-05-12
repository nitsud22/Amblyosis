import tensorflow as tf
import numpy as np


#Instantiate a base model for transfer learning
base_model = tf.keras.applications.Xception(
    weights = 'imagenet',
    input_shape = (150, 150, 3),
    include_top = False
)

#Freeze the base_model layers
base_model.trainable = False

base_model.summary()

#Create a new model on top of base_model
inputs = keras.Input(shape=(150, 150, 3))