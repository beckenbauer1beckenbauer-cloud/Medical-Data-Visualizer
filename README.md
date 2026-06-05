# ================================================================================
#          MEDICAL DATA VISUALIZER: COMPLETE FILE SUITE FOR FREECODECAMP
# ================================================================================

This master block contains all three essential files needed to pass the freeCodeCamp 
Medical Data Visualizer project. Copy this block and extract the files accordingly.

# Medical Data Visualizer

A data science and visualization project completed for the **Data Analysis with Python** certification on **freeCodeCamp**.

This project processes, cleans, normalizes, and visualizes body metrics and clinical examination data collected from patients. It evaluates the relational correlations between lifestyle habits, physiological measurements, and cardiovascular diseases.

## 📈 Visualizations Included

1. **Categorical Strip Chart (`catplot.png`)**: Splits patients by their cardiovascular health status (`cardio=0` vs `cardio=1`) and contrasts the explicit totals of good vs bad habits/metrics across 6 major health indicators.
2. **Correlation Matrix Heatmap (`heatmap.png`)**: A clean, diagonally-masked triangular matrix visualizing correlation coefficients between elements like age, weight, blood pressure, cholesterol, and cardiovascular disease presence.

## 🛠️ Data Engineering Operations Applied

* **BMI Aggregations**: Derived an `overweight` indicator feature from raw scales via conditional metric equations.
* **Feature Normalization**: Aligned disparate qualitative tracking formats into strict binary configurations ($0 = \text{Good}$, $1 = \text{Bad}$).
* **Advanced Positional Filtering**: Stripped statistical anomalies and processing bugs out of the dataset using multi-variable quantile thresholds (`0.025` and `0.975`).

## 🚀 Execution

Execute the visualization renderer and testing pipeline via terminal:
```bash
python main.py
