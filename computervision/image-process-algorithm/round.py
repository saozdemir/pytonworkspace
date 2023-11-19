"""
 @author saozd
 @project pytonworkspace round
 @date 18 Kas 2023
 <p>
 @description:
"""



import numpy as np

# Original 50x50 matrix (example)
original_matrix = np.random.randint(0, 256, (50, 50), dtype=np.uint8)

# Display the original matrix
print("Original 50x50 Matrix:")
print(original_matrix)

# New size (20x20)
new_size = (20, 20)

# Calculate the corresponding coordinates in the original matrix for (2, 6) in the resized matrix
i_resized, j_resized = 2, 6
m = int(i_resized * original_matrix.shape[0] / new_size[0])
n = int(j_resized * original_matrix.shape[1] / new_size[1])

# Calculate the weighted average based on the area overlap
K, L = new_size[0] // original_matrix.shape[0], new_size[1] // original_matrix.shape[1]
weights = np.ones((K, L)) / (K * L)  # Equal weights for simplicity, normalized to sum to 1

# Calculate the new pixel value using the weighted average
new_pixel_value = np.sum(original_matrix[m:m+K, n:n+L] * weights)

# Display the result
print(f"\nNew pixel value at ({i_resized}, {j_resized}) in the resized 20x20 matrix: {new_pixel_value}")
