# Air Quality Analytics Dashboard Using Apache Spark

A big data analytics system for analyzing and visualizing air quality trends across Indian cities using Apache Spark and Streamlit.

The project processes large-scale AQI datasets to identify pollution trends, anomaly patterns, city-wise pollution distribution, and environmental insights through interactive visualizations.

---

## Features

- Large-scale AQI data analysis using Apache Spark
- Interactive Streamlit dashboard
- Temporal AQI trend analysis
- City-wise pollution comparison
- Heatmaps and correlation analysis
- AQI anomaly and extreme event detection
- Spatial visualization using map-based analytics

---

## Tech Stack

| Category | Technologies |
|---|---|
| Big Data Processing | Apache Spark, PySpark |
| Data Analysis | Pandas, NumPy |
| Visualization | Streamlit, Matplotlib, Plotly |
| Environment | Google Colab |
| Language | Python |

---

## Dataset

The project uses the **Air Quality Dataset: Indian Cities (2022–2025)** from Kaggle.

Dataset Highlights:
- 842,000+ hourly observations
- 29 Indian cities
- 60+ environmental and meteorological features

Dataset Link:  
https://www.kaggle.com/datasets/bhautikvekariya21/air-quality-dataset-indian-cities-2022-2025

---

## Big Data Concepts Demonstrated

- Distributed Data Processing
- Parallel Computation
- Spark DataFrames
- Window Functions
- Data Partitioning
- Caching and Optimization
- Statistical Anomaly Detection

---

## Key Analysis Performed

### Temporal Trend Analysis
- Daily AQI trends
- Hourly pollution pattern analysis

### City-wise AQI Comparison
- Highest AQI cities
- Lowest AQI cities

### Correlation Analysis
- PM2.5 vs AQI
- PM10 and NO₂ impact
- Weather influence on pollution

### Anomaly Detection
- Detection of unusual AQI spikes
- Identification of hazardous pollution events

### Spatial Analysis
- AQI map visualization using geographical coordinates

---

## Spark Operations Used

- Aggregation and Grouping
- Window Functions
- Ranking
- Filtering
- Statistical Analysis
- Partitioning
- Caching

---

## Installation

```bash
git clone https://github.com/kavana185/Air-Quality-Analytics-Dashboard-Using-Spark
cd Air-Quality-Analytics-Dashboard-Using-Spark
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## Dashboard Visualizations

- AQI trend plots
- Heatmaps
- Correlation matrices
- AQI anomaly detection
- City-wise AQI comparisons
- Spatial AQI maps

---

## Future Improvements

- Real-time AQI data integration
- AQI forecasting using ML models
- Advanced dashboard filtering
- City-level deep analysis
- Real-time anomaly alerts

---
