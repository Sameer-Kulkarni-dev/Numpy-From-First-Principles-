#
'''Note: We also have the method split() available but it will not adjust the elements 
when elements are less in source array for splitting like in example above, 
array_split() worked properly but split() would fail.'''


# import numpy as np
# arr=np.array([1,2,3,4,5,6])

# newarr=np.split(arr,4)
# print(newarr)
'''in split
    raise ValueError(
        'array split does not result in an equal division') from None
ValueError: array split does not result in an equal division'''


# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6])

# newarr = np.array_split(arr, 3)

# print(newarr[0])
# print(newarr[1])
# print(newarr[2])    

"""The return value of the array_split() method is a list containing each
 of the split as an array.

[1 2]
[3 4]
[5 6]

If you split an array into 3 arrays, you can access them from 
the result just like any array element:"""








# splitting the 2-d array 

# import numpy as np

# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

# newarr = np.array_split(arr, 3)

# print(newarr)
# print(newarr[0])


# import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

# newarr = np.array_split(arr, 3)

# print(newarr)



'''Split the 2-D array into three 2-D arrays along columns.  axis = 1'''
# import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

# newarr = np.array_split(arr, 3, axis=1) # slipt along columns


# #print(newarr)
# print(newarr[0])



import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)  # hsplit()  along column split
print(newarr[0])

''';Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().'''