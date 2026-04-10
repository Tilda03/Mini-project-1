import numpy as np
import matplotlib.pyplot as plt

# Parameters
D = 0.02
u = np.array([0.3, 0.0])
N = 2000
h = 0.1
snapshots = {15: None, 30: None, 45: None, 60: None}

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
fig, axes = plt.subplots(2, 2, figsize=(14, 6))
axes = axes.flatten()

for i in range(N):
    snapshots = {15: None, 30: None, 45: None, 60: None}  # reset for each particle
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
plt.show()