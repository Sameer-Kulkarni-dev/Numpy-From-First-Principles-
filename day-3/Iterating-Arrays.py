# '''Iterating Arrays
# Iterating means going through elements one by one.

# As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.

# If we iterate on a 1-D array it will go through each element one by one.'''

# import numpy as np

# arr=np.array([1,2,3,4,5])

# for x in arr:
    
#     print(x)



# '''Iterating 2-D Arrays
# In a 2-D array it will go through all the rows.'''

# # import numpy as  np

# # arr=np.array([[1,2,3],[4,5,6]])

# # for x in arr:
# #     for y in x:
# #         print(y)


# '''if we iterate on a n-D array it will go through n-1th dimension one by one.'''

# # import numpy as np

# # arr = np.array([[1, 2, 3], [4, 5, 6]])

# # for x in arr:
# #   for y in x:
# #     print(y)

# # import numpy as np

# # arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# # for x in arr:
# #     for y in x:
# #         for z in y:
# #             print(z)



# """ nditer()"""

# # import numpy as np

# # arr=np.array([[[1,2,3],[4,5,6],[3,4,5],[7,6,8]]])

# # for i in np.nditer(arr):
# #     print(i)



# import numpy as np

# arr=np.array([1,2,"sam"], dtype=object)

# for x in arr:
#     print(x,type(x))  
# """
# 1
# 2
# 3
# 4
# 5

# 1    <class 'int'>
# 2   <class 'int'>
# sam     <class 'str'> """



# import numpy as np

# arr=np.array(["a","b","c"])

# for x in np.nditer(arr):
#     print(x)

""""Iterating with Different Step Size"""

"""🔹 Core Idea

Instead of visiting every element, you skip elements using slicing.

👉 This is NOT handled by iteration itself —
It is controlled by array slicing before iteration"""

# import numpy as np

# arr = np.array([10, 20, 30, 40, 50, 60])

# #for x in arr[::2]:   # step = 2
# for x in arr[::-1]: # negative iteration Reverse Iteration (Negative Step)

#     """ print negative array """
#     print(x)






"""2D Array Step Iteration"""

# import numpy as np

# arr=np.array([[1,2,3],[4,5,6],[7,8,9]])

# for x in arr[::2]:
#     print(x)




"""🧠 1. Core Idea (Understand This First)

In NumPy slicing:

arr[rows, columns]

👉 So when you write:

arr[:, ::2]
: → take all rows
::2 → take every 2nd column"""


# import numpy as np

# arr = np.array([[1,2,3,4],
#                 [5,6,7,8],
#                 [9,10,11,12]])

# for row in arr[:, ::2]:
#     print(row)


# reverse the matrix

# import numpy as np

# arr = np.array([[1,2,3,4],
#                 [5,6,7,8],
#                 [9,10,11,12]])

# for row in arr[:, ::-1]:
#     print(row)


