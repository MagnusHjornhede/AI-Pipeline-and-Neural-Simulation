# AI Pipeline and Neural Simulation

---

## Project Overview

This repository combines structured machine learning preprocessing with biologically inspired neuron simulation.

It demonstrates two complementary competencies:

* Building a clean, reproducible data processing pipeline
* Modeling neural dynamics using a Leaky Integrate-and-Fire (LIF) framework

The project bridges conventional AI workflows with neuromorphic computation concepts.

<p align="center">
  <img src="plots/pipeline_overview.png" alt="Pipeline Overview Diagram" width="750"/>
</p>

---

## What This Project Shows

* Feature engineering and normalization for structured gesture data
* Statistical diagnostics and visualization
* Implementation of a biophysical neuron model
* Parameter exploration and spike threshold analysis
* Understanding of temporal integration and event-based computation

This repository is structured to reflect both analytical rigor and neural modeling insight.

---

## Part I — Gesture Data Pipeline

The preprocessing pipeline operates on gesture datasets (`train-final.csv`, `test-final.csv`) and prepares features for machine learning models.

### Pipeline Capabilities

* Automatic handling of missing values
* Feature scaling via `MinMaxScaler` or `StandardScaler`
* Structured visualization of 240 engineered features
* Clear separation of feature groups

### Feature Structure

The dataset is organized into four groups:

1. **Joint Positions (1–60)** — raw spatial coordinates
2. **Cosine Angles (61–120)** — geometric joint relationships
3. **Mean Positions (121–180)** — average movement patterns
4. **Standard Deviations (181–240)** — variability over time

#### Example Feature Distributions

<p align="center">
  <img src="plots/BoxPlot1-60.png" width="720"/> 
</p>

<p align="center">
  <img src="plots/BoxPlot60-120.png" width="720"/>
</p>

<p align="center">
  <img src="plots/BoxPlot120-180.png" width="720"/>
</p>

<p align="center">
  <img src="plots/BoxPlot180-240.png" width="720"/>
</p>

These visualizations demonstrate structured variation across gesture types and validate the engineered feature design.

---

## Part II — Spiking Neuron Simulation

The second component implements a **Leaky Integrate-and-Fire (LIF)** neuron model to simulate membrane potential dynamics under controlled synaptic input.

### Governing Equation

[
\tau_m \frac{du}{dt} = -(u - u_{rest}) + R \cdot I_{syn}
]

### Parameter Configuration

| Parameter | Meaning                | Value  |
| :-------- | :--------------------- | :----- |
| R         | Membrane resistance    | 95 MΩ  |
| τₘ        | Membrane time constant | 3 ms   |
| u_rest    | Resting potential      | −65 mV |
| u_reset   | Reset potential        | −65 mV |
| u_thres   | Spike threshold        | −50 mV |

---

### Membrane Potential Integration

<p align="center">
  <img src="plots/potential_build_up_example.png" width="720"/>
</p>

The neuron integrates synaptic input until the threshold is reached, then emits a spike and resets — modeling event-driven computation.

---

### Spike Threshold Analysis

<p align="center">
  <img src="plots/spike_threshold_search.png" width="720"/>
</p>

A systematic current sweep determines the minimal synaptic input required for sustained spiking (~160 pA).

This analysis demonstrates:

* Sensitivity to input strength
* Relationship between current amplitude and firing behavior
* Practical exploration of neuron stability

---

## Why This Project Matters

Modern AI is moving toward:

* Event-driven processing
* Energy-efficient computation
* Neuromorphic hardware systems

This project reflects

* Classical structured ML pipelines
* Biophysical neural modeling foundations

It provides a stepping stone toward hybrid AI–SNN systems and hardware-aware neural architectures.

---

---

## Author

Magnus Hjornhede
Göteborg · Sweden

```
