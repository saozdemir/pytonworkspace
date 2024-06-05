"""
 @author saozd
 @project pytonworkspace Titanic
 @date 14 Oca 2024
 <p>
 @description:
"""
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import sklearn.metrics as sm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
import seaborn as sns

# Titanic veri setini yükle
titanic = sns.load_dataset('titanic')

# Eksik verileri doldur
titanic.fillna(method='ffill', inplace=True)

# Kategorik özellikleri sayısal hale getir
le = LabelEncoder()
titanic['sex'] = le.fit_transform(titanic['sex'])
titanic['embarked'] = le.fit_transform(titanic['embarked'])

# Özellikler ve etiketler
x = titanic.drop(['survived'], axis=1)
y = titanic['survived']

# Veriyi eğitim ve test setlerine ayır
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

# KNN modelini oluştur (K=3 için)
model_knn = KNeighborsClassifier(n_neighbors=3)
model_knn.fit(x_train, y_train)
predY_knn = model_knn.predict(x_test)

# Karar Ağaçları modelini oluştur
model_dt = DecisionTreeClassifier()
model_dt.fit(x_train, y_train)
predY_dt = model_dt.predict(x_test)

# SVM modelini oluştur
model_svm = SVC()
model_svm.fit(x_train, y_train)
predY_svm = model_svm.predict(x_test)

print("KNN Modelin doğruluğu:", sm.accuracy_score(y_test, predY_knn))
print("Decision Tree Modelin doğruluğu:", sm.accuracy_score(y_test, predY_dt))
print("SVM Modelin doğruluğu:", sm.accuracy_score(y_test, predY_svm))