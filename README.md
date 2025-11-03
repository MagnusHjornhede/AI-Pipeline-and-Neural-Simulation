# AI-Pipeline-and-Neural-Simulation

---

## Overview

This repository about **machine learning preprocessing** and **biophysical neuron simulation**  
into a single experimental framework — from *gesture data normalization* to *membrane potential dynamics*.

<p align="center">
  <img src="plots/pipeline_overview.png" alt="Pipeline Overview Diagram" width="750"/>
</p>

---

## Core Concepts

### 1. **Data Analysis Pipeline**

- Loads gesture datasets (`train-final.csv`, `test-final.csv`)  
- Handles missing values automatically  
- Performs normalization (`MinMaxScaler` / `StandardScaler`)  
- Generates diagnostic boxplots for 4 feature groups:
  - Positions (1–60)
  - Cosine Angles (61–120)
  - Mean Positions (121–180)
  - Standard Deviations (181–240)

#### Feature Distributions

| Raw Data | After Normalization |
|:---------:|:------------------:|
| <img src="plots/BoxPlot1-60.png" width="360"/> | <img src="plots/BoxPlotAll.png" width="360"/> |

*(Left: unscaled feature clusters; Right: normalized feature set.)*

---

### 2. **Cosine Angles and Statistical Features**

<p align="center">
  <img src="plots/BoxPlot60-120.png" alt="Cosine Angles Boxplot" width="720"/>
</p>

Visualizing angular relationships between gestures — these cosine-derived features  
represent the *geometric consistency* of the recorded hand trajectories.

<p align="center">
  <img src="plots/BoxPlot120-180.png" alt="Mean Positions Boxplot" width="720"/>
</p>

Mean and standard-deviation feature groups (below) quantify stability and variation.

<p align="center">
  <img src="plots/BoxPlot180-240.png" alt="STD Positions Boxplot" width="720"/>
</p>

---

### 3. **Spiking Neuron Simulation**

Implements a **Leaky Integrate-and-Fire (LIF)** neuron model:

\[
\tau_m \frac{du}{dt} = -(u - u_{rest}) + R \cdot I_{syn}
\]

| Symbol | Meaning | Value |
|:--|:--|:--|
| R | Membrane resistance | 95 MΩ |
| τₘ | Membrane time constant | 3 ms |
| u_rest | Resting potential | −65 mV |
| u_reset | Reset potential | −65 mV |
| u_thres | Spike threshold | −50 mV |

Scripts explore:
- Membrane potential buildup  
- Threshold-triggered spiking  
- Reset and refractory dynamics  

#### Membrane Potential Buildup

<p align="center">
  <img src="plots/potential_build_up_example.png" alt="LIF neuron potential buildup" width="720"/>
</p>

*(Membrane voltage integration until the firing threshold, then reset.)*

#### 🔍 Spike Current Threshold Search

<p align="center">
  <img src="plots/spike_threshold_search.png" alt="Threshold current scan" width="720"/>
</p>

*(Systematically increasing synaptic input to find the minimal spiking current, ~160 pA.)*

---

### 4. **Example Outputs**

- **Data Exploration**
  - Boxplots of normalized gesture features  
  - Heatmaps showing missing-value patterns  
- **Neuron Simulation**
  - Time-domain voltage trajectories  
  - Spike detection and current threshold curves  

---

### 5. **Future Directions**

- Multi-neuron SNN simulation  
- Synaptic plasticity (e.g. STDP)  
- Real-time sensory encoding  
- Hybrid AI × SNN architectures  

---

## Author

**Magnus Hjornhede**  
Göteborg · Sweden  

---

