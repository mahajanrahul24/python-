# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:33:45 2018
Feature extraction and activity detection using AndroSensor.
All mobile senosr data is collected using AndroSensor mobiel app.
Data is imported and visualozed using pandas and matplolib libearies.
Feature isextracted using sliding window and activity is evaluated.

Feature Extracted from 'stairs_n_jumps.csv':
        1. Number of stairs 
        2. Number of jumps
        3. Noise during walking 
        
@author: rahulm99
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

def peak_counter(lower_bound, upper_bound, column, threshold):
    ''' Calculate peak points within given range and threshold.
        Works as sliding window function to select the range.
        In:
            lower_bound: integer lower limit in range
            upper_bound: integer upper bound in limit
            column: string value for column
            threshold: integer value to eliminate lower values
        Return:
            Number of peaks in given range
    '''
    filtered_data = DATA_FIELD[column].iloc[lower_bound:upper_bound]
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

print("Number of steps : ", peak_counter(0, 100, 'ACC_RMS', 11))
print("Number of jumps : ", peak_counter(100, 150, 'ACC_RMS', 14))

SOUND = DATA_FIELD['SOUND LEVEL']
plt.title('SOUND LEVEL')
plt.plot(DATA_FIELD.index, SOUND)
plt.show()

SOUND_LEVEL = peak_counter(0, 250, 'SOUND LEVEL', 65)
#number of peaks observed above 65dB sound level.
#Most of the TIME sound level is greater than 65dB
#According to noise level, concluion is made as Conversation in office or restaurant.
if SOUND_LEVEL > 25:
    print("Conevrsation is going on ")
