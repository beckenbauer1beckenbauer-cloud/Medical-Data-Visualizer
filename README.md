# ================================================================================
#          MEDICAL DATA VISUALIZER: COMPLETE FILE SUITE FOR FREECODECAMP
# ================================================================================

This master block contains all three essential files needed to pass the freeCodeCamp 
Medical Data Visualizer project. Copy this block and extract the files accordingly.

--------------------------------------------------------------------------------
FILE 1: medical_data_visualizer.py (The Solution File)
--------------------------------------------------------------------------------
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import the data from medical_examination.csv
df = pd.read_csv('medical_examination.csv')

# 2. Add an overweight column
# Formula: weight (kg) / [height (m)]^2. Note: height is given in cm, so divide by 100.
bmi = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (bmi > 25).astype(int)

# 3. Normalize data by making 0 always good and 1 always bad
# If value is 1 -> 0. If value is > 1 -> 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Draw the Categorical Plot
def draw_cat_plot():
    # 5. Create a DataFrame for the cat plot using pd.melt
    df_cat = pd.melt(
        df, 
        id_vars=['cardio'], 
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # 6. Group and reformat the data to split it by cardio and show the counts
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # 7. Convert data into long format and create the chart using sns.catplot()
    cat_plot = sns.catplot(
        x='variable', 
        y='total', 
        hue='value', 
        col='cardio', 
        data=df_cat, 
        kind='bar'
    )

    # 8. Get the figure for the output
    fig = cat_plot.fig

    # 9. Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# 10. Draw the Heat Map
def draw_heat_map():
    # 11. Clean the data in df_heat by filtering out incorrect segments
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12. Calculate the correlation matrix
    corr = df_heat.corr()

    # 13. Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15. Plot the correlation matrix using sns.heatmap()
    sns.heatmap(
        corr, 
        mask=mask, 
        annot=True, 
        fmt=".1f", 
        center=0, 
        vmin=-0.1, 
        vmax=0.32, 
        square=True, 
        linewidths=.5, 
        cbar_kws={"shrink": .5}
    )

    # 16. Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

--------------------------------------------------------------------------------
FILE 2: main.py (The Executable Entry Point)
--------------------------------------------------------------------------------
import medical_data_visualizer
from unittest import main

# Test your functions by fetching the figures
print("Generating Categorical Plot...")
medical_data_visualizer.draw_cat_plot()

print("Generating Heat Map Correlation Matrix...")
medical_data_visualizer.draw_heat_map()

# Run automated tests automatically
print("\nRunning automated unit tests...")
main(module='test_module', exit=False)

--------------------------------------------------------------------------------
FILE 3: README.md (The Project Documentation)
--------------------------------------------------------------------------------
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
