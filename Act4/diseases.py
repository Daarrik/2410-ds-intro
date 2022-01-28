# Tensorflow and Keras Neural Network to predict diseases based on training data from Kaggle:
# https://www.kaggle.com/kaushil268/disease-prediction-using-machine-learning

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Generate a dictionary of class labels with a corresponding number value given a list of class labels
def generate_class_numbers(string_list):
  class_dictionary = {}
  class_count = 0
  for string in string_list:
    if string not in class_dictionary:
      class_dictionary[string] = class_count
      class_count += 1
  return class_dictionary

# Convert a list of class labels to a list of numbers using a dictionary with keys that match the list of class labels
# Requires that there is a dictionary entry for every string in string_list
def convert_class_list(class_dictionary, string_list):
  converted_list = []
  for string in string_list:
    converted_list.append(class_dictionary[string])
  return converted_list

def main():
  training_data = pd.read_csv('Training.csv')
  test_data = pd.read_csv('Testing.csv')

  training_data.drop('Unnamed: 133', axis=1, inplace=True)  # pandas reads an extra column for some reason
  x_training = training_data.drop('prognosis', axis=1)
  y_training = np.array(training_data['prognosis'])

  x_testing = test_data.drop('prognosis', axis=1)
  y_testing = np.array(test_data['prognosis'])

  class_dictionary = generate_class_numbers(y_training)
  y_training_nums = np.array(
    convert_class_list(class_dictionary, y_training))
  y_testing_nums = np.array(
    convert_class_list(class_dictionary, y_testing))

  model = keras.Sequential()
  model.add(layers.Input(shape=132))  # Keras automatically adds an input layer if not specified
  # model.add(layers.Dense(100, activation='relu'))
  # model.add(layers.Dense(50, activation='relu'))
  model.add(layers.Dense(units=41, activation='softmax')) # Output layer
  model.compile(optimizer='sgd',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

  model.fit(x=x_training, y=y_training_nums, epochs=100)
  loss, accuracy = model.evaluate(x_testing, y_testing_nums)
  print(f'Model accuracy: {accuracy}')
  
  new_dict = dict([(value, key) for key, value in class_dictionary.items()])
  class_predicted = np.argmax(model.predict(x_testing), axis=-1)
  for predicted, true in zip(class_predicted, y_testing_nums):
    if predicted != true:
      print(f'predicted value {new_dict[predicted]} did not match true value {new_dict[true]}')

  tf.keras.utils.plot_model(model, to_file='./model.png', show_shapes=True, show_layer_names=True)

if __name__ == '__main__':
  main()