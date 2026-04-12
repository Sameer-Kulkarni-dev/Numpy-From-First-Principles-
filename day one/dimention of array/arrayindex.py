"""array indeing is nothing but accessing array elements by refering to its array index 
    [1,2,3,34,4]
    arr[0]
    output=1
"""

# import numpy as np
# arr=np.array([1,2,3,4,5])
# print(arr[0]) # 1
# print(arr[1]+arr[2]) #5



#--------------------------------------------------------
# accessing element from 2d array 

# dimention= ROW
# INDEX = COLUMN
# import numpy as np

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])    # 0 = FIRTS ROW
#                                                 # 1 = SECOND ROW


# print(arr[1, 4]) # == 10 



#-------------------------------------------------------------------------------------

# ACCESING 3 D ARRAY 

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])  # 6 