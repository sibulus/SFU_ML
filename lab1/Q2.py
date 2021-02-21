from dataEntry import x_train, x_test, y_train, y_test, X, Y
from scipy import stats
import os
import glob
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import scipy

# 2.1/2.2
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn import model_selection
import sklearn
import math

# Ranks input by correlation
def sortByCoeff(x, y):
    # iterate through x and store correlation
    correlations = []
    for i in x:
        currentP = scipy.stats.pearsonr(x[i], y)
        pearson = abs(currentP[0])
        correlations.append([pearson,i])    
    #sort correlations
    correlations.sort(reverse = True)
    return correlations

# builds simple linear regression 
def lineReg(xTrain,yTrain,xTest,yTest):
    simp_lin_reg = LinearRegression()
    simp_lin_reg.fit(xTrain, yTrain)
    y_pred = simp_lin_reg.predict(xTest).astype('int64')
    lin_reg_r2 = r2_score(yTest, y_pred)
    mse = mean_squared_error(yTest, y_pred)
    rmse = math.sqrt(mse)
    # print('rmse: ',rmse, 'r2: ', lin_reg_r2)
    return rmse, lin_reg_r2
# print(lineReg(x_train[NOXBest],y_train['NOX'], x_test(NOXBest), y_test['NOX']))

def SLR22(target):
    a = sortByCoeff(x_train, y_train[target])
    NOXBest = a[0][1]
    X1_train = np.array(x_train[NOXBest]).reshape(-1,1)
    Y1_train = np.array(y_train[target]).reshape(-1,1)
    X1_test = np.array(x_test[NOXBest]).reshape(-1,1)
    Y1_test = y_test[target]
    print(NOXBest,',', target, ' rmse & r2 Test: ',lineReg(X1_train, Y1_train, X1_test, Y1_test))
    print(NOXBest,',', target, ' rmse & r2 Train: ',lineReg(X1_train, Y1_train, X1_train, Y1_train))

SLR22('TEY')
SLR22('CO')
SLR22('NOX')

# 2.3
RMSEs = []
for i in [0.5, 0.3, 0.1]:
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size= i, random_state=0)
    X_test = np.array(x_test['TIT']).reshape(-1,1)
    Y_test = np.array(y_test['CO']).reshape(-1,1)
    X_train = np.array(x_train['TIT']).reshape(-1,1)
    Y_train = np.array(y_train['CO']).reshape(-1,1)

    rmse0, r21 = lineReg(X_train, Y_train, X_train, Y_train)
    rmse1, r22 = lineReg(X_train, Y_train, X_test, Y_test)
    RMSEs.append(rmse0)
    RMSEs.append(rmse1)
# print(RMSEs)
plt.bar(["50%Train", "50%Test", "70%Train", "30%Test","90%Train", "10%Test",],RMSEs)
plt.title('effect of training/testing split on RMSE for TIT vs CO')
plt.xlabel('split')
plt.ylabel('RMSE')
plt.show()