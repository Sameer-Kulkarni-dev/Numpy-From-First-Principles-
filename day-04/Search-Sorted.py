'''There is a method called searchsorted() which performs a binary search in the array,
 and returns the index where the specified value would be inserted to maintain the search order.

The searchsorted() method is assumed to be used on sorted arrays.'''


# import numpy as np

# arr = np.array([6, 7, 8, 9])

# x = np.searchsorted(arr, 7)

# print(x)


# import numpy as np

# arr=np.array([1,2,3,4,5])

# x=np.searchsorted(arr,3, side='right')

# print(x)

import numpy as np
arr = np.array([10, 20, 30, 40])

values = [5, 25, 50]

pos = np.searchsorted(arr, values)
print(pos)