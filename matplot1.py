import matplotlib.pyplot as plt
import pandas1

x_data = pandas1.data['Name '][0:10]
y_data = pandas1.data['Age'][0:10]

plt.bar(x_data,y_data,edgecolor="white")
plt.show()