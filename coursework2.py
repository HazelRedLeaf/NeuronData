import math
import numpy as np
import random
import matplotlib.pyplot as plt

# for loading neuron 1 - 4 and time
neuron = []
f = open("neuron1.csv")
neuron += [map(lambda x: int(x.strip()), f.readlines())]
f = open("neuron2.csv")
neuron += [map(lambda x: int(x.strip()), f.readlines())]
f = open("neuron3.csv")
neuron += [map(lambda x: int(x.strip()), f.readlines())]
f = open("neuron4.csv")
neuron += [map(lambda x: int(x.strip()), f.readlines())]

# for loading x
f = open("x.csv")
x = map(lambda x: float(x.strip()), f.readlines())

# for loading y
f = open("y.csv")
y = map(lambda x: float(x.strip()), f.readlines())

# for loading time
f = open("time.csv")
time = map(lambda x: int(x.strip()), f.readlines())

# neuron 1
newX1 = []
newY1 = []

for n1 in neuron[0]:
	for i in range(len(time)):
		if n1 <= time[i]:
			newX1.append(x[i])
			newY1.append(y[i])
			break

# neuron 2
newX2 = []
newY2 = []

for n2 in neuron[1]:
	for i in range(len(time)):
		if n2 <= time[i]:
			newX2.append(x[i])
			newY2.append(y[i])
			break

# neuron 3
newX3 = []
newY3 = []

for n3 in neuron[2]:
	for i in range(len(time)):
		if n3 <= time[i]:
			newX3.append(x[i])
			newY3.append(y[i])
			break

# neuron 4
newX4 = []
newY4 = []

for n4 in neuron[1]:
	for i in range(len(time)):
		if n4 <= time[i]:
			newX4.append(x[i])
			newY4.append(y[i])
			break

# plot the results
plt.figure(1)
plt.scatter(newX1, newY1, color = 'b')
plt.show()
plt.figure(2)
plt.scatter(newX2, newY2, color = 'c')
plt.show()
plt.figure(3)
plt.scatter(newX3, newY3, color = 'g')
plt.show()
plt.figure(4)
plt.scatter(newX4, newY4, color = 'r')
plt.show()