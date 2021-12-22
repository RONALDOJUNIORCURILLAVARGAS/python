import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt 
import cv2
datos , metadatos =tfds.load('cats_vs_dogs', as_supervised=True,with_info=True)
