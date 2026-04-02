# AI Pipeline and Neural Simulation


A small project exploring two sides of machine learning:

- building a structured data preprocessing pipeline  
- simulating neuron dynamics with a Leaky Integrate-and-Fire model

The goal is to connect **practical ML workflows** with **biologically inspired computation**.

<br>

## Project Overview

This repository contains two independent but related components.

### 1. Gesture Data Pipeline

A preprocessing pipeline for structured gesture datasets, focusing on feature organization, scaling, and diagnostics.

### 2. Spiking Neuron Simulation

A simple implementation of a **Leaky Integrate-and-Fire (LIF)** neuron model used to explore membrane dynamics and spike generation.

Together they illustrate both:

- practical machine learning data preparation  
- fundamentals of neural computation

<!--
<p align="center">
  <img src="plots/pipeline_overview.png" alt="Pipeline Overview Diagram" width="750"/>
</p>
-->

<br>

## What This Project Demonstrates

This repository focuses on several practical topics:

- feature engineering for structured sensor data  
- dataset normalization and preprocessing  
- statistical diagnostics and visualization  
- simulation of a biophysical neuron model  
- exploration of spike thresholds and temporal integration  

The code is structured and documented to keep the workflow transparent and reproducible.

<br>

## Part I — Gesture Data Pipeline

The preprocessing pipeline operates on gesture datasets (`train-final.csv`, `test-final.csv`) and prepares features for machine learning models.

### Pipeline Capabilities

* Automatic handling of missing values
* Feature scaling via `MinMaxScaler` or `StandardScaler`
* Structured visualization of 240 engineered features
* Clear separation of feature groups

### Feature Structure

The dataset contains **240 engineered features**, divided into four conceptual groups.

1. **Joint Positions (1–60)**  
   Raw spatial coordinates from the gesture capture system.

2. **Cosine Angles (61–120)**  
   Angular relationships between joints.

3. **Mean Positions (121–180)**  
   Average spatial patterns over time.

4. **Standard Deviations (181–240)**  
   Temporal variability of joint movement.

This structure allows the pipeline to analyze both **geometry** and **movement statistics**.



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

<br>

## Part II — Spiking Neuron Simulation

The second component implements a classic **Leaky Integrate-and-Fire (LIF)** neuron model.

This model captures how biological neurons accumulate input current and emit spikes once a threshold is reached.

### Governing Equation

The membrane potential follows the standard LIF equation:

$\tau_m \frac{du}{dt} = -(u - u_{rest}) + R \cdot I_{syn}$

### Parameter Configuration

| Parameter | Meaning                | Value  |
| :-------- | :--------------------- | :----- |
| R         | Membrane resistance    | 95 MΩ  |
| τₘ        | Membrane time constant | 3 ms   |
| u_rest    | Resting potential      | −65 mV |
| u_reset   | Reset potential        | −65 mV |
| u_thres   | Spike threshold        | −50 mV |



### Membrane Potential Integration
<!--
<p align="center">
  <img src="plots/potential_build_up_example.png" width="720"/>
</p>
-->
The neuron integrates incoming current over time.

Once the membrane potential reaches the spike threshold:

1. a spike is emitted  
2. the potential resets  
3. integration continues

This simple mechanism produces **event-driven computation**, which is the basis of many spiking neural network models.



### Spike Threshold Exploration
<!--
<p align="center">
  <img src="plots/spike_threshold_search.png" width="720"/>
</p>
-->
A current sweep experiment was performed to determine the minimal synaptic input required for sustained firing.

The threshold was observed at approximately:

**~160 pA**

This experiment illustrates:

- sensitivity of firing behavior to input strength  
- how neuron parameters influence stability  
- how simple models can reproduce spike dynamics

<br>

## Why This Project Matters

Modern machine learning research is increasingly interested in:

- event-driven computation  
- energy-efficient AI systems  
- neuromorphic hardware  

This project connects two perspectives:

**structured ML data pipelines**

and

**biophysical neuron models**

It explores how classical ML workflows and biologically inspired neuron models can be studied side by side.

The project also provides a simple starting point for thinking about hybrid AI–SNN systems and neuromorphic computation.

<br>

## Author

Magnus H
Göteborg · Sweden

```
