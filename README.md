# AI-Pipeline-and-Neural-Simulation

> A hands-on exploration of how artificial intelligence pipelines and biologically inspired neuron models can coexist in the same experimental space.

---

## Overview

This repository combines **machine learning data processing** and **spiking neural dynamics** into one coherent simulation pipeline.

The idea is simple but powerful:  
to bridge classical feature-based datasets with biologically plausible models of computation —  
from **gesture data normalization** to **neuron membrane potential simulation**.

---

## Core Concepts

### 1. **Data Analysis Pipeline**
- Loads gesture datasets (`train-final.csv`, `test-final.csv`)  
- Handles missing values with automatic mean-imputation  
- Performs normalization (`MinMaxScaler` or `StandardScaler`)  
- Generates boxplots for 4 feature groups:
  - Positions (1–60)
  - Cosine Angles (61–120)
  - Mean Positions (121–180)
  - Standard Deviations (181–240)

This step provides the **feature-space anatomy** of the gesture data — before any neural encoding occurs.

---

### 2. **Spiking Neuron Simulation**

Implements a **Leaky Integrate-and-Fire (LIF)** neuron model:

\[
\tau_m \frac{du}{dt} = -(u - u_{rest}) + R \cdot I_{syn}
\]

with parameters:

| Symbol | Meaning | Typical Value |
|:-------|:---------|:--------------|
| R | Membrane resistance | 95 MΩ |
| τₘ | Membrane time constant | 3 ms |
| u_rest | Resting potential | -65 mV |
| u_reset | Reset potential | -65 mV |
| u_thres | Spike threshold | -50 mV |

Scripts explore:
- Membrane potential evolution over time  
- Minimum synaptic current required to generate spikes  
- Potential buildup and reset dynamics  

All visualized with Matplotlib for educational clarity.

---

### 3. **Example Outputs**

- Data Exploration

  - Boxplots showing feature normalization across gesture categories.
  - Heatmaps of missing values.

- Neuron Simulation

  - Time-domain plots of voltage trajectories and spike reset behavior.
  - Spiking current thresholds between 150–170 pA (depending on parameters).

---


### 4. **Future Directions**

- Integrate multi-neuron SNN simulation
- Add synaptic plasticity models (e.g., STDP)
- Extend pipeline for real-time sensory encoding
- Experiment with hybrid AI–SNN architectures

---

Author: Magnus Hjornhede
Göteborg, Sweden
