from matplotlib import pyplot
import numpy as np

# data for histogram
data0 = [2,2,0,3,5,5]
# data for line graph
data1 = np.random.randint(10,size=(10,2))
# plot and show histogram
gr = pyplot.hist(data0)
pyplot.show()
# plot and show line graph
pyplot.subplot()
pyplot.plot(data1)
pyplot.show()

# simple math
x = [0,10,20,30,40,50,60,70,80,90,100]
x = np.asarray(x)
y = 4 + 2 * np.sin(x * 2)

pyplot.subplot()
pyplot.plot(x,y)
pyplot.show()
