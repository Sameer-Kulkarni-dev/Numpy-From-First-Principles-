

# # """Feature	copy()	                        view()
# #     Memory	New copy	                       Shared
# #     Speed	   Slower	                    Faster
# # Data changes	Independent                	Linked

# # Use case	When you need a safe, independent array  ==copy()
# # When you want performance and can allow shared data == view()"""

# # import numpy as np

# # arr = np.array([1, 2, 3])
# # arr_copy = arr.copy()  # Creates a deep copy

# # arr_copy[0] = 99

# # print("Original:", arr)     # [1 2 3]
# # print("Copy:", arr_copy)    # [99  2  3]
# # #np.shares_memory(arr, arr_view)  # True
# # np.shares_memory(arr, arr_copy)  # False



# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# arr[0] = 42

# print(arr)
# print(x)     # shallow copy  The view SHOULD be affected by the changes made to the original arr



import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)   # NONE 
print(y.base)   # [1,2,3, 4,5]


"""The copy returns None.
The view returns the original array."""