"""
 @author Seyit Ahmet ÖZDEMİR
 @project pytonworkspace KnnAlgorithm
 @date 14 Oca 2024
 <p>
 @description: İris Veri Seti üzerinde KNN algoritmasının uygulandığı uygulamadır.
"""
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from matplotlib.colors import ListedColormap

# Iris veri setini yükle
iris = load_iris()

# Özellikler ve etiketler
X = iris.data[:, :2]  # İlk iki özelliği alıyoruz
y = iris.target

# KNN modelini oluştur (K=3 için)
knn = KNeighborsClassifier(n_neighbors=3)

# Modeli eğit
knn.fit(X, y)

# Tüm veri setinde tahmin yap
y_pred = knn.predict(X)

# Modelin doğruluğunu kontrol et
print("Modelin doğruluğu:", metrics.accuracy_score(y, y_pred))

# Kümeleme öncesi ve sonrası için sınıflandırma grafiklerini çiz
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor='k', s=20)
plt.xlim(X[:, 0].min() - 1, X[:, 0].max() + 1)
plt.ylim(X[:, 1].min() - 1, X[:, 1].max() + 1)
plt.title("Kümeleme Öncesi")

plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap=cmap_light, edgecolor='k', s=20)
plt.xlim(X[:, 0].min() - 1, X[:, 0].max() + 1)
plt.ylim(X[:, 1].min() - 1, X[:, 1].max() + 1)
plt.title("Kümeleme Sonrası")

plt.show()