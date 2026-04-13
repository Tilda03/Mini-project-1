import numpy as np 
import matplotlib.pyplot as plt

# Parameters
D = 0.02
u = np.array([0.3, 0.0])

Q = 100              
h = 0.1             
T = 60

snapshots = {15: [], 30: [], 45: [], 60: []}

xmin, xmax = 0, 25
ymin, ymax = -5, 5

source = np.array([0.0, 0.0])

# number of new particles per step
new_particles = int(Q * h)

# Euler–Maruyama step
def step(particles, h, D, u):
    new_particles_list = []

    for p in particles:
        Z = np.random.randn(2)
        p = p + u * h + np.sqrt(2 * D * h) * Z

        # keep inside domain
        if xmin <= p[0] <= xmax and ymin <= p[1] <= ymax:
            new_particles_list.append(p)

    return new_particles_list

# Simulation
particles = []

t = 0
while t <= T:

    # 1. Add new particles at source
    for _ in range(new_particles):
        particles.append(source.copy())

    # 2. Move all particles
    particles = step(particles, h, D, u)

    # 3. Save snapshots
    if int(t) in snapshots:
        snapshots[int(t)] = np.array(particles)

    t = round(t + h, 1)


# Plot
fig, axes = plt.subplots(2, 2, figsize=(14, 7))
axes = axes.flatten()

times = [15, 30, 45, 60]

for i, t in enumerate(times):
    data = snapshots[t]

    if len(data) > 0:
        axes[i].scatter(data[:, 0], data[:, 1], s=1, color='royalblue')

    axes[i].set_title(f't = {t} s')
    axes[i].set_xlim(xmin, xmax)
    axes[i].set_ylim(ymin, ymax)
    axes[i].set_xlabel('x')
    axes[i].set_ylabel('y')

plt.suptitle('Task 3: Continuous source particle simulation')
plt.tight_layout()
plt.show()


