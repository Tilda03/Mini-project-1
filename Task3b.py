import numpy as np
import matplotlib.pyplot as plt
from Task1 import snapshots

epsilon = 0.1

x = np.linspace(0, 25, 200)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

def concentration(particles, X, Y, epsilon):
    C = np.zeros_like(X)
    
    if len(particles) == 0:
        return C

    for p in particles:
        px, py = p
        
        dist2 = (X - px)**2 + (Y - py)**2
        C += np.exp(-dist2 / (2 * epsilon**2))

    C = C / len(particles)
    return C

fig, axes = plt.subplots(2, 2, figsize=(14, 7), sharex=True, sharey=True)
axes = axes.flatten()

times = [15, 30, 45, 60]

Cs = []
for t in times:
    data = snapshots[t]
    C = concentration(data, X, Y, epsilon)
    Cs.append(C)

vmin = min(C.min() for C in Cs)
vmax = max(C.max() for C in Cs)

levels = np.linspace(vmin, vmax, 50)

# low = white, high = red
cmap = plt.cm.Reds

for i, t in enumerate(times):
    im = axes[i].contourf(
        X, Y, Cs[i],
        levels=levels,
        cmap=cmap,
        vmin=vmin,
        vmax=vmax
    )
    axes[i].set_title(f'Concentration at t = {t} s')
    axes[i].set_xlim(0, 25)
    axes[i].set_ylim(-5, 5)

plt.tight_layout()
plt.show()
