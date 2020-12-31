# -*- coding: utf-8 -*-
"""
Simon Fraser University - Mechatronic Systems Engineering
Spring 2021 - MSE491 - Application of Machine Learning in Mechatronic Systems
Lab 1  - Regression
@author: Amin Kabir - kabir@sfu.ca
"""

from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt5')

# Importing libraries 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('house_price.csv', header=0)

dataset.sample()

# X: Features, y: Targets
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1].values

# Handling categorical features
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
cols = X.columns
num_cols = X._get_numeric_data().columns
categorical_cols = list(set(cols) - set(num_cols))
X.loc[:,categorical_cols] = X.loc[:,categorical_cols].astype(str)
for cat_col in categorical_cols:
    ind_cat = X.columns.get_loc(cat_col)
    X.iloc[:,ind_cat] = labelencoder_X.fit_transform(X.iloc[:,ind_cat])

# Create our imputer to replace missing values with the mean
from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
imp = imp.fit(X)
X = imp.transform(X)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Save Test Set
np.savetxt("features_house_test.csv", X_test, delimiter=",")
np.savetxt("targets_house_test.csv", y_test, delimiter=",")

#%% Simple Linear Regression

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
simp_lin_reg = LinearRegression()

### Simple Linear Regression
# Only using one feature: "Above grade (ground) living area square feet"
X1_train = X_train[:,45]
X1_train = X1_train.reshape(-1, 1)
X1_test = X_test[:,45]
X1_test = X1_test.reshape(-1, 1)
simp_lin_reg.fit(X1_train, y_train)

# Visualizing the Linear Regression results
def viz_linear():
    plt.scatter(X1_train, y_train, color='red')
    plt.plot(X1_train, simp_lin_reg.predict(X1_train), color='blue')
    plt.title('Linear Regression')
    plt.xlabel('Above grade (ground) living area square feet')
    plt.ylabel('The property sale price in dollars')
    plt.show()
    return
plt.figure()
viz_linear()

# Predicting a random new result 
import random
R_test = random.randrange(len(X_test))
Random_Test = X1_test[R_test].reshape(-1, 1)

# Predicting a new result with Linear Regression
y_pred1 = simp_lin_reg.predict(Random_Test)
print('Predicted sale price for sample %d:   %d' %(R_test,y_pred1))
print('True sale price for sample %d:        %d' %(R_test,y_test[R_test]))

# Evaluation
from sklearn.metrics import r2_score
y_pred = simp_lin_reg.predict(X1_test).astype('int64')
lin_reg_r2 = r2_score(y_test, y_pred)
print('\nSimple Linear Regression - R-Squared: %f' %lin_reg_r2)


#%% Polynomial Regression with 1 Feature for visualization
import random
from sklearn import preprocessing
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

degree = 10

# 1 feature (Linear feet of street connected to property)
# with 20 random samples for visualization
Rp = random.sample(range(0,X_train.shape[0]),20)
ypv_train = y_train[Rp]
Xpv_train = X_train[Rp,2]
Xpv_train = Xpv_train.reshape(-1, 1)

# Standardizing features by removing the mean and scaling to unit variance
scaler = preprocessing.StandardScaler()
### Polynomial Regression - using one feature with 20 samples
polyreg_scaled = make_pipeline(PolynomialFeatures(degree),scaler,LinearRegression())
polyreg_scaled.fit(Xpv_train,ypv_train)

# Visualizing the Polymonial Regression results
poly_pred = polyreg_scaled.predict(Xpv_train)
zipped_pred = zip(Xpv_train, poly_pred)
sorted_pred = sorted(zipped_pred)
tuples = zip(*sorted_pred)
Xpv_train, poly_pred = [list(tuple) for tuple in tuples]

def viz_polymonial():
    plt.scatter(Xpv_train, ypv_train, color='red')
    plt.plot(Xpv_train, poly_pred, color='blue')
    plt.title('Polymonial Regression with 1 Feature for visualization')
    plt.xlabel('Linear feet of street connected to property')
    plt.ylabel('The property sale price in dollars')
    plt.show()
    return
plt.figure()
viz_polymonial()


#%% Multiple Linear Regression

### Multiple Linear Regression - using 10 randome features
import random
R10 = random.sample(range(0,X.shape[1]),10)
X10_train = X_train[:,R10]
X10_test = X_test[:,R10]
mult_lin_reg10 = LinearRegression()
mult_lin_reg10.fit(X10_train, y_train)

### Multiple Linear Regression - using all features
mult_lin_reg = LinearRegression()
mult_lin_reg.fit(X_train, y_train)

# Save Model
import pickle
pickle.dump(mult_lin_reg, open('Model_MLR.pkl', 'wb'))

# Evaluation
from sklearn.metrics import r2_score
y_pred10 = mult_lin_reg10.predict(X10_test).astype('int64')
lin_reg_r2_10 = r2_score(y_test, y_pred10)
print('\nMultiple Linear Regression using 10 randome features - R-Squared: %f' %lin_reg_r2_10)

y_pred = mult_lin_reg.predict(X_test).astype('int64')
lin_reg_r2 = r2_score(y_test, y_pred)
print('\nMultiple Linear Regression using all features - R-Squared: %f' %lin_reg_r2)


#%% Test some non-linear Regression models

### Decision Tree Regressor
from sklearn.tree import DecisionTreeRegressor
dt_reg = DecisionTreeRegressor()
dt_reg.fit(X_train, y_train)
# Save Model
import pickle
pickle.dump(dt_reg, open('Model_DT.pkl', 'wb'))
# Evaluation
from sklearn.metrics import r2_score
y_pred = mult_lin_reg.predict(X_test).astype('int64')
dt_reg_r2 = r2_score(y_test, y_pred)
print('\nDecision Tree Regression - R-Squared: %f' %dt_reg_r2)

### K-Nearest Neighbors Regressor
from sklearn.neighbors import KNeighborsRegressor
knn_reg = KNeighborsRegressor(n_neighbors=5)
# Save Model
import pickle
pickle.dump(knn_reg, open('Model_KNN.pkl', 'wb'))
knn_reg.fit(X_train, y_train)
# Evaluation
from sklearn.metrics import r2_score
y_pred = knn_reg.predict(X_test).astype('int64')
knn_reg_r2 = r2_score(y_test, y_pred)
print('\nK-Nearest Neighbors Regression - R-Squared: %f' %knn_reg_r2)
