# # import numpy as np

# # #arr=np.array([1,2,3,4,5])

# # arr=np.array([12,43,65,87,56,98])

# # #print(arr[1:5])   #[43 65 87 56]

# # print([arr[:6:3]])  #[array([12, 87])]
 


# # import numpy as np

# # arr = np.array([1, 2, 3, 4, 5, 6, 7])

# # print(arr[4:])  # [5 6 7]


# import numpy as sam

# arr=sam.array([1,2,3,4,5])

# print(arr[:4])  # 1,2,3,4

'''STEP
Use the step value to determine the step of the slicing:'''

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[1:5:2])



# '''SLICING 2-D ARRAY '''

# import numpy as np

# arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])

# print(arr[0,1:4])  


# """here 0/1 represents array 1 or array 0 
#     and regular slicing is continued [0,1:4]"""


# import numpy as np

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(arr[0:3,3])  #[4 9]


"""in this above example slicing works as first select rows to be excluded , and 
give the INDEX  of element to be print if i want to print (4,9) >>> 
 write the code as [0:3,3]"""


import numpy as np

arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(arr[0:2,1:4])