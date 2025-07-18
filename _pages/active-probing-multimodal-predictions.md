---
layout: single
title: " "
permalink: /papers/active-probing-multimodal-predictions/
author_profile: false
classes: wide
---

<div class="paper-header">
  <h1 class="paper-title">Active Probing with Multimodal Predictions for Motion Planning</h1>
  
  <div class="authors">
    <span class="author">Darshan Gadginmath<sup>1,2</sup></span>
    <span class="author">Farhad Nawaz<sup>1</sup></span>
    <span class="author">Minjun Sung<sup>1</sup></span>
    <span class="author">Faizan M Tariq<sup>1</sup></span>
    <span class="author">Sangjae Bae<sup>1</sup></span>
    <span class="author">David Isele<sup>1</sup></span>
    <span class="author">Fabio Pasqualetti<sup>2</sup></span>
    <span class="author">Jovin D'sa<sup>1</sup></span>
  </div>
  
  <div class="affiliations">
    <p><sup>1</sup>Honda Research Institute, USA, San Jose, CA</p>
    <p><sup>2</sup>Department of Mechanical Engineering, University of California Riverside</p>
  </div>
  
  <div class="conference">
    <strong>IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) 2025</strong>
  </div>
</div>

<div class="paper-links">
  <a href="https://arxiv.org/pdf/2507.09822" class="btn btn--primary">Paper (arxiv)</a>
  <a href="https://www.github.com/darshangm" class="btn btn--info">Code</a>
  <a href="https://www.youtube.com/watch?v=GBGBFXxoEmM" class="btn btn--success">Video</a>
</div>

## Abstract

Navigation in dynamic environments requires autonomous systems to reason about uncertainties in the behavior of other agents. In this paper, we introduce a unified framework that combines trajectory planning with multimodal predictions and active probing to enhance decision-making under uncertainty. We develop a novel risk metric that seamlessly integrates multimodal prediction uncertainties through mixture models. When these uncertainties follow a Gaussian mixture distribution, we prove that our risk metric admits a closed-form solution, and is always finite, thus ensuring analytical tractability. 

To reduce prediction ambiguity, we incorporate an active probing mechanism that strategically selects actions to improve its estimates of behavioral parameters of other agents, while simultaneously handling multimodal uncertainties. We extensively evaluate our framework in autonomous navigation scenarios using the MetaDrive simulation environment. Results demonstrate that our active probing approach successfully navigates complex traffic scenarios with uncertain predictions. Additionally, our framework shows robust performance across diverse traffic agent behavior models, indicating its broad applicability to real-world autonomous navigation challenges.

## Key Contributions

- **Novel Risk Metric**: A Wasserstein-based risk metric that rigorously quantifies risk by incorporating both multimodal prediction uncertainties and deviations from the ego agent's reference trajectory.

- **Analytical Tractability**: Closed-form solution to risk computation with proof that the risk is always finite when prediction uncertainties follow a Gaussian mixture distribution.

- **Active Probing Framework**: A proactive strategy to infer agent behavior while seamlessly integrating multimodal predictions and their associated uncertainties, scaling efficiently with the number of prediction modes and agents.

- **Comprehensive Evaluation**: Extensive validation in MetaDrive simulation environment across diverse traffic scenarios including merging situations and dense intersections.

## Method Overview

<div class="method-figure">
  <img src="/images/highway_fig.png" alt="Method Overview" style="width: 100%; max-width: 800px;">
  <p class="caption"><strong>Figure 1:</strong> Illustrative figure of a merging scenario with uncertain multimodal predictions. The red vehicle represents the ego agent with its intended trajectory given by the pink dashed line. The predictor provides multimodal predictions and assigns likelihoods to each mode, with colored ellipsoids representing uncertainty extent.</p>
</div>

Our framework addresses three key challenges in autonomous navigation:

### 1. Utility Maximization
We define a utility-based reward that encourages the ego agent to follow a reference trajectory while maintaining driving comfort and fuel efficiency.

### 2. Safety with Risk Assessment  
We develop a probabilistic risk metric using the 2-Wasserstein distance between the ego agent's planned trajectory distribution and predicted trajectories of other agents. This metric:
- Directly incorporates prediction uncertainties
- Provides closed-form risk computation for multimodal distributions 
- Captures distributional proximity weighted by prediction confidence

### 3. Active Probing for Behavior Inference
Our active probing mechanism:
- Models agent interactions through reward functions rather than joint dynamics
- Uses a modified Boltzmann model informed by predicted likelihoods
- Employs information-theoretic measures to maximize learning about agent behaviors
- Includes risk-aware thresholding to prevent dangerous probing actions

## Demonstration {#videos}
<iframe width="560" height="315" 
        src="https://www.youtube.com/embed/GBGBFXxoEmM" 
        title="Active probing based motion planning" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        allowfullscreen>
</iframe>

## Code

