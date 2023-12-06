import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
from scipy import stats
from scipy.stats import ttest_ind, mannwhitneyu

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

def decision_tree_model(X_train, y_train):
    features = ['monthly_charges', 'senior_citizen', 'tenure']  

    tree = DecisionTreeClassifier(max_depth=3, random_state=123)

    tree.fit(X_train[features], y_train)
  
    return(print('Accuracy of Decision Tree classifier on training set: {:.2f}'.format(tree.score(X_train[features], y_train))))

def random_forest_model(X_train, y_train):
    features = ['monthly_charges', 'senior_citizen', 'tenure']

    rf = RandomForestClassifier(min_samples_leaf=9, max_depth=2, random_state=123)

    rf.fit(X_train[features], y_train)

    return(print('Accuracy of Random Forest classifier on training set: {:.2f}'.format(rf.score(X_train[features], y_train))))

def linear_regression_model(X_train, y_train):
    features = ['monthly_charges','tenure','senior_citizen']
    
    lr = LogisticRegression()
    lr.fit(X_train[features], y_train)
       
    return(print('Accuracy of Linear Regression classifier on training set: {:.2f}'.format(lr.score(X_train[features], y_train))))
