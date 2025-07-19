This project analyzes the World Happiness Report data to understand how health and family contribute to national happiness. It includes data cleaning, visualization in Tableau, a predictive model, and an interactive Streamlit app.

![Happiness Word Cloud](data/images/happiness_wordcloud.png)

### World Happiness Analytics (2015–2024)

This project explores the relationship between happiness and health across countries using data from the **World Happiness Reports** for the years **2015 to 2024**. The analysis aims to uncover how various factors — particularly health and well-being — influence happiness globally.

#### Dataset and Preprocessing Overview

## Notebooks

<details>
  <summary><strong><a href="./notebooks/01_etl_pipeline.ipynb">01_etl_pipeline</a></strong></summary>

This notebook handles the extraction, transformation, and loading (ETL) of happiness report data from 2015 to 2024. It combines and cleans data across 10 years, ensuring consistency and completeness. A final dataset of 131 countries with complete records is created by dropping countries with missing data. Additional feature engineering is performed to prepare the data for further analysis.

</details>

<details>
  <summary><strong><a href="./notebooks/01_descriptive_analysis.ipynb">01_descriptive_analysis</a></strong></summary>

This notebook provides an overview of global happiness trends using descriptive analysis techniques. It includes key visualizations such as scatter plots, area charts, heatmaps, and bar charts. These explore relationships between health, happiness, and other contributing factors. The analysis also highlights differences in happiness patterns across continents and over time.

</details>

<details>
  <summary><strong><a href="./notebooks/03_hypothesis_testing.ipynb">03_hypothesis_testing</a></strong></summary>

This notebook tests specific hypotheses to determine which factors significantly affect happiness. Statistical tests include the Kruskal-Wallis and Mann-Whitney U tests. Variables like family support, life expectancy, generosity, and continent are analyzed. The results provide evidence-based insights into which factors show significant differences in happiness levels.

</details>

### Key Questions Addressed

1. How much does health (life expectancy) contribute to happiness compared to income and freedom?
2. Which countries or regions show the strongest health-related effects on well-being?
3. Can improvements in health predict future happiness?
4. How does social support compare to health and income in influencing happiness?

### Tools Used

- **Python**, **Pandas**, **NumPy**
- **Scikit-learn** for preprocessing
- **Matplotlib**, **Seaborn**, **Plotly** for visualization
- **Jupyter Notebook** for interactive analysis

### Tableau Dashboard

View the interactive dashboard: [Click here](https://public.tableau.com/app/profile/angel.jayakumar/viz/Book2_17521895743850/Whatmakenationshappy)

### Word Cloud Visualization

The word cloud image displayed above was generated using the Python `WordCloud` library. It visually represents countries sized by their happiness rank, where countries with higher happiness appear larger. This visualization helps to quickly identify and compare happiness levels across different countries.

### Directory Structure

### Data Source and Credits

This project uses data from two Kaggle datasets:

- [World Happiness Report 2015–2019](https://www.kaggle.com/datasets/unsdsn/world-happiness?select=2019.csv)
- [World Happiness Report 2020–2024](https://www.kaggle.com/datasets/samithsachidanandan/world-happiness-report-2020-2024)

The original data is based on the **Gallup World Poll**, which surveys over 160 countries and includes key well-being indicators such as happiness score, GDP per capita, social support, healthy life expectancy, and more. All 10 CSV files were cleaned and merged to create a unified dataset for analysis covering the years 2015 to 2024.
