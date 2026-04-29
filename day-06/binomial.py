# from numpy import random

# x=random.binomial(n=10 , p=0.5 , size=10)

# print(x)

# visualizatiom
# from numpy import random
# import matplotlib.pyplot as plt 
# import seaborn as sns

# sns.displot(random.binomial(n=10 , p=0.5 , size=1000))

# plt.show()


'''The main difference is that normal distribution is continous whereas binomial is discrete,
but if there are enough data points 
it will be quite similar to normal distribution with certain loc and scale.'''


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = {
  "normal": random.normal(loc=50, scale=5, size=1000),
  "binomial": random.binomial(n=100, p=0.5, size=1000)
}

sns.displot(data, kind="kde")

plt.show()