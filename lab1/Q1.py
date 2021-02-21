# Load General Libraries
from scipy import stats
import os
import glob
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import scipy

rPath = r"Z:\sibroot\repo\personal\MSE491\SFU_ML\lab1\Gas Turbine Dataset"
os.chdir(rPath)
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
# print(all_filenames)
#combine and import all files in the list to pandas dataframe
dataset = pd.concat([pd.read_csv(f) for f in all_filenames ])

# 1.3
NOX = dataset['NOX']
# np.histogram(NOX, bins=100)
plt.hist(NOX, bins=100)
plt.title('NOX Distribution')
plt.xlabel('NOX Frequency')
plt.ylabel('NOX Amplitude')

# 1.4a
TIT = dataset["TIT"]
TAT = dataset["TAT"]
plt.scatter(TIT,TAT)
plt.title('TIT vs TAT scatterplot')
plt.xlabel('TIT')
plt.ylabel('TAT')
plt.show()

# 1.4b
TEY = dataset["TEY"]
plt.scatter(TIT,TEY)
plt.title('TIT vs TEY scatterplot')
plt.xlabel('TIT')
plt.ylabel('TEY')
plt.show()

# 1.4c
print(scipy.stats.pearsonr(TIT, TAT)[0])
print(scipy.stats.pearsonr(TIT, TEY)[0])

# 1.5
xvar = ['AT','AP','AH','AFDP','GTEP','TIT','TAT','CDP']
X = dataset[xvar]
yvar = ['TEY','CO','NOX']
Y = dataset[yvar]

from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)