"""
Created on Tue Nov  6 14:33:45 2018
Feature extraction and activity detection using AndroSensor.
All mobile senosr data is collected using AndroSensor mobiel app.
Data is imported and visualozed using pandas and matplolib libearies.
Feature isextracted using sliding window and activity is evaluated.

Feature Extracted from 'stairs_n_jumps.csv':
        1. Number of stairs
        2. Number of jumps
        3. Source of noise
@author: rahulm99
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

def peak_counter(column, threshold):
    ''' Calculate peak points within given range and threshold.
        Works as sliding window function to select the range.
        In:
            column: string value for column
            threshold: integer value to eliminate lower values
        Return:
            Number of peaks in given range
    '''
    filtered_data = (DATA_FIELD[column] - DATA_FIELD[column].mean())
    peak, _ = find_peaks(filtered_data, height=threshold)
    num_peak = len(peak)
    return num_peak

#import the sensor data from .csv file
DATA_FIELD = pd.read_csv('stairs_n_jumps.csv')

ACC_X = DATA_FIELD['ACCELEROMETER X']
ACC_Y = DATA_FIELD['ACCELEROMETER Y']
ACC_Z = DATA_FIELD['ACCELEROMETER Z']

#New column is added in dataframe, contains RMS value of accelerometer of all three axis.
DATA_FIELD['ACC_RMS'] = np.sqrt(DATA_FIELD['ACCELEROMETER X'] **2 + DATA_FIELD['ACCELEROMETER Y'] ** 2 + DATA_FIELD['ACCELEROMETER Z'] **2)
plt.plot(DATA_FIELD.index, DATA_FIELD['ACC_RMS'])
plt.show()

print("Number of stairs : ", peak_counter('ACC_RMS', 2))
print("Number of jumps : ", peak_counter('ACC_RMS', 6))

SOUND = DATA_FIELD['SOUND LEVEL']
plt.title('SOUND LEVEL')
plt.plot(DATA_FIELD.index, SOUND)
plt.show()
'''
To check the sound lvevl.
We used http://www.industrialnoisecontrol.com/comparative-noise-examples.htm
database.
'''
print("Source of NOISE: ")
if np.mean(SOUND) < 10:
    print("Breathing")
elif np.mean(SOUND) < 20:
    print("Whisper, rustling leaves")
elif np.mean(SOUND) < 30:
    print("Quiet rural area")
elif np.mean(SOUND) < 40:
    print("Library, bird calls")
elif np.mean(SOUND) < 50:
    print("Quiet suburb, conversation at home")
elif np.mean(SOUND) < 60:
    print("Conversation in restaurant, office, background music, Air conditioning unit")
elif np.mean(SOUND) < 70:
    print("Passenger car at 65 mph at 25 ft")
elif np.mean(SOUND) < 80:
    print("Garbage disposal, dishwasher, average factory, freight train (at 15 meters)")
else:
    print("Above 80 dB. More noise.")
    
