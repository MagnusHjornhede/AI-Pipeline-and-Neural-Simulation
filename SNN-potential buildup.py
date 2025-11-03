import numpy as np
import matplotlib.pyplot as plt

# Initialization
R = 95e6  # Resistance in ohms
tau_m = 0.003  # Membrane time constant in seconds
u_rest = -65e-3  # Resting membrane potential in volts
u_reset = -65e-3  # Reset potential in volts
u_thres = -50e-3  # Threshold potential in volts
dt = 0.00001  # Time step in seconds


# Function to simulate neuron for a given I_syn
def simulate_neuron(I_syn):
    u = u_rest  # Start at resting potential
    t_i = np.arange(0, 1, dt)  # Time array from 0 to 1 second
    u_i = []  # To store membrane potential over time

    for t in t_i:
        # Euler method to update membrane potential
        du_dt = (-(u - u_rest) + R * I_syn) / tau_m
        u += du_dt * dt
        u_i.append(u)  # Store current value of u
        # Reset if threshold is reached
        if u >= u_thres:
            u = u_reset
    return t_i, u_i


if __name__ == '__main__':

    # Example usage for a single I_syn value
    I_syn_example = 159e-12  # 50 pA
    t_i, u_i = simulate_neuron(I_syn_example)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(t_i, u_i, label=f'Membrane Potential (I_syn = {I_syn_example * 1e12:.0f} pA)')
    plt.title('Membrane Potential Buildup Over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Membrane Potential (V)')
    plt.axhline(y=u_thres, color='r', linestyle='--', label='Threshold Potential')
    plt.grid(True)
    plt.legend()
    plt.show()
