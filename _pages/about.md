---
permalink: /
title: "About me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<style>
/* ── research thread cards ── */
.rp-cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  margin: 1.5rem 0 2rem;
}
.rp-card {
  background: #1c1c1c;
  border: 0.5px solid #2a2a2a;
  border-radius: 8px;
  padding: 14px 12px;
  text-decoration: none;
  display: block;
  transition: border-color 0.15s;
}
.rp-card:hover { border-color: #444; text-decoration: none; }
.rp-card-bar {
  height: 3px;
  border-radius: 2px;
  width: 24px;
  margin-bottom: 10px;
}
.rp-card-title {
  font-size: 0.78rem;
  font-weight: 500;
  color: #ddd;
  margin: 0 0 4px;
  line-height: 1.35;
}
.rp-card-desc {
  font-size: 0.7rem;
  color: #666;
  line-height: 1.5;
  margin: 0;
}

/* ── news ── */
.news-list {
  list-style: none;
  padding: 0;
  margin: 0;
}
.news-item {
  display: flex;
  gap: 10px;
  align-items: flex-start;
  padding: 10px 0;
  border-bottom: 0.5px solid #1f1f1f;
  font-size: 0.83rem;
}
.news-item:last-child { border-bottom: none; }
.news-tag {
  display: inline-block;
  font-size: 0.62rem;
  font-weight: 500;
  padding: 2px 8px;
  border-radius: 10px;
  white-space: nowrap;
  flex-shrink: 0;
  margin-top: 1px;
}
.tag-phd    { background: #1e2e28; color: #5DCAA5; }
.tag-pub    { background: #1e1e2e; color: #AFA9EC; }
.tag-talk   { background: #2a2010; color: #EF9F27; }
.tag-award  { background: #1e2a1e; color: #97C459; }
.news-text  { color: #999; line-height: 1.55; }
.news-text a { color: #5DCAA5; text-decoration: none; }
.news-text a:hover { text-decoration: underline; }
.news-date  { color: #555; font-size: 0.7rem; display: block; margin-top: 2px; }

@media (max-width: 600px) {
  .rp-cards { grid-template-columns: 1fr; }
}
</style>

I am a Research Scientist at [Mitsubishi Electric Research Laboratories (MERL)](https://www.merl.com/) in Cambridge, MA, working on the Control for Autonomy team. I recently completed my PhD in Mechanical Engineering at UC Riverside, advised by [Prof. Fabio Pasqualetti](https://www.fabiopas.it/).

My research develops algorithms for safe autonomy — using control barrier functions, diffusion models, and Koopman operator theory to build robots and autonomous agents that can plan and adapt reliably in uncertain environments.

Previously, I was a Research Intern at the Honda Research Institute, and a Research Assistant with [Dr. Pavankumar Tallapragada](https://ee.iisc.ac.in/~pavant/) at the Indian Institute of Science. I received my B.E. in Electrical and Electronics Engineering from RV College of Engineering, Bengaluru.

<div class="rp-cards">
  <a class="rp-card" href="/research/#safe-generative-sampling">
    <div class="rp-card-bar" style="background:#5DCAA5;"></div>
    <p class="rp-card-title">Safe generative sampling</p>
    <p class="rp-card-desc">CBF-guided diffusion with prescribed-time guarantees</p>
  </a>
  <a class="rp-card" href="/research/#koopman-control">
    <div class="rp-card-bar" style="background:#AFA9EC;"></div>
    <p class="rp-card-title">Data-driven control</p>
    <p class="rp-card-desc">Feedback linearization via Koopman operator methods</p>
  </a>
  <a class="rp-card" href="/research/#active-probing">
    <div class="rp-card-bar" style="background:#EF9F27;"></div>
    <p class="rp-card-title">Active probing</p>
    <p class="rp-card-desc">Uncertainty-aware intent inference for autonomous driving</p>
  </a>
</div>

## News

<ul class="news-list">
  <li class="news-item">
    <span class="news-tag tag-phd">PhD</span>
    <span class="news-text">
      Defended my dissertation — <em>Unifying Generative Sampling and Data-Driven Control for Safe Autonomy</em>
      <span class="news-date">March 2026</span>
    </span>
  </li>
  <li class="news-item">
    <span class="news-tag tag-pub">Preprint</span>
    <span class="news-text">
      Two new preprints on safe generative sampling, and control with constricting barrier functions —
      <a href="https://arxiv.org/abs/2602.21429">arXiv 2602.21429</a> and
      <a href="https://arxiv.org/abs/2603.17003">arXiv 2603.17003</a>
      <span class="news-date">February – March 2026</span>
    </span>
  </li>
  <li class="news-item">
    <span class="news-tag tag-pub">Preprint</span>
    <span class="news-text">
      Two new papers on dynamics-aware diffusion models for robotics and control —
      <a href="https://arxiv.org/pdf/2504.00236">Paper 1</a>,
      <a href="https://arxiv.org/pdf/2504.09836">Paper 2</a>
      <span class="news-date">April 2025</span>
    </span>
  </li>
  <li class="news-item">
    <span class="news-tag tag-talk">Talk</span>
    <span class="news-text">
      Invited talk at USC — probabilistic perspectives for AI agent behavior and nonlinear control
      <span class="news-date">September 2024</span>
    </span>
  </li>
</ul>