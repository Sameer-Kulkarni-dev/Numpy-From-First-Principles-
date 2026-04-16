# # import numpy as np

# # arr = np.array([3, 2, 0, 1])

# # print(np.sort(arr))

# # import numpy as np

# # arr = np.array(['banana', 'cherry', 'apple'])

# # print(np.sort(arr))


# # import numpy as np

# # arr = np.array([True, False, True])

# # print(np.sort(arr))


# # import numpy as np

# # arr = np.array([[3, 2, 4], [5, 0, 1]])

# # print(np.sort(arr))


# import numpy as np

# arr = np.array([41, 42, 43, 44])

# filter_arr = arr > 42

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)    #[False False  True  True]

#                     #[43 44]


# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# filter_arr = arr % 2 == 0

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr) 



import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])

filt_arr= arr%2 == 0

newarr=arr[filt_arr]

print(filt_arr)
print(newarr)
