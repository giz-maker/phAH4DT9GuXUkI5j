# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 14:10:54 2020

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
from sklearn.neighbors import KNeighborsClassifier
#%% import dataset
data=pd.read_csv("term-deposit-marketing-2020.csv", sep=",")
print(data.info())




#%% data visualization
dfk = data.select_dtypes(include =["object"])

#kategorik olanlar
dfk['job'].value_counts().sort_index().plot.bar().set_title("Meslekler Frekansı")

dfk['marital'].value_counts().sort_index().plot.bar().set_title("Medeni Durum Frekansı")

dfk['education'].value_counts().sort_index().plot.bar().set_title("Eğitim Frekansı")

dfk['default'].value_counts().sort_index().plot.bar().set_title("Önceden Batan Kredi Frekansı")

dfk['housing'].value_counts().sort_index().plot.bar().set_title("Ev Kredisi Frekansı")

dfk['loan'].value_counts().sort_index().plot.bar().set_title("Bireysel Kredi Frekansı")

dfk['contact'].value_counts().sort_index().plot.bar().set_title("İletişim Aracı Frekansı")

dfk['month'].value_counts().sort_index().plot.bar().set_title("İletişime Geçilen Son Ay Frekansı")

dfk['y'].value_counts().sort_index().plot.bar().set_title("Cevap Frekansı")





plt.figure(figsize=(3,20),)
sbn.catplot(x="balance",y="job",hue ="education",data = data); 
#Burada meslek grublarına karşı hesap bakiyerini görmek istedim.
#Ayrıca eğitim seviyelerinin de etkisi meslek grupları ile grublayıp bakiyelerin derinliği görmüş oldum.


plt.figure(figsize=(3,20),)
sbn.catplot(x="balance",y="y",hue ="job",data = data); 
#burada hesap bakiyeleri ve yaşa göre kabul ve red oranlarını gözlemledim.









