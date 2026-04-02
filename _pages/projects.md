---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

<style>
/* ── reset & base ── */
.research-page * { box-sizing: border-box; }

.research-page {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  color: #aaa;
  max-width: 760px;
}

/* ── section labels ── */
.rp-section-label {
  font-size: 0.65rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #555;
  margin: 0 0 1.5rem;
  padding-bottom: 0.5rem;
  border-bottom: 0.5px solid #2a2a2a;
}

/* ── thread block ── */
.rp-thread {
  display: flex;
  gap: 18px;
  margin-bottom: 3rem;
  padding-bottom: 3rem;
  border-bottom: 0.5px solid #1f1f1f;
  align-items: flex-start;
}
.rp-thread:last-of-type {
  border-bottom: none;
}

.rp-bar {
  width: 3px;
  border-radius: 2px;
  flex-shrink: 0;
  margin-top: 4px;
  min-height: 48px;
  align-self: stretch;
}

.rp-thread-content { flex: 1; min-width: 0; }

.rp-thread-title {
  font-size: 1rem;
  font-weight: 500;
  color: #f0f0f0;
  margin: 0 0 3px;
  line-height: 1.3;
}

.rp-thread-sub {
  font-size: 0.7rem;
  color: #555;
  margin: 0 0 0.9rem;
}

.rp-desc {
  font-size: 0.83rem;
  color: #999;
  line-height: 1.7;
  margin: 0 0 0.9rem;
}

/* ── contributions ── */
.rp-contribs {
  list-style: none;
  padding: 0;
  margin: 0 0 0.9rem;
}
.rp-contribs li {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  font-size: 0.78rem;
  color: #888;
  margin-bottom: 5px;
  line-height: 1.5;
}
.rp-contribs li::before {
  content: '';
  display: block;
  width: 4px;
  height: 4px;
  border-radius: 50%;
  flex-shrink: 0;
  margin-top: 6px;
}
.rp-thread--teal   .rp-contribs li::before { background: #5DCAA5; }
.rp-thread--purple .rp-contribs li::before { background: #AFA9EC; }
.rp-thread--amber  .rp-contribs li::before { background: #EF9F27; }

/* ── link pills ── */
.rp-links {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 1.1rem;
}
.rp-link {
  display: inline-block;
  font-size: 0.7rem;
  padding: 2px 10px;
  border-radius: 4px;
  text-decoration: none;
  transition: opacity 0.15s;
}
.rp-link:hover { opacity: 0.75; text-decoration: none; }

.rp-thread--teal   .rp-link { color: #5DCAA5; border: 0.5px solid #2a4a3e; background: #1a2a24; }
.rp-thread--purple .rp-link { color: #AFA9EC; border: 0.5px solid #3a3260; background: #1e1e2e; }
.rp-thread--amber  .rp-link { color: #EF9F27; border: 0.5px solid #4a3a10; background: #2a2010; }

/* ── video grid ── */
.rp-videos {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}
.rp-video-wrap {
  flex: 1;
  min-width: 240px;
  max-width: 360px;
}
.rp-video-wrap iframe {
  width: 100%;
  height: 180px;
  border: 0.5px solid #2a2a2a;
  border-radius: 6px;
  display: block;
}
.rp-video-caption {
  font-size: 0.68rem;
  color: #555;
  margin-top: 5px;
  line-height: 1.4;
}

/* ── earlier work ── */
.rp-earlier { margin-top: 0.5rem; }

.rp-small {
  display: flex;
  gap: 18px;
  align-items: flex-start;
  margin-bottom: 1.1rem;
  padding-bottom: 1.1rem;
  border-bottom: 0.5px solid #1f1f1f;
}
.rp-small:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }

.rp-small-bar {
  width: 3px;
  height: 36px;
  border-radius: 2px;
  background: #2a2a2a;
  flex-shrink: 0;
  margin-top: 2px;
}

.rp-small-title {
  font-size: 0.83rem;
  font-weight: 500;
  color: #ccc;
  margin: 0 0 3px;
}
.rp-small-desc {
  font-size: 0.75rem;
  color: #666;
  line-height: 1.55;
  margin: 0 0 6px;
}
.rp-small-links {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}
.rp-small-link {
  font-size: 0.68rem;
  color: #888;
  border: 0.5px solid #333;
  border-radius: 4px;
  padding: 1px 8px;
  text-decoration: none;
  background: #1c1c1c;
}
.rp-small-link:hover { color: #aaa; text-decoration: none; }

/* responsive */
@media (max-width: 600px) {
  .rp-thread { flex-direction: row; gap: 12px; }
  .rp-video-wrap { min-width: 100%; }
  .rp-videos { flex-direction: column; }
}
</style>

<div class="research-page">

<p style="font-size:0.85rem; color:#888; margin-bottom:2rem; line-height:1.7;">
I develop algorithms for safe autonomy — bridging control theory, machine learning, and robotics. My dissertation unified three threads: steering generative models for safe planning, data-driven feedback linearization via Koopman operators, and active probing for intent inference under uncertainty.
</p>

<div class="rp-section-label">Research threads</div>

<!-- ── Thread 1: Safe generative sampling ── -->
<div class="rp-thread rp-thread--teal">
  <div class="rp-bar" style="background:#5DCAA5;"></div>
  <div class="rp-thread-content">
    <p class="rp-thread-title">Safe generative sampling</p>
    <p class="rp-thread-sub">2023 – present &nbsp;·&nbsp; Dissertation chapter I</p>
    <p class="rp-desc">
      Diffusion models generate impressive plans and trajectories but offer no safety guarantees out of the box. I develop <em>constricting control barrier functions</em> that steer the reverse diffusion process to stay within safe regions — provably, without resampling or post-processing, and without modifying the underlying model.
    </p>
    <ul class="rp-contribs">
      <li>Prescribed-time safety guarantees via constricting tubes in the diffusion trajectory</li>
      <li>Applies to image generation, trajectory planning, and multi-robot swarm control</li>
      <li>No modification to the pretrained diffusion model required</li>
    </ul>
    <div class="rp-links">
      <a class="rp-link" href="https://arxiv.org/abs/2602.21429">arXiv 2602.21429</a>
      <a class="rp-link" href="https://arxiv.org/abs/2603.17003">arXiv 2603.17003</a>
      <a class="rp-link" href="https://arxiv.org/pdf/2504.00236">CDC 2025 (paper 1)</a>
      <a class="rp-link" href="https://arxiv.org/pdf/2504.09836">CDC 2025 (paper 2)</a>
      <a class="rp-link" href="https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10886071">TAC</a>
      <a class="rp-link" href="https://github.com/darshangm/diffusion-nonlinear-control">Code</a>
    </div>
    <div class="rp-videos">
      <div class="rp-video-wrap">
        <iframe src="https://www.youtube.com/embed/3qQoxwMP33M"
          title="Swarm control with dynamics-aware diffusion"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen></iframe>
        <p class="rp-video-caption">Swarm control with dynamics-aware diffusion</p>
      </div>
      <div class="rp-video-wrap">
        <iframe src="https://www.youtube.com/embed/tbaFg1HthMo"
          title="Deployment on multiple Husky robots"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen></iframe>
        <p class="rp-video-caption">Deployment on multiple Husky robots</p>
      </div>
    </div>
  </div>
</div>

<!-- ── Thread 2: Koopman control ── -->
<div class="rp-thread rp-thread--purple">
  <div class="rp-bar" style="background:#AFA9EC;"></div>
  <div class="rp-thread-content">
    <p class="rp-thread-title">Data-driven control via Koopman operators</p>
    <p class="rp-thread-sub">2022 – present &nbsp;·&nbsp; Dissertation chapter II</p>
    <p class="rp-desc">
      Feedback linearization is a powerful control technique but requires an exact analytic model. I use the Koopman operator and its generator to learn the linearizing transformation directly from data — making interpretable, theoretically grounded controllers available for systems where no model exists.
    </p>
    <ul class="rp-contribs">
      <li>Data-driven feedback linearization with finite-sample guarantees</li>
      <li>Complete dictionary conditions for exact linearization from data</li>
      <li>Two IEEE Transactions on Automatic Control papers</li>
    </ul>
    <div class="rp-links">
      <a class="rp-link" href="https://ieeexplore.ieee.org/abstract/document/10565947">TAC 2024</a>
      <a class="rp-link" href="https://arxiv.org/pdf/2308.11229">arXiv 2308.11229</a>
      <a class="rp-link" href="https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10383720">CDC 2023</a>
    </div>
    <div class="rp-videos">
      <div class="rp-video-wrap">
        <iframe src="https://www.youtube.com/embed/zHBFvQXijQk"
          title="Koopman-based nonlinear control demo"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen></iframe>
        <p class="rp-video-caption">Koopman-based nonlinear control demo</p>
      </div>
    </div>
  </div>
</div>

<!-- ── Thread 3: Active probing ── -->
<div class="rp-thread rp-thread--amber">
  <div class="rp-bar" style="background:#EF9F27;"></div>
  <div class="rp-thread-content">
    <p class="rp-thread-title">Active probing for intent inference</p>
    <p class="rp-thread-sub">2024 &nbsp;·&nbsp; Honda Research Institute internship &nbsp;·&nbsp; Dissertation chapter III</p>
    <p class="rp-desc">
      Autonomous vehicles can't safely plan without knowing what other drivers intend to do. I developed an active probing framework that strategically selects actions to reduce uncertainty about other agents' behavior, while simultaneously planning safely under multimodal predictions.
    </p>
    <ul class="rp-contribs">
      <li>Closed-form Wasserstein risk metric for multimodal Gaussian mixture predictions</li>
      <li>44% smoother trajectories vs non-probing baseline in MetaDrive simulation</li>
      <li>Risk-aware thresholding prevents dangerous probing actions</li>
    </ul>
    <div class="rp-links">
      <a class="rp-link" href="https://darshangm.github.io/papers/active-probing-multimodal-predictions">Project page</a>
      <a class="rp-link" href="https://arxiv.org/pdf/2507.09822">IROS 2025</a>
      <a class="rp-link" href="https://www.youtube.com/watch?v=GBGBFXxoEmM">Video</a>
    </div>
    <div class="rp-videos">
      <div class="rp-video-wrap">
        <iframe src="https://www.youtube.com/embed/GBGBFXxoEmM"
          title="Active probing in highway merging scenarios"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen></iframe>
        <p class="rp-video-caption">Active probing in highway merging scenarios</p>
      </div>
    </div>
  </div>
</div>

<!-- ── Earlier work ── -->
<div class="rp-section-label" style="margin-top:1rem;">Earlier work</div>

<div class="rp-earlier">

  <div class="rp-small">
    <div class="rp-small-bar"></div>
    <div>
      <p class="rp-small-title">Coverage control of ground robots</p>
      <p class="rp-small-desc">Distributed algorithms for optimal area coverage using teams of ground robots with OptiTrack mocap. Consensus protocol for oscillator-based controller.</p>
      <div class="rp-small-links">
        <a class="rp-small-link" href="https://www.youtube.com/watch?v=KYLpdI5PiXY">Video</a>
      </div>
    </div>
  </div>

  <div class="rp-small">
    <div class="rp-small-bar"></div>
    <div>
      <p class="rp-small-title">Distributed intersection management for CAVs</p>
      <p class="rp-small-desc">Data-guided distributed control for safe and efficient intersection management in connected vehicle environments.</p>
      <div class="rp-small-links">
        <a class="rp-small-link" href="https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9867733">ACC 2022</a>
        <a class="rp-small-link" href="https://www.youtube.com/watch?v=QfIfFiEhi_g">Video</a>
      </div>
    </div>
  </div>

  <div class="rp-small">
    <div class="rp-small-bar"></div>
    <div>
      <p class="rp-small-title">Behavior-based attack detection in dynamical systems</p>
      <p class="rp-small-desc">Direct vs indirect methods for detecting attacks using behavioral analysis. Established a tradeoff between system identification and direct detection.</p>
      <div class="rp-small-links">
        <a class="rp-small-link" href="https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9993195">CDC 2022</a>
      </div>
    </div>
  </div>

  <div class="rp-small">
    <div class="rp-small-bar"></div>
    <div>
      <p class="rp-small-title">Heterogeneous online learning</p>
      <p class="rp-small-desc">Fusing multiple algorithms for online learning with heterogeneous sensor arrays arriving at different rates.</p>
      <div class="rp-small-links">
        <a class="rp-small-link" href="https://arxiv.org/pdf/2312.05432">ACC 2025</a>
      </div>
    </div>
  </div>

</div>
</div>