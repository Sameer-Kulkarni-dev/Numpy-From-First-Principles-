# import numpy as np
# arr=np.array([1,2,3,4,5,5,4,4])

# x=np.where(arr  ==  4)   #Find the indexes where the value is 4:   (array([3, 6, 7]),)
# print(x)

'''The example above will return a tuple: (array([3, 5, 6],)

Which means that the value 4 is present at index 3, 5, and 6.'''


# where idx val is odd

import numpy as np
arr=np.array([1,2,3,4,5])

x=np.where(arr%2==1)
print(x)

import numpy as np
arr=np.array([1,2,3,4,5])

x=np.where(arr%2==0)
print(x)