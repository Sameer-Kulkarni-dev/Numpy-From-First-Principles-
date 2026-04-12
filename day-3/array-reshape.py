# # # reshaping from 1d to 2 d array 

# # import numpy as np

# # arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15,17,18,19,20,21,22,23,24,25])

# # new_arr=arr.reshape(5,5)  # 5*5=25 25 elements should be present in 1d array

# # print(new_arr)


# '''1-d to 3-d arrray '''
# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# newarr = arr.reshape(2, 3, 2)

# print(newarr)


'''Unknown Dimension
You are allowed to have one "unknown" dimension.

Meaning that you do not have to specify an exact number for one of the dimensions in the
 reshape method.

Pass -1 as the value, and NumPy will calculate this number for you.

Example
Convert 1D array with 8 elements to 3D array with 2x2 elements:'''

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# newarr = arr.reshape(2, 2, -1)

# print(newarr)



'''Flattening the arrays
Flattening array means converting a multidimensional array into a 1D array.

We can use reshape(-1) to do this.'''

import numpy as np

arr=np.array([[1,2,3,4],[1,2,3,4]])

new_arr=arr.reshape(-1)   # back t0 1d  array 
print(new_arr)

