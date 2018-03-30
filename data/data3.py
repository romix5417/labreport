# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

X = [0, 1, 2, 3, 4, 5]
Y = [222, 42, 455, 664, 454, 334]
fig = plt.figure()
plt.bar(X, Y, 0.4, color="green")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("bar chart")


plt.show()
