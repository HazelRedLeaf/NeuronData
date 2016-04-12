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


############################################################
# QUESTION 1                                               #
############################################################
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

for n4 in neuron[3]:
	for i in range(len(time)):
		if n4 <= time[i]:
			newX4.append(x[i])
			newY4.append(y[i])
			break

# plot the results
plt.figure(1)
plt.title("Neuron 1")
plt.xlabel("X axis of the maze")
plt.ylabel("Y axis of the maze")
plt.scatter(newX1, newY1, color = 'b')
plt.show()
plt.figure(2)
plt.title("Neuron 2")
plt.xlabel("X axis of the maze")
plt.ylabel("Y axis of the maze")
plt.scatter(newX2, newY2, color = 'c')
plt.show()
plt.figure(3)
plt.title("Neuron 3")
plt.xlabel("X axis of the maze")
plt.ylabel("Y axis of the maze")
plt.scatter(newX3, newY3, color = 'g')
plt.show()
plt.figure(4)
plt.title("Neuron 4")
plt.xlabel("X axis of the maze")
plt.ylabel("Y axis of the maze")
plt.scatter(newX4, newY4, color = 'r')
plt.show()


############################################################
# QUESTION 2                                               #
############################################################

bins = 200
buckets1 = [0] * bins
buckets2 = [0] * bins
buckets3 = [0] * bins
buckets4 = [0] * bins

# neuron 1
deltaT1 = (neuron[0][-1] - neuron[0][0]) / (bins/2) + 1

for n1 in neuron[0]:
	for n2 in neuron[0]:
		bin = (n2 - n1) / deltaT1
		buckets1[bin + bins/2] += 1

delta1 = []

for d in range(bins):
	delta1.append(deltaT1*(d - bins/2))

# neuron 2
deltaT2 = (neuron[1][-1] - neuron[1][0]) / (bins/2) + 1

for n1 in neuron[1]:
	for n2 in neuron[1]:
		bin = (n2 - n1) / deltaT2
		buckets2[bin + bins/2] += 1

delta2 = []

for d in range(bins):
	delta2.append(deltaT2*(d- bins/2))

# neuron 3
deltaT3 = (neuron[2][-1] - neuron[2][0]) / (bins/2) + 1

for n1 in neuron[2]:
	for n2 in neuron[2]:
		bin = (n2 - n1) / deltaT3
		buckets3[bin + bins/2] += 1

delta3 = []

for d in range(bins):
	delta3.append(deltaT3*(d- bins/2))

# neuron 4
deltaT4 = (neuron[3][-1] - neuron[3][0]) / (bins/2) + 1

for n1 in neuron[3]:
	for n2 in neuron[3]:
		bin = (n2 - n1) / deltaT4
		buckets4[bin + bins/2] += 1

delta4 = []

for d in range(bins):
	delta4.append(deltaT4*(d- bins/2))

# plot the results
plt.figure(5)
plt.bar(delta1, buckets1, deltaT1)
#plt.show()
plt.figure(6)
plt.bar(delta2, buckets2, deltaT2)
#plt.show()
plt.figure(7)
plt.bar(delta3, buckets3, deltaT3)
#plt.show()
plt.figure(8)
plt.bar(delta4, buckets4, deltaT4)
#plt.show()

############################################################
# QUESTION 3                                               #
############################################################

bins = 200
buckets12 = [0] * bins
buckets13 = [0] * bins
buckets14 = [0] * bins
buckets23 = [0] * bins
buckets24 = [0] * bins
buckets34 = [0] * bins

# neurons 1 and 2
deltaT12 = (max(neuron[0][-1],neuron[1][-1]) - min(neuron[0][0],neuron[1][0])) / (bins/2) + 1

for n1 in neuron[0]:
	for n2 in neuron[1]:
		bin = (n2 - n1) / deltaT12
		buckets12[bin + bins/2] += 1

delta12 = []
for d in range(bins):
	delta12.append(deltaT12*(d - bins/2))

# neurons 1 and 3
deltaT13 = (max(neuron[0][-1],neuron[2][-1]) - min(neuron[0][0],neuron[2][0])) / (bins/2) + 1

for n1 in neuron[0]:
	for n3 in neuron[2]:
		bin = (n3 - n1) / deltaT13
		buckets13[bin + bins/2] += 1

delta13 = []
for d in range(bins):
	delta13.append(deltaT13*(d - bins/2))

# neurons 1 and 4
deltaT14 = (max(neuron[0][-1],neuron[3][-1]) - min(neuron[0][0],neuron[3][0])) / (bins/2) + 1

for n1 in neuron[0]:
	for n4 in neuron[3]:
		bin = (n4 - n1) / deltaT14
		buckets14[bin + bins/2] += 1

delta14 = []
for d in range(bins):
	delta14.append(deltaT14*(d - bins/2))

# neurons 2 and 3
deltaT23 = (max(neuron[1][-1],neuron[2][-1]) - min(neuron[1][0],neuron[2][0])) / (bins/2) + 1

for n2 in neuron[1]:
	for n3 in neuron[2]:
		bin = (n2 - n3) / deltaT23
		buckets23[bin + bins/2] += 1

delta23 = []
for d in range(bins):
	delta23.append(deltaT23*(d - bins/2))

# neurons 2 and 4
deltaT24 = (max(neuron[1][-1],neuron[3][-1]) - min(neuron[1][0],neuron[3][0])) / (bins/2) + 1

for n2 in neuron[1]:
	for n4 in neuron[3]:
		bin = (n4 - n2) / deltaT24
		buckets24[bin + bins/2] += 1

delta24 = []
for d in range(bins):
	delta24.append(deltaT24*(d - bins/2))

# neurons 3 and 4
deltaT34 = (max(neuron[2][-1],neuron[3][-1]) - min(neuron[2][0],neuron[3][0])) / (bins/2) + 1

for n3 in neuron[2]:
	for n4 in neuron[3]:
		bin = (n4 - n3) / deltaT34
		buckets34[bin + bins/2] += 1

delta34 = []
for d in range(bins):
	delta34.append(deltaT34*(d - bins/2))

plt.figure(9)
plt.bar(delta12, buckets12, deltaT12)
plt.figure(10)
plt.bar(delta13, buckets13, deltaT13)
plt.figure(11)
plt.bar(delta14, buckets14, deltaT14)
plt.figure(12)
plt.bar(delta23, buckets23, deltaT23)
plt.figure(13)
plt.bar(delta24, buckets24, deltaT24)
plt.figure(14)
plt.bar(delta34, buckets34, deltaT34)
plt.show()

############################################################
# QUESTION 4                                               #
############################################################
