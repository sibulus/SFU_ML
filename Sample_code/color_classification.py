# This is a sample code for color classification using a Machine Learning Model
# and the TCS3200 color sensor. This code is inspired by the following article:
# https://www.electronicshub.org/raspberry-pi-color-sensor-tutorial/
# Please note that this code is not tested and may require some edits to get it
# to a working state

# This code shows the inference side of things, the model training needs to be done in advance
# This code could be adapted to obtain training data

import RPi.GPIO as GPIO
import time
import pickle
import numpy as np

LABEL_DICT = {0:"red", 1:"green", 2:"blue", 3:"pink", 4:"black", 5:"white", 6:"brown"}
TRAINED_MODEL_PATH = "/home/pi/SFU_ML/Sample_code/saved_models/color_classification_model.pkl"
s2 = 23
s3 = 24
signal = 25
NUM_CYCLES = 10

def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(s2,GPIO.OUT)
  GPIO.setup(s3,GPIO.OUT)
  print("\n")

def loop(model):
  temp = 1
  while(1):  

    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.LOW)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start      #seconds to run for loop
    red  = NUM_CYCLES / duration   #in Hz
    print("red value - ",red)

    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    blue = NUM_CYCLES / duration
    print("blue value - ",blue)

    GPIO.output(s2,GPIO.HIGH)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    green = NUM_CYCLES / duration
    print("green value - ",green)
    time.sleep(2)  

    input_list = (red, blue, green)
    label_number = model.predict(np.array(input_list).reshape(1, -1))
    print("The predicted label is: {}".format(LABEL_DICT[label_number]))

def endprogram():
    GPIO.cleanup()

if __name__=='__main__':
    
    setup()

    try:
        model = pickle.load(open(TRAINED_MODEL_PATH, 'rb'))
        loop(model)
    except KeyboardInterrupt:
        endprogram()