Code will be made available [here](https://www.github.com/darshangm/)

## Citation

```bibtex
@inproceedings{gadginmath2025activebehaviorinference,
  title={Active Probing with Multimodal Predictions for Motion Planning},
  author={Gadginmath, Darshan and Nawaz, Farhad and Sung, Minjun and Tariq, Faizan M and Bae, Sangjae and Isele, David and Pasqualetti, Fabio and D'sa, Jovin},
  booktitle={IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
  year={2025}
}
```

## Acknowledgments

This work was conducted during Darshan Gadginmath's internship at Honda Research Institute, USA. We thank the Honda Research Institute team for their support and resources.

<style>
/* Import Fira Sans font */
@import url('https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap');

/* Apply Fira Sans globally */
body, .paper-header, .paper-title, h1, h2, h3, h4, h5, h6, p, div, span {
  font-family: 'Fira Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

/* Make page wider */
.page {
  max-width: 1400px !important;
  margin: 0 auto;
  padding: 0 2rem;
}

.page__content {
  max-width: none !important;
  margin: 0 !important;
  padding: 0 !important;
}

/* Responsive width adjustments */
@media (min-width: 1200px) {
  .page {
    max-width: 1600px !important;
    padding: 0 3rem;
  }
}

@media (min-width: 1400px) {
  .page {
    max-width: 1800px !important;
    padding: 0 4rem;
  }
}

.paper-header {
  text-align: center;
  margin-bottom: 2em;
  padding: 2em 0;
  border-bottom: 2px solid #f0f0f0;
}

.paper-title {
  font-size: 2.5em;
  font-weight: 600;
  margin-bottom: 1em;
  color: #2c3e50;
  line-height: 1.2;
}

.authors {
  font-size: 1.2em;
  margin-bottom: 1em;
  line-height: 1.6;
  font-weight: 400;
}

.author {
  margin-right: 1em;
}

.affiliations {
  font-size: 1em;
  color: #666;
  margin-bottom: 1em;
  font-weight: 300;
}

.conference {
  font-size: 1.1em;
  color: #e74c3c;
  margin-bottom: 2em;
  font-weight: 500;
}

.paper-links {
  text-align: center;
  margin: 2em 0;
}

/* Modern button styles - made more specific to override theme */
.paper-links a.btn {
  margin: 0.8em !important;
  padding: 0.6em 1.2em !important;
  text-decoration: none !important;
  border-radius: 12px !important;
  font-weight: 500 !important;
  display: inline-block !important;
  border: 2px solid !important;
  background: rgba(255, 255, 255, 0.1) !important;
  backdrop-filter: blur(10px);
  transition: all 0.3s ease !important;
  position: relative;
  overflow: hidden;
  font-size: 0.9rem !important;
}

.paper-links a.btn:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15) !important;
  background: rgba(255, 255, 255, 0.2) !important;
  text-decoration: none !important;
}

.paper-links a.btn.btn--primary { 
  border-color: #e74c3c !important; 
  color: #e74c3c !important;
  background: linear-gradient(145deg, rgba(231, 76, 60, 0.1), rgba(231, 76, 60, 0.05)) !important;
}
.paper-links a.btn.btn--primary:hover { 
  background: linear-gradient(145deg, rgba(231, 76, 60, 0.2), rgba(231, 76, 60, 0.1)) !important;
  box-shadow: 0 8px 25px rgba(231, 76, 60, 0.3) !important;
  color: #e74c3c !important;
}

.paper-links a.btn.btn--info { 
  border-color: #9b59b6 !important; 
  color: #9b59b6 !important;
  background: linear-gradient(145deg, rgba(155, 89, 182, 0.1), rgba(155, 89, 182, 0.05)) !important;
}
.paper-links a.btn.btn--info:hover { 
  background: linear-gradient(145deg, rgba(155, 89, 182, 0.2), rgba(155, 89, 182, 0.1)) !important;
  box-shadow: 0 8px 25px rgba(155, 89, 182, 0.3) !important;
  color: #9b59b6 !important;
}

.paper-links a.btn.btn--success { 
  border-color: #f39c12 !important; 
  color: #f39c12 !important;
  background: linear-gradient(145deg, rgba(243, 156, 18, 0.1), rgba(243, 156, 18, 0.05)) !important;
}
.paper-links a.btn.btn--success:hover { 
  background: linear-gradient(145deg, rgba(243, 156, 18, 0.2), rgba(243, 156, 18, 0.1)) !important;
  box-shadow: 0 8px 25px rgba(243, 156, 18, 0.3) !important;
  color: #f39c12 !important;
}

.paper-links a.btn.btn--warning { 
  border-color: #16a085 !important; 
  color: #16a085 !important;
  background: linear-gradient(145deg, rgba(22, 160, 133, 0.1), rgba(22, 160, 133, 0.05)) !important;
}
.paper-links a.btn.btn--warning:hover { 
  background: linear-gradient(145deg, rgba(22, 160, 133, 0.2), rgba(22, 160, 133, 0.1)) !important;
  box-shadow: 0 8px 25px rgba(22, 160, 133, 0.3) !important;
  color: #16a085 !important;
}

.method-figure {
  text-align: center;
  margin: 2em 0;
}

.caption {
  font-style: italic;
  color: #666;
  margin-top: 0.5em;
  font-weight: 300;
}

.results-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2em;
  margin: 2em 0;
}

.result-item {
  background: #f8f9fa;
  padding: 1.5em;
  border-radius: 8px;
  border-left: 4px solid #3498db;
}

.result-item table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1em;
}

.result-item th, .result-item td {
  padding: 0.7em;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.result-item th {
  background-color: #e9ecef;
  font-weight: 600;
}

.video-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2em;
  margin: 2em 0;
}

.video-item {
  background: #f8f9fa;
  padding: 1.5em;
  border-radius: 8px;
}

.video-item h4 {
  margin-top: 0;
  color: #2c3e50;
  font-weight: 600;
}

/* Responsive styles */
@media (max-width: 768px) {
  .paper-title {
    font-size: 1.8em;
  }
  
  .authors {
    font-size: 1em;
  }
  
  .paper-links .btn {
    display: block;
    margin: 0.5em 0;
  }
  
  .video-grid {
    grid-template-columns: 1fr;
  }
  
  .page {
    padding: 0 1rem !important;
  }
}
</style>