# -*- coding: utf-8 -*-
"""

Lab 2 - Classification

@author: Amin Kabir - kabir@sfu.ca

"""
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt5')

# Importing libraries 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing the dataset
df0 = pd.read_csv("EMG\EMG_0.csv", header=None)
df1 = pd.read_csv("EMG\EMG_1.csv", header=None)
df2 = pd.read_csv("EMG\EMG_2.csv", header=None)
df3 = pd.read_csv("EMG\EMG_3.csv", header=None)
dataset = pd.concat([df0,df1,df2,df3], axis = 0)

# X: Features, y: Targets
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1].values
class_names = ['rock','scissors','paper','ok']

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Standardize features by removing the mean and scaling to unit variance
from sklearn.preprocessing import StandardScaler
X_train = pd.DataFrame(StandardScaler().fit_transform(X_train))
X_test = pd.DataFrame(StandardScaler().fit_transform(X_test))


### Classification Models

# Decision Trees Classification
from sklearn.tree import DecisionTreeClassifier
MODEL_DT = DecisionTreeClassifier()

# Nearest Neighbors Classification
from sklearn.neighbors import KNeighborsClassifier
MODEL_KNN = KNeighborsClassifier(n_neighbors=5)

# Support Vector Machines
from sklearn import svm
MODEL_SVM = svm.SVC()


# Train the Model
model = MODEL_SVM
model.fit(X_train,y_train)

# Predict the trained Model on our Test data
y_pred = model.predict(X_test)

# Evaluate the trained Model
from sklearn.metrics import classification_report
#from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix

print('Classification Report: \n', classification_report(y_test,y_pred))

# Plot normalized confusion matrix
titles_options = [("Confusion matrix, without normalization", None),
                  ("Normalized confusion matrix", 'true')]
for title, normalize in titles_options:
    disp = plot_confusion_matrix(model, X_test, y_test,
                                 display_labels=class_names,
                                 cmap=plt.cm.Blues,
                                 normalize=normalize)
    disp.ax_.set_title(title)

    print(title)
    print(disp.confusion_matrix)

plt.show()