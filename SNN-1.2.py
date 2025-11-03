# ***********************
# Code for Task 2
# ***********************
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def rasterplot(ax, x, y, x_label, y_label):
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.scatter(x, y, marker='|')
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

if __name__ == '__main__':
    # plt.rcParams['figure.figsize'] = [10, 10]
    # Parameters for Tasks 1–5

    # Timestep
    dt = 0.00001

    # Neuron parameters
    R = 95e6  # resistance in ohms
    tau_m = 3e-3  # Membrane constant in seconds
    u_rest = -65e-3  # resting membrane potential in V
    u_reset = -65e-3  # reset potential in V
    u_thres = -50e-3  # threshold potential in V

    # Code for Task 1

    # Input current from synapses
    I_syn = 50e-12  # A

    # Neuron identifier, only one neuron in this simulation
    n_id = 0

    # Placeholders for u(t), used for plotting
    t_i = []
    u_i = []

    # Placeholders for list of spike times and neuron ID's
    t_spike = []
    n_spike = []


I_syn = 50  # pA
# Re-initializing the spiking detection setup
found_spike = False  # Reset the flag for detecting spikes
spiking_current = None  # Reset the spiking current value
print("Start")
# Corrected loop to find the spiking current
for I_syn in range(50, 1000, 2):  # from 50 pA up to 1000 pA
    t = 0  # Reset time for each I_syn value
    u = u_rest  # Reset membrane potential for each simulation

    while t <= 1:
        # Euler forward method for du/dt
        du_dt = (-(u - u_rest) + R * (I_syn * 1e-12)) / tau_m
        u += du_dt * dt


        if u >= u_thres:  # Check for spike
            spiking_current = I_syn  # Store the spiking current value
            found_spike = True  # Set the flag to true
            break  # Exit the inner loop if a spike is found

        t += dt  # Increment time

    if found_spike:
        print(f"Found spike at: {spiking_current}pA")

        break  # Exit the outer loop if a spike has been found
else:
    print("No spiking current found within the tested range.")
# Plotting
