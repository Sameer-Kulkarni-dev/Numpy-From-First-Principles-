# from numpy import random

# x=random.randint(100)
# print(x)                
# """"Generate a random integer from 0 to 100:"""


# from numpy import random
# y=random.rand()
# print(y)

# from numpy import random
# x=random.randint(100,size=(100))
# print(x)


'''Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
'''
# from numpy import random

# x = random.randint(100, size=(3, 5))

# print(x)



'''Generate a 1-D array containing 5 random floats:'''

# from numpy import random

# x = random.rand(5)

# print(x)

'''Generate a 2-D array with 3 rows, each row containing 5 random numbers:'''

# from numpy import random

# x = random.rand(3, 5)

# print(x)



from numpy import random

x = random.choice([3, 5, 7, 9])

print(x)

from numpy import random

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)