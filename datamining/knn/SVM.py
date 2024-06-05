"""
 @author saozd
 @project pytonworkspace SVM
 @date 14 Oca 2024
 <p>
 @description:
"""
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import SVC
import sklearn.metrics as sm

import pandas as pd
import numpy as np

iris = datasets.load_iris()

x = pd.DataFrame(iris.data)
x.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']

y = pd.DataFrame(iris.target)
y.columns = ['Targets']

plt.figure(figsize=(14, 7))

colormap = np.array(['red', 'blue', 'black'])

plt.subplot(1, 2, 1)
plt.scatter(x.Sepal_Length, x.Sepal_Width, c=colormap[y.Targets], s=40)
plt.title('Sepal')

plt.subplot(1, 2, 2)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[y.Targets], s=40)
plt.title('Petal')
plt.show()
plt.close()

# SVM modelini oluştur
model = SVC()

# Modeli eğit
model.fit(x, y.values.ravel())

# Tüm veri setinde tahmin yap
predY = model.predict(x)

plt.figure(figsize=(14, 7))

colormap = np.array(['red', 'blue', 'black'])

plt.subplot(1, 2, 1)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[y.Targets], s=40)
plt.title('Real Classification')

plt.subplot(1, 2, 2)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[predY], s=40)
plt.title('SVM Classification')

print("Modelin doğruluğu:", sm.accuracy_score(y, predY))