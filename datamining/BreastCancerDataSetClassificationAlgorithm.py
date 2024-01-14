"""
 @author saozd
 @project pytonworkspace BreastCancer
 @date 9 Oca 2024
 <p>
 @description: sklearn Breast Cancer dataseti için K-NN, DecisionTree ve SVM
 algoritmalrının sınflandırma grafiklerini çizer.
 Doğruluk oranlarını hesaplayarak yazdırır.
"""
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import sklearn.metrics as sm
import pandas as pd
import numpy as np

# Breast Cancer veri setini yükle
cancer = datasets.load_breast_cancer()

# Özellikler ve etiketler
x = pd.DataFrame(cancer.data, columns=cancer.feature_names)
y = pd.DataFrame(cancer.target, columns=['Targets'])

# KNN modelini oluştur (K=3 için)
model_knn = KNeighborsClassifier(n_neighbors=3)
model_knn.fit(x, y.values.ravel())
predY_knn = model_knn.predict(x)

# Karar Ağaçları modelini oluştur
model_dt = DecisionTreeClassifier()
model_dt.fit(x, y.values.ravel())
predY_dt = model_dt.predict(x)

# SVM modelini oluştur
model_svm = SVC()
model_svm.fit(x, y.values.ravel())
predY_svm = model_svm.predict(x)

# İlk iki özelliği alarak sınıflandırma sonuçlarını görselleştir
plt.figure(figsize=(14, 7))
colormap = np.array(['red', 'blue', 'black'])

plt.subplot(1, 3, 1)
plt.scatter(x.iloc[:, 0], x.iloc[:, 1], c=colormap[predY_knn], s=40)
plt.title('KNN Classification')

plt.subplot(1, 3, 2)
plt.scatter(x.iloc[:, 0], x.iloc[:, 1], c=colormap[predY_dt], s=40)
plt.title('Decision Tree Classification')

plt.subplot(1, 3, 3)
plt.scatter(x.iloc[:, 0], x.iloc[:, 1], c=colormap[predY_svm], s=40)
plt.title('SVM Classification')

plt.show()

print("KNN Modelin doğruluğu:", sm.accuracy_score(y, predY_knn))
print("Decision Tree Modelin doğruluğu:", sm.accuracy_score(y, predY_dt))
print("SVM Modelin doğruluğu:", sm.accuracy_score(y, predY_svm))