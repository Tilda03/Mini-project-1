'''import numpy as np
import matplotlib.pyplot as plt

# Parameters
D = 0.02
u = np.array([0.3, 0.0])
N = 2000
h = 0.1
snapshots = {15: [], 30: [], 45: [], 60: []}

X0 = np.array([0.0, 0.0])

def euler_maruyama(X0, h, snapshots, D, u):
   
    X = X0
    k = 0
    while k <= max(snapshots):
        Z = np.array([np.random.normal(0, 1), np.random.normal(0, 1)])
        X = X + u * h + np.sqrt(2 * D * h) * Z
        k = round(k + h, 1)
        if k in snapshots:
            snapshots[k] = X

    return snapshots

# Setup 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 7))
axes = axes.flatten()

for i in range(N):
    result = euler_maruyama(X0, h, snapshots, D, u)       # store return value separately

    for j, t in enumerate(result):
        pos = result[t]
        axes[j].scatter(pos[0], pos[1], s=2, color='royalblue')

for j, t in enumerate(snapshots):
    axes[j].set_title(f't = {t} s')
    axes[j].set_xlim(0, 25)
    axes[j].set_ylim(-5, 5)
    axes[j].set_xlabel('x')
    axes[j].set_ylabel('y')

plt.suptitle('Particle cloud at different time levels')
plt.tight_layout()
plt.show()'''

import numpy as np
import matplotlib.pyplot as plt

# Parameters
D = 0.02
u = np.array([0.3, 0.0])
N = 2000
h = 0.1
times = [15, 30, 45, 60]

X0 = np.array([0.0, 0.0])

def euler_maruyama(X0, h, times, D, u):
    X = X0.copy()
    k = 0
    result = {t: None for t in times}

    while k <= max(times):
        Z = np.random.normal(0, 1, size=2)
        X = X + u * h + np.sqrt(2 * D * h) * Z
        k = round(k + h, 1)

        if k in result:
            result[k] = X.copy()

    return result


# Store all particles at each time
snapshots = {t: [] for t in times}

for i in range(N):
    result = euler_maruyama(X0, h, times, D, u)

    for t in times:
        snapshots[t].append(result[t])

# Convert lists to NumPy arrays (important for fast plotting & later use)
for t in times:
    snapshots[t] = np.array(snapshots[t])


# Plotting
fig, axes = plt.subplots(2, 2, figsize=(14, 7))
axes = axes.flatten()

for i, t in enumerate(times):
    data = snapshots[t]

    axes[i].scatter(data[:, 0], data[:, 1], s=2, color='royalblue')

    axes[i].set_title(f't = {t} s')
    axes[i].set_xlim(0, 25)
    axes[i].set_ylim(-5, 5)
    axes[i].set_xlabel('x')
    axes[i].set_ylabel('y')

plt.suptitle('Particle cloud at different time levels')
plt.tight_layout()
plt.show()