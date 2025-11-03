import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


# Set default figure size


# Function that is used to plot spike times
def rasterplot(ax, x, y, x_label, y_label):
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.scatter(x, y, marker='|')
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))


if __name__ == '__main__':
    plt.rcParams['figure.figsize'] = [10, 10]
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

    # Simulate one second of time
    t = 0
    u = u_rest
    while t <= 1:

        # Euler forward step

        # u_next = u + dt * du_dt
        du_dt = (-(u - u_rest) + R * (I_syn)) / tau_m
        u += du_dt * dt
        # u += (dt / tau_m) * (-(u - u_rest) + R * I_syn)   # ref
        u_i.append(u)  # Store u(t)

        # Spike condition
        # print(u)
        # print(u_thres)
        if u >= u_thres:  # Added threshold
            t_spike.append(t)  # spike time
            n_spike.append(n_id)  # neuron ID
            u = u_reset  # Added reset
            print("SPIKE")
        # Timestep completed
        t_i.append(t)
        t += dt

    # Plot u(t)
    fig, ax = plt.subplots()
    ax.plot(t_i, u_i)
    ax.set(xlabel='Time [s]', ylabel='Membrane potential u(t)')
    ax.grid()
    plt.show()
    print("Testing spike training...")
    # Parameters
    u_rest = -65e-3  # Resting membrane potential in V
    R = 95e6  # Membrane resistance in ohms
    I_syn = 50 * 1e-12  # Synaptic input current in pA

    # Convert I_syn from pA to A for calculation
    # I_syn_A = I_syn * 1e-12

    u_steady_state = u_rest + (R * int(I_syn * 1e3))  # Convert A to mV by multiplying by 1e3

    print(f"Expected steady-state membrane potential: {u_steady_state} mV")
    # Check final value for convergence
    print(f"Final membrane potential: {u} mV")


    # ***********************
    # Code for Task 2
    # ***********************

    I_syn = 50  # pA
    # Re-initializing the spiking detection setup
    found_spike = False  # Reset the flag for detecting spikes
    spiking_current = None  # Reset the spiking current value
    print("Start")
    # Corrected loop to find the spiking current
    for I_syn in range(50, 1000, 2):  # Search from 50 pA up to 1000 pA
        t = 0  # Reset time for each I_syn value
        u = u_rest  # Reset membrane potential for each simulation
        print(I_syn)
        while t <= 1:
            # Euler forward method for du/dt
            du_dt = (-(u - u_rest) + R * (I_syn * 1e-12)) / tau_m
            u += du_dt * dt

            if u >= u_thres:  # Check for spike
                spiking_current = I_syn  # Store the spiking current value
                found_spike = True  # Set the flag to true
                #break  # Exit the inner loop if a spike is found

            t += dt  # Increment time

        if found_spike:
            print("Found spike")
            #break  # Exit the outer loop if a spike has been found

    # Checking if spiking_current was found before proceeding with plotting
    if spiking_current is not None:
        # Reset simulation variables for plotting
        t = 0
        u = u_rest
        t_i = []  # Time points for plotting
        u_i = []  # Membrane potentials for plotting

        # Simulation loop for plotting at the spiking current
        while t <= 1:
            du_dt = (-(u - u_rest) + R * (spiking_current * 1e-12)) / tau_m
            u += du_dt * dt

            # Record for plotting
            u_i.append(u)
            t_i.append(t)

            # Reset u to u_reset if it crosses threshold, to simulate spike occurrence
            if u >= u_thres:
                u = u_reset

            t += dt  # Increment time

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.plot(t_i, u_i, label=f'Membrane Potential at I_syn = {spiking_current} pA')
        plt.title('Membrane Potential over Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Membrane Potential (mV)')
        plt.grid(True)
        plt.legend()
        plt.show()

        print(spiking_current)
    else:
        print("No spiking current found within the tested range.")
