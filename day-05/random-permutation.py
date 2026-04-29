# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])

# shuffled = np.random.permutation(arr)

# print("Original:", arr)
# print("Shuffled:", shuffled)

# import numpy as np
# x=np.random.permutation(5)
# print(x)

# arr = np.array([[1,2],
#                 [3,4],
#                 [5,6]])

# shuffled = np.random.permutation(arr)
# print(shuffled)

# arr = np.array([1, 2, 3, 4, 5])

# np.random.shuffle(arr)

# print(arr)  

import numpy as np
X = np.array([[1],[2],[3],[4]])
y = np.array([10,20,30,40])

indices = np.random.permutation(len(X))

X_shuffled = X[indices]
y_shuffled = y[indices]
print(X_shuffled)
print(y_shuffled)