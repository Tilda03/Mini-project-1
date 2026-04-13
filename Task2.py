import numpy as np
import matplotlib.pyplot as plt
from Task1 import snapshots

# Grid
x = np.linspace(0, 25, 200)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

epsilon = 0.3
times = [15, 30, 45, 60]

def concentration(particles, X, Y, epsilon):
    if particles is None or len(particles) == 0:
        return np.zeros_like(X)

    particles = np.array(particles)

    px = particles[:, 0][:, None, None]
    py = particles[:, 1][:, None, None]

    dist2 = (X - px)**2 + (Y - py)**2

    C = np.exp(-dist2 / (2 * epsilon**2)).sum(axis=0)
    C /= len(particles) 

    return C


# Compute concentration fields first (important for consistent color scale)
C_fields = []
for t in times:
    C = concentration(snapshots[t], X, Y, epsilon)
    C_fields.append(C)

# Find global min/max for consistent color scaling
vmin = min(C.min() for C in C_fields)
vmax = max(C.max() for C in C_fields)


# Plotting
fig, axes = plt.subplots(2, 2, figsize=(14, 7), sharex=True, sharey=True)
axes = axes.flatten()

for i, t in enumerate(times):
    C = C_fields[i]

    im = axes[i].contourf(
        X, Y, C,
        levels=50,
        cmap='Reds',     # white -> red
        vmin=vmin,
        vmax=vmax
    )

    axes[i].set_title(f'Concentration at t = {t} s')
    axes[i].set_xlim(0, 25)
    axes[i].set_ylim(-5, 5)
    axes[i].set_xlabel('x')
    axes[i].set_ylabel('y')

plt.suptitle('Concentration field evolution')
plt.tight_layout()
plt.show()