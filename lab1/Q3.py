from dataEntry import x_train, x_test, y_train, y_test, X, Y
from Q2 import lineReg
import numpy as np
import matplotlib.pyplot as plt

X_train = np.array(x_train).reshape(-1,8)
X_test = np.array(x_test).reshape(-1,8)
Y_train = np.array(y_train['TEY']).reshape(-1,1)
Y_test = np.array(y_test['TEY']).reshape(-1,1)
rmse1, r21 = lineReg(X_train, Y_train, X_test, Y_test)
Y_train = np.array(y_train['CO']).reshape(-1,1)
Y_test = np.array(y_test['CO']).reshape(-1,1)
rmse2, r22 = lineReg(X_train, Y_train, X_test, Y_test)

plt.bar(['RMSE.TEY', 'RMSE.CO'],[rmse1, rmse2])
plt.title('Multiple Linear Regression: RMSE')
plt.xlabel('models')
plt.ylabel('RMSE')
plt.show()