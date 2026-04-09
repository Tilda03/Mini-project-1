import numpy as np
from Task1 import euler_maruyama

D = 0.02
u = np.array([0.3, 0.0])
N = 2000
h = 0.1
T = 60.0
plot_times = [15, 30, 45, 60]
epsilon = 0.1

# creating the grid
x = np.linspace(0, 25, 200)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y) #?

def concentration(particles, X, Y, epsilon):
    N = len(particles)
    C = np.zeros_like(X)

    for p in particles:
        px, py = p

