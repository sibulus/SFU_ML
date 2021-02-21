from dataEntry import x_train, x_test, y_train, y_test, X, Y
from Q2 import lineReg, sortByCoeff
import numpy as np
import matplotlib.pyplot as plt

corr1 = sortByCoeff(x_train,y_train['TEY'])
corr2 = sortByCoeff(x_train,y_train['CO'])
TEY4 = []
CO4 = []

for i in range(0,4):
    TEY4.append(corr1[i][1])
    CO4.append(corr2[i][1])
# print(TEY4)

X_train = np.array(x_train[TEY4]).reshape(-1,4)
X_test = np.array(x_test[TEY4]).reshape(-1,4)
Y_train = np.array(y_train['TEY']).reshape(-1,1)
Y_test = np.array(y_test['TEY']).reshape(-1,1)
rmse1, r21 = lineReg(X_train, Y_train, X_test, Y_test)

X_train = np.array(x_train[CO4]).reshape(-1,4)
X_test = np.array(x_test[CO4]).reshape(-1,4)
Y_train = np.array(y_train['CO']).reshape(-1,1)
Y_test = np.array(y_test['CO']).reshape(-1,1)
rmse2, r22 = lineReg(x_train, Y_train, x_test, Y_test)

plt.bar(['TEY4', 'CO4'],[rmse1, rmse2])
plt.title('Multiple Linear Regression: RMSE')
plt.xlabel('models')
plt.ylabel('RMSE')
plt.show()