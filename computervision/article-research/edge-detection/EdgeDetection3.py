"""
 @author saozd
 @project pytonworkspace EdgeDetection3
 @date 17 Ara 2023
 <p>
 @description:
"""
import numpy as np
import cv2
from sklearn.mixture import GaussianMixture
from sklearn.naive_bayes import GaussianNB

# Görüntüyü yükle (örneğin: beyin MRI)
img = cv2.imread('E:/PycharmProjects/pytonworkspace/computervision/article-research/edge-detection/image2.png', cv2.IMREAD_GRAYSCALE)


# Gauss karışım modeli ile gri madde ve beyaz madde ayrımı
gmm = GaussianMixture(n_components=2)
img_flat = img.reshape((-1, 1))
gmm.fit(img_flat)
segmentation = gmm.predict(img_flat)
segmentation = segmentation.reshape(img.shape)

# Gri madde ve beyaz madde üzerinde Naive Bayes sınıflandırıcı
gray_matter = img[segmentation == 0]
white_matter = img[segmentation == 1]

# Sınıf belirleme için Naive Bayes
nb_classifier = GaussianNB()
nb_classifier.fit(gray_matter.reshape((-1, 1)), np.zeros_like(gray_matter))
nb_classifier.fit(white_matter.reshape((-1, 1)), np.ones_like(white_matter))

# MAP ile doku sınıfı belirleme
posterior_probabilities = nb_classifier.predict_proba(img.reshape((-1, 1)))
posterior_gray = posterior_probabilities[:, 0].reshape(img.shape)
posterior_white = 1 - posterior_gray  # 1 - posterior_gray olarak beyaz madde olasılığını hesapla

# Expectation Maximization (EM) algoritması ile olasılık dağılımı
gmm_em = GaussianMixture(n_components=2)
gmm_em.fit(img_flat)

# EM ile oluşturulan olasılık dağılımından kenarlık görüntüsü çıkarma
prob_density = np.exp(gmm_em.score_samples(img_flat))
prob_density = prob_density.reshape(img.shape)
edge_image = np.abs(np.gradient(prob_density))[0]

# Sonuçları görselleştirme
cv2.imshow('Original Image', img)
cv2.imshow('Segmentation', segmentation.astype(np.uint8) * 255)
cv2.imshow('Gray Matter Posterior Probability', (posterior_gray * 255).astype(np.uint8))
cv2.imshow('White Matter Posterior Probability', (posterior_white * 255).astype(np.uint8))
cv2.imshow('EM Probability Density', (prob_density / np.max(prob_density) * 255).astype(np.uint8))
cv2.imshow('Edge Image', (edge_image / np.max(edge_image) * 255).astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()