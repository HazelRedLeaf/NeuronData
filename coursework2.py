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