# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:59:49 2020

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
from sklearn.naive_bayes import GaussianNB


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
#%% yes-no cevaplarını binary'e dönüştürme

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

#%% normalization

x=(data-np.min(data))/(np.max(data)-np.min(data))
y=data.y.values
x.drop(["y"],axis=1,inplace=True)
#%% train test data

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)


#%% naive bayes modeli   acc=0.833571

nb=GaussianNB()
nb.fit(x_train,y_train)

print("naive bayes acc:",nb.score(x_test,y_test))

#%% confussion matrix
y_pred=nb.predict(x_test)
y_true=y_test
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_true,y_pred)

f,ax=plt.subplots(figsize=(5,5))
sbn.heatmap(cm,annot=True,linewidths=0.5,linecolor="red",fmt=".0f",ax=ax)
plt.xlabel("y_pred")
plt.ylabel("y_true")
plt.show()

