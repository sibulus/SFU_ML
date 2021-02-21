from Q1 import xvar, yvar
from Q2 import x_train, x_test, y_train, y_test, X, Y

import random
import math
import numpy as np
from sklearn import preprocessing
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression

def polyReg (deg, x, y):
    # Try with polynomial of degree 3
    degree = deg

    # 1 feature (Linear feet of street connected to property)
    # with 20 random samples for visualization
    ypv_train = y_train[y]
    Xpv_train = x_train[x]
    Xpv_train = np.array(Xpv_train).reshape(-1, 1)
    ypv_train = np.array(ypv_train).reshape(-1, 1)

    # Standardizing features by removing the mean and scaling to unit variance
    scaler = preprocessing.StandardScaler()
    polyreg_scaled = make_pipeline(PolynomialFeatures(degree),scaler,LinearRegression())
    polyreg_scaled.fit(Xpv_train,ypv_train)

    # Visualizing the Polymonial Regression results
    xTest = np.array(x_test[x]).reshape(-1,1)
    poly_pred = polyreg_scaled.predict(xTest)
    zipped_pred = zip(xTest, poly_pred)
    # print(type(zipped_pred))
    sorted_pred = sorted(zipped_pred)
    tuples = zip(*sorted_pred)
    xTest, poly_pred = [list(tuple) for tuple in tuples]
    # plt.figure()
    # viz_polymonial(Xpv_train, ypv_train, poly_pred, x, y)

    yTest = np.array(y_test[y]).reshape(-1,1)
    poly_reg_r2 = r2_score(yTest, poly_pred)
    mse = mean_squared_error(yTest, poly_pred)
    rmse = math.sqrt(mse)
    
    # print('rmse: ',rmse, 'r2: ', lin_reg_r2)
    return rmse, poly_reg_r2

results = []
for i in xvar:
    for y in yvar:
        for j in [2,5,11]:
            rmse, r2 = polyReg(j, i, y)
            result = [j, i, y, rmse, r2]
            print(result)
            results.append(result)

results = []
for i in range(2,15):
    rmse, r2 = polyReg(i, 'AT', 'NOX')
    result = [j, i, y, rmse, r2]
    # print(result)
    results.append(result)

from operator import itemgetter

results = []
for i in xvar:
    for y in yvar:
        sortL = []
        for j in (2,15):
            rmse, r2 = polyReg(j, i, y)
            result = [rmse, j, i, y, r2]
            sortL.append(result)
        sortL.sort(reverse = False)
        print(sortL[0])
        results.append(sortL[0])