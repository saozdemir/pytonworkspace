"""
 @author saozd
 @project pytonworkspace colleration
 @date 19 Kas 2023
 <p>
 @description:
"""
import numpy as np

# Görüntü matrisi I
I = np.array([[1, 2, 3, 4, 5],
              [5, 4, 3, 2, 1],
              [1, 2, 3, 4, 5],
              [5, 4, 3, 2, 1]])

# Şablon matrisi T
T = np.array([[3, 4],
              [3, 4]])

# Normalizasyon işlemi
I_normalized = (I - np.mean(I)) / np.std(I)
T_normalized = (T - np.mean(T)) / np.std(T)

# Korelasyon hesaplama
correlation_matrix = np.correlate(I_normalized.flatten(), T_normalized.flatten(), mode='full')

# Korelasyon matrisini yeniden boyutlandırma
correlation_matrix = np.resize(correlation_matrix, (I.shape[0] - T.shape[0] + 1, I.shape[1] - T.shape[1] + 1))

print("Görüntü Matrisi (I):")
print(I)
print("\nŞablon Matrisi (T):")
print(T)
print("\nNormalleştirilmiş Görüntü Matrisi (I_normalized):")
print(I_normalized)
print("\nNormalleştirilmiş Şablon Matrisi (T_normalized):")
print(T_normalized)
print("\nKorelasyon Matrisi:")
print(correlation_matrix)

