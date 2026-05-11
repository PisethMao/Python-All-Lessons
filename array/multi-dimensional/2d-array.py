import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
print(arr[1][2])
subarr = arr[1:3]
print(subarr)
subarr *= 2
print(subarr)
print(np.sum(arr))
print(np.mean(arr, axis=1))
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.dot(arr, b))