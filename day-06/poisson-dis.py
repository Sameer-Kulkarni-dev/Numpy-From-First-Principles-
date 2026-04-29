# from numpy import random

# x=random.poisson(lam=2 , size=2)



# print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.poisson(lam=2, size=1000))

plt.show()