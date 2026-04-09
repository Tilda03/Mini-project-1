import numpy as np
import matplotlib.pyplot as plt

# Parameters
D = 0.02
u = np.array([0.3, 0.0])
N = 2000
h = 0.1
T = 60.0
plot_times = [15, 30, 45, 60]

def euler_maruyama(end_time, time_step, N, D):

    # Each particle has a position [x, y]
    # We store all particles in a list of N positions
    # At the start, every particle is at the origin [0, 0]
    positions = []
    for i in range(N):
        positions.append(np.array([0.0, 0.0]))

    # We save a snapshot of all positions at each time step
    # so we can look back at any moment in time
    history = [list(positions)]

    k = 0
    while k * time_step <= end_time:

        # Create an empty list for the updated positions
        new_positions = []

        # Loop over each particle and update its position
        for i in range(N):

            # Draw a random kick in x and y direction
            Z = np.array([np.random.normal(0, 1), np.random.normal(0, 1)])

            # Euler-Maruyama update:
            # new position = old position + advection + diffusion
            advection = u * time_step
            diffusion = np.sqrt(2 * D * time_step) * Z
            new_pos = positions[i] + advection + diffusion

            new_positions.append(new_pos)

        # The new positions become the current positions
        positions = new_positions

        # Save a snapshot
        history.append(list(positions))

        k += 1

    return history


history = euler_maruyama(T, h, N, D)

# Plot
fig, axes = plt.subplots(2, 2, figsize=(14, 6))
axes = axes.flatten()

for i, t in enumerate(plot_times):
    step_idx = int(t / h)

    # Extract x and y from the snapshot for plotting
    snapshot = history[step_idx]   # a list of N positions, each being [x, y]
    x_values = [pos[0] for pos in snapshot]
    y_values = [pos[1] for pos in snapshot]

    axes[i].scatter(x_values, y_values, s=2, alpha=0.5, color='steelblue')
    axes[i].set_title(f't = {t} s')
    axes[i].set_xlim(0, 25)
    axes[i].set_ylim(-5, 5)
    axes[i].set_xlabel('x')
    axes[i].set_ylabel('y')

plt.suptitle('Particle cloud at different time levels (Task 1)', fontsize=13)
plt.tight_layout()
plt.show()