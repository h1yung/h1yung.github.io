---
layout: archive
title: "Teaching"
permalink: /teaching/
author_profile: true
---

<style>
.teaching-item {
  margin: 0.75em 0;
  border: 1px solid #e8e8e8;
  border-radius: 4px;
  overflow: hidden;
}

.teaching-item details {
  background: #f9f9f9;
}

.teaching-item summary {
  padding: 0.75em 1em;
  cursor: pointer;
  font-size: 0.95em;
  font-weight: bold;
  background: #fff;
  border-bottom: 1px solid #e8e8e8;
  transition: background 0.3s;
  list-style: none;
  display: flex;
  align-items: center;
}

.teaching-item summary::-webkit-details-marker {
  display: none;
}

.teaching-item summary::before {
  content: "▶";
  display: inline-block;
  transition: transform 0.3s;
  margin-right: 0.5em;
  flex-shrink: 0;
}

.teaching-item details[open] summary::before {
  transform: rotate(90deg);
}

.teaching-item summary:hover {
  background: #f5f5f5;
}

.teaching-preview {
  display: flex;
  align-items: center;
  gap: 1em;
}

.teaching-content {
  padding: 0.75em 1em;
  background: #fff;
  line-height: 1.4;
  font-size: 0.9em;
}

.teaching-meta {
  color: #666;
  font-size: 0.85em;
  margin-top: 0.25em;
}

.teaching-content h3 {
  margin-top: 0.75em;
  margin-bottom: 0.35em;
  font-size: 1em;
}
</style>

<!-- Example teaching entries -->
<div class="teaching-item">
  <details>
    <summary>
      <div class="teaching-preview">
        <div>
          <strong>CS 19300 - Tools</strong>
          <div class="teaching-meta">Teaching Assistant • Fall 2021 • Purdue University</div>
        </div>
      </div>
    </summary>
    <div class="teaching-content">
      <p><strong>Venue:</strong> Purdue University, Department of Computer Sciences</p>
      <p><strong>Location:</strong> West Lafayette, IN, USA</p>
      
      <h3>Description</h3>
      <p>Graded assignments on essential computer science topics including Git, Terminal, and Java programming</p>
    </div>
  </details>
</div>

<div class="teaching-item">
  <details>
    <summary>
      <div class="teaching-preview">
        <div>
          <strong>CS19000 - Data Science Seminar</strong>
          <div class="teaching-meta">Teaching Assistant • Fall 2021, Spring 2022 • Purdue University</div>
        </div>
      </div>
    </summary>
    <div class="teaching-content">
      <p><strong>Venue:</strong> Purdue University, Department of Computer Sciences</p>
      <p><strong>Location:</strong> West Lafayette, IN, USA</p>
      
      <h3>Description</h3>
      <p>Provide guidance and insight to over 500 students in weekly office hours on topics regarding data science</p>
    </div>
  </details>
</div>
