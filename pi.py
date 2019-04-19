"""
This program estimates value of pie using Monte Carlo simulation.
Consider a quadrant inscribed in a unit square, the ratio their respective area will be pi/4.
To simulate this:
1. Create a uniform distribution of points in the unit sqaure.
2. Count the number of points within circle with radius as 1 unit.
3. Divide the number of points in step 2 by total number of points, resulting value when multiplied by 4 gives approx value of pi.
"""
import numpy as np
import matplotlib.pyplot as plt

#number of points
n_points = 3000

#uniform distribution for x, y points
x = np.random.rand(n_points)
y = np.random.rand(n_points)

#initiate counter for points inside circle of radius 1.
inside = 0

for n in range(len(x)):
    a = np.random.choice(x)
    b = np.random.choice(y)
    radius = np.sqrt(a**2+ b**2)            #calculating radius
    print(n)
    if radius <=1:
        inside+=1                           #increase count for inside point
        plt.scatter(a, b, c="red")          #add point to the plot
    else:
        plt.scatter(a, b, c='blue')         #addd point to the plot, outside circle

plt.show()

pi = inside/n_points
print("Estimated value of pi is", pi*4)
