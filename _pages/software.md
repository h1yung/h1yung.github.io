---
layout: archive
title: "Software"
permalink: /software/
author_profile: true
---

<style>
.software-item {
  margin: 0.75em 0;
  border: 1px solid #e8e8e8;
  border-radius: 4px;
  overflow: hidden;
}

.software-item details {
  background: #f9f9f9;
}

.software-item summary {
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

.software-item summary::-webkit-details-marker {
  display: none;
}

.software-item summary::before {
  content: "▶";
  display: inline-block;
  transition: transform 0.3s;
  margin-right: 0.5em;
  flex-shrink: 0;
}

.software-item details[open] summary::before {
  transform: rotate(90deg);
}

.software-item summary:hover {
  background: #f5f5f5;
}

.software-preview {
  display: flex;
  align-items: center;
  gap: 1em;
}

.software-preview img {
  max-width: 120px;
  max-height: 80px;
  object-fit: cover;
  border-radius: 3px;
}

.software-content {
  padding: 0.75em 1em;
  background: #fff;
  line-height: 1.4;
  font-size: 0.9em;
}

.software-content img {
  max-width: 100%;
  height: auto;
  margin: 0.5em 0;
  border-radius: 3px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.1);
}

.software-content h3 {
  margin-top: 0.75em;
  margin-bottom: 0.35em;
  font-size: 1em;
}

.software-meta {
  color: #666;
  font-size: 0.85em;
  margin-top: 0.25em;
}

.software-links {
  margin-top: 0.75em;
}

.software-links a {
  display: inline-block;
  margin-right: 0.5em;
  margin-bottom: 0.25em;
  padding: 0.35em 0.75em;
  background: #0366d6;
  color: white;
  text-decoration: none;
  border-radius: 3px;
  font-size: 0.85em;
  transition: background 0.3s;
}

.software-links a:hover {
  background: #0256c2;
}
</style>

<!-- Example software entries -->
<div class="software-item">
  <details>
    <summary>
      <div class="software-preview">
        <img src="/images/software/lambda-vercel.png" alt="Org Networking Platform" onerror="this.style.display='none'">
        <div>
          <strong>AlumniNetwork</strong>
          <div class="software-meta">Applet helping fraternity & sorority members navigate their alumni network</div>
        </div>
      </div>
    </summary>
    <div class="software-content">
      <p>This applet helps your connection find and connect with each other around the world. It visualizes where our members are located and provides tools to explore lineage and membership history.</p>
      
      <h3>Features</h3>
      <ul>
        <li><strong>Interactive Global Map & Roster:</strong> Visualize members worldwide with location clustering, search filters, and detailed roster views by region.</li>
        <li><strong>Family Lineage & History:</strong> Browse organizational family trees and membership history with encrypted mode for sensitive genealogical data.</li>
        <li><strong>Directory & Meetup Planning:</strong> Searchable member directory with location data and tools for organizing local meetups and gatherings.</li>
      </ul>
      
      <img src="/images/software-screenshot-1.png" alt="Screenshot 1" onerror="this.style.display='none'">
      
      <h3>Technical Details</h3>
        <ul>
        <li><strong>Frontend:</strong> React + TypeScript; Vite (build tool); Leaflet (interactive maps)</li>
        <li><strong>Backend:</strong> Vercel Serverless Functions; Node.js + TypeScript; Redis (data caching)</li>
        <li><strong>Data Pipeline:</strong> Google Sheets API; Google Apps Script (triggers); OpenStreetMap Nominatim (geocoding)</li>
        <li><strong>Infrastructure:</strong> Vercel (hosting); GitHub (version control); SSL/TLS encryption</li>
        </ul>
      
      <img src="/images/software/lambda-vercel2.png" alt="Screenshot 2" onerror="this.style.display='none'">
      
      <div class="software-links">
        <a href="https://github.com/h1yung/lambda-web" target="_blank">GitHub</a>
        <a href="https://lambda-web-seven.vercel.app/" target="_blank">Live Demo</a>
        <!-- <a href="/files/project-paper.pdf" target="_blank">Paper</a> -->
      </div>
    </div>
  </details>
</div>

<!-- Add more software items following the same pattern -->
<div class="software-item">
  <details>
    <summary>
      <div class="software-preview">
        <img src="/images/software/btcdriftpilot.png" alt="BTC DriftPilot" onerror="this.style.display='none'">
        <div>
          <strong>BTC-DriftPilot</strong>
          <div class="software-meta">Applet for BTCUSD trading strategy selection with concept drift monitoring</div>
        </div>
      </div>
    </summary>
    <div class="software-content">
      <p>This adaptive trading system automatically detects market regime shifts and adjusts predictive models in response to concept drift. It combines rigorous statistical analysis with risk controls to execute data-driven trading strategies on Bitcoin and other assets.</p>

      <h3>Features</h3>
      <ul>
        <li><strong>Adaptive Model Retraining:</strong> Monitors market conditions using Page-Hinkley, KS, PSI, and CUSUM drift detectors. Automatically retrains logistic classifiers when concept drift is detected to maintain prediction accuracy across regime changes.</li>
        <li><strong>Dual Strategy Framework:</strong> Choose between short-term adaptive logistic classification (model-based) or long-term SMA momentum strategies (rule-based) with flexible rebalancing modes (weekly, monthly, or custom intervals).</li>
        <li><strong>Risk Management & Backtesting:</strong> Volatility targeting, max-drawdown limits, ATR-based stops, and event-driven simulation with transaction costs. Comprehensive metrics including Sharpe, Sortino, MDD, and hit rate.</li>
      </ul>

      <img src="/images/software-screenshot-1.png" alt="Screenshot 1" onerror="this.style.display='none'">

      <h3>Technical Details</h3>
      <ul>
        <li><strong>Frontend:</strong> Streamlit dashboard with interactive tabs (Overview, Backtest, Drift, Features); Plotly charts and CSV export</li>
        <li><strong>Backend:</strong> Python; scikit-learn (LogisticRegression); NumPy/Pandas (data processing)</li>
        <li><strong>Data Pipeline:</strong> Yahoo Finance and Binance APIs (daily/hourly BTC); feature engineering for technical indicators (RSI, SMA, momentum, volatility, ATR)</li>
        <li><strong>Infrastructure:</strong> GitHub (version control); walk-forward evaluation and event-driven backtesting engine</li>
      </ul>
      
      <div class="software-links">
        <a href="https://github.com/h1yung/driftpilot" target="_blank">GitHub</a>
        <a href="https://btcdriftpilot.streamlit.app/" target="_blank">Live Demo</a>
        <!-- <a href="/files/project-paper.pdf" target="_blank">Paper</a> -->
      </div>
      
    </div>
  </details>
</div>
