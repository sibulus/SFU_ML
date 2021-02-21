import os
import glob
import pandas as pd

rPath = r"Z:\sibroot\repo\personal\MSE491\SFU_ML\lab1\Gas Turbine Dataset"
os.chdir(rPath)
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
# print(all_filenames)
#combine and import all files in the list to pandas dataframe
dataset = pd.concat([pd.read_csv(f) for f in all_filenames ])

xvar = ['AT','AP','AH','AFDP','GTEP','TIT','TAT','CDP']
X = dataset[xvar]
yvar = ['TEY','CO','NOX']
Y = dataset[yvar]

from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)