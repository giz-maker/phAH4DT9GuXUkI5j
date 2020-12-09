# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 23:47:02 2020

@author: user
"""


"""
1-)Yatırım ürününü satın alma olasılığı daha yüksek olan müşteriler bulmakla da ilgileniyoruz.
 Müşterimizin öncelik vermesi gereken müşteri segmentlerini belirleyin.

2-)Müşterilerin satın almasını sağlayan nedir? 
Bize hangi özelliğe daha fazla odaklanmamız gerektiğini söyleyin.

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

#1 olan değerleri ayrı bir varible'atadık
a=new_data.loc[new_data["y"]=="yes"]
print(a.shape)
#tek tek evet deme durumlarına göre görselleştirme yapıcaz

#medeni durum oranlarında hem veri sayısı hem frekans dökümünü yaptık.
#geri kalanlarında frekans dökümünü yaparak karar vereceğiz.
#en fazla evli kişiler olumlu yanıt vermiştir.
b=a.loc[a["marital"]=="married"]
print(b.shape)

c=a.loc[a["marital"]=="single"]
print(c.shape)

d=a.loc[a["marital"]=="divorced"]
print(d.shape)
a['marital'].value_counts().sort_index().plot.bar().set_title("Medeni Durum Frekansı")

#en fazla mavi yakalılar ve girişimciler olumlu yanıt vermiştir.
a['job'].value_counts().sort_index().plot.bar().set_title("Meslekler Frekansı")

#en fazla orta okul mezunları olumlu yanıt vermiştir.
a['education'].value_counts().sort_index().plot.bar().set_title("Eğitim Frekansı")

#en fazla batan kredisi olmayanlar olumlu yanıt vermiştir.
a['default'].value_counts().sort_index().plot.bar().set_title("Önceden Batan Kredi Frekansı")

#en fazla ev kredisi olmayanlar olumlu yanıt vermiştir.
a['housing'].value_counts().sort_index().plot.bar().set_title("Ev Kredisi Frekansı")

#en fazla bireysel kredisi olmayanlar  olumlu yanıt vermiştir.
a['loan'].value_counts().sort_index().plot.bar().set_title("Bireysel Kredi Frekansı")

#en fazla cep telefonundan ulaşılanlar olumlu yanıt vermiştir.
a['contact'].value_counts().sort_index().plot.bar().set_title("İletişim Aracı Frekansı")

#en fazla nisan ayında olumlu yanıt vermiştir.
a['month'].value_counts().sort_index().plot.bar().set_title("İletişime Geçilen Son Ay Frekansı")




plt.figure(figsize=(3,20),)
sbn.catplot(x="balance",y="y",hue ="job",new_data = new_data); 
#burada hesap bakiyeleri ve yaşa göre kabul ve red oranlarını gözlemledim.

"""
plt.figure(figsize=(3,20),)
sbn.catplot(x="balance",y="y",hue ="job",new_data = new_data); 
#burada hesap bakiyeleri ve mesleklere göre kabul ve red oranlarını gözlemledim.
#balance_kabul grafiğinde görebilirsiniz
"""
"""
plt.figure(figsize=(3,20),)
sbn.catplot(x="day",y="y",hue ="job",new_data = new_data); 
"""
plt.figure(figsize=(3,20),)
sbn.catplot(x="duration",y="y",hue ="job",new_data = new_data); 
"""
1-) Yatırım ürününü alma oranlarına baktığımız zaman herhangi bir kredi borcu olmayan insanlar bu konuda çok daha fazla olumlu yanıt vermiştir.
Meslek grupların da ise mavi yakalılar ve girişimciler çok daha fazla olumlu yanıt vermiştir.
Bakiye durumu verilere bakıldığında etkilemediği gözlenmiştir.



"""
"""
2-) Müşteriye ulaşılan son ay bazında baktığımız zaman nisan ayında çok büyük bir sıçrama ile olumlu yanıt miktarı artmıştır.Bu kesinlikle göz önünde bulundurulmalıdır.
Duration ve day etkilemez.Görselleri duration ve day isimli grafiklerde gözlemlenebilir.
Cep telefonundan aranan insanlar daha fazla olumlu yanıt vermiştir.

"""
"""
Bu dataset için en başarılı eğitimi yapan model Random Forest'tır.

"""