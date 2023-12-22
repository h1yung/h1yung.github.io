---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
header:
  og_image: "research/ecdf.png"
---

I envision my Ph.D. thesis to focus on out-of-distribution (OOD) generalization and the robustness of machine learning (ML) models. I will answer the critical question: How can we adapt ML models to effectively generalize across real-world variations while minimizing human supervision? I intend to investigate various facets of robustness improvement, such as generating synthetic data to mitigate substantial costs and potential ethical concerns associated with data collection for adversarially robust classification tasks.

Within this research landscape, I will create new techniques and also examine established methodologies like pre-training, data augmentation, and self-supervision, seeking to leverage their potential to enhance model robustness.
One area of exploration that especially piques my interest is causal ML. In DL, two significant challenges that hinder its adaptation to society are interpretability and robustness. When it comes to interpretability, as DL model performance improves, its explainability typically diminishes. This has implications for transparency, trust, and control in decision-making processes. A promising solution to address these challenges is causal representation learning, which aims to rectify the limitations of DL models that rely on correlation-based variable associations for decisions and are vulnerable to the spurious correlations problem. Essentially, it involves methods for identifying and modeling causal relationships between nodes. Making decisions based on causal inference holds the promise of ensuring prediction robustness not only in situations where data follows an independent and identically distributed (i.i.d.) pattern but also in scenarios with distribution shifts. Therefore, researching and developing techniques based on causal inference to improve ML systems is of the utmost interest.


<nbsp>

{% include base_path %}

{% assign ordered_pages = site.research | sort:"order_number" %}

{% for post in ordered_pages %}
  {% include archive-single.html type="grid" %}
{% endfor %}
