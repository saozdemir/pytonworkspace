"""
 @author saozd
 @project pytonworkspace EdgeDetection4
 @date 18 Ara 2023
 <p>
 @description:
"""
import cv2
import numpy as np

# Beyin görüntüsü yükleyin
brain_image = cv2.imread("E:/PycharmProjects/pytonworkspace/computervision/article-research/edge-detection/image2.png")

# Gri tonlamalı görüntüyü oluşturun
gray_image = cv2.cvtColor(brain_image, cv2.COLOR_BGR2GRAY)

# Gauss karışım modeli ile beyaz ve gri maddeyi ayırın
gmm_model = cv2.ml.EM_create()
gmm_model.setClustersNumber(2)
gmm_model.trainEM(gray_image)

segmented_data = gmm_model.predict2(gray_image)[1].reshape(gray_image.shape)
gray_matter = np.zeros_like(segmented_data)
gray_matter[segmented_data == 0] = 255
white_matter = np.zeros_like(segmented_data)
white_matter[segmented_data == 1] = 255

# Naive Bayes ile beyaz ve gri maddeyi ayrıştırın
nb_model = cv2.ml.NormalBayesClassifier_create()
nb_model.train(gray_image.reshape(-1, 1), cv2.ml.ROW_SAMPLE, segmented_data)
_, posterior, _, _ = nb_model.predictProb(gray_image.reshape(-1, 1))
posterior = posterior.reshape(gray_image.shape)
gray_matter = np.zeros_like(posterior)
gray_matter[posterior[:, :, 0] > posterior[:, :, 1]] = 255
white_matter = np.zeros_like(posterior)
white_matter[posterior[:, :, 0] < posterior[:, :, 1]] = 255

# Kenarlık görüntüsünü çıkarın
edge_image = cv2.Canny(gray_image, 100, 200)

# Gri madde, beyaz madde ve kenarlık görüntülerini gösterin
cv2.imshow("Gri Madde", gray_matter)
cv2.imshow("Beyaz Madde", white_matter)
cv2.imshow("Kenarlık Görüntüsü", edge_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

