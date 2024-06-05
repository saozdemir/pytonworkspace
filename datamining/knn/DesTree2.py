"""
 @author saozd
 @project pytonworkspace DesTree2
 @date 14 Oca 2024
 <p>
 @description:
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

# Iris veri setini yükleyin
iris = datasets.load_iris()
X = iris.data[:, 2:4]  # Sadece Petal_Length ve Petal_Width özelliklerini kullanıyoruz
y = iris.target

# Veriyi eğitim ve test setlerine ayırın
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# K-NN modelini oluşturun ve eğitin
knn_model = KNeighborsClassifier()
knn_model.fit(X_train, y_train)

# Decision Tree modelini oluşturun ve eğitin
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)

# Test seti üzerinde tahmin yapın
predY_knn = knn_model.predict(X_test)
predY_dt = dt_model.predict(X_test)

# Scatter plot için renk haritası
colormap = np.array(['r', 'g', 'b'])

# Gerçekleşen ve tahmini sonuçları görselleştirin
plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
plt.scatter(X_test[:, 0], X_test[:, 1], c=colormap[y_test], s=40)
plt.title('Gerçek Sınıflar')

plt.subplot(1, 2, 2)
plt.scatter(X_test[:, 0], X_test[:, 1], c=colormap[predY_knn], s=40)
plt.title('KNN Sınıflandırma')

plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
plt.scatter(X_test[:, 0], X_test[:, 1], c=colormap[y_test], s=40)
plt.title('Gerçek Sınıflar')

plt.subplot(1, 2, 2)
plt.scatter(X_test[:, 0], X_test[:, 1], c=colormap[predY_dt], s=40)
plt.title('Decision Tree Sınıflandırma')

plt.show()
