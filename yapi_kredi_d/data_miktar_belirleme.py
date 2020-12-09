# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:25:12 2020

@author: user
"""


#%%  libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn
from sklearn.linear_model import LinearRegression
import altair as alt
from vega_datasets import data as vega_data
from sklearn import preprocessing
#from vega_datasets import data as vega_data
from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
onehotencoder = preprocessing.OneHotEncoder()
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier



#%% import dataset
new_data=pd.read_csv("term-deposit-marketing-2020.csv", sep=",")
print(new_data.info())

#Duration bilgisi tahminlemenin yapıldığı esnada bilinemeyeceği için çıkartılacak

new_data.drop(["duration"],axis=1,inplace=True)
#1 olan değerleri ayrı bir varible'atadık
a=new_data.loc[new_data["y"]=="yes"]
print(a.shape)
#0 olan değerleri ayrı bir varible'a atayıp son 3104 tanesini aldık
c=new_data.loc[new_data["y"]=="no"]
z=c.drop(c.index[0:33000])
print(z.shape)
#seçtiğimiz datalardan yeni bir dataset oluşturduk
data = a.append(z.iloc[:])
print(data.shape)
#%% kategorik verileri binary'e dönüştürme

data['default']= label_encoder.fit_transform(data['default'])
data

data['job']= label_encoder.fit_transform(data['job'])
data

data['education']= label_encoder.fit_transform(data['education'])
data

data['month']= label_encoder.fit_transform(data['month'])
data

data['marital']= label_encoder.fit_transform(data['marital'])
data

data['housing']= label_encoder.fit_transform(data['housing'])
data

data['loan']= label_encoder.fit_transform(data['loan'])
data

data['y']= label_encoder.fit_transform(data['y'])
data

data.drop(["contact"],axis=1,inplace=True)




