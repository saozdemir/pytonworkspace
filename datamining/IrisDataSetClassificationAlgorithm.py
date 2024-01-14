"""
 @author Seyit Ahmet ÖZDEMİR
 @project pytonworkspace Classifications
 @date 9 Oca 2024
 <p>
 @description: sklearn Iris dataseti için K-NN, DecisionTree ve SVM
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

# Iris veri setini yükle
iris = datasets.load_iris()

x = pd.DataFrame(iris.data)
x.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']

y = pd.DataFrame(iris.target)
y.columns = ['Targets']

plt.figure(figsize=(14, 7))

colormap = np.array(['red', 'blue', 'black'])

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

plt.subplot(1, 3, 1)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[predY_knn], s=40)
plt.title('KNN Classification')

plt.subplot(1, 3, 2)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[predY_dt], s=40)
plt.title('Decision Tree Classification')

plt.subplot(1, 3, 3)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[predY_svm], s=40)
plt.title('SVM Classification')

plt.show()

print("KNN Modelin doğruluğu:", sm.accuracy_score(y, predY_knn))
print("Decision Tree Modelin doğruluğu:", sm.accuracy_score(y, predY_dt))
print("SVM Modelin doğruluğu:", sm.accuracy_score(y, predY_svm))