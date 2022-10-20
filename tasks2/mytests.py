from functions_vectorised import cosine_distance
import numpy as np

X = np.array([[0, 0, 0], [1, 0, 0]])
Y = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(cosine_distance(X, Y))