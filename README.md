This project analyzes the World Happiness Report data to understand how health and family contribute to national happiness. It includes data cleaning, visualization in Tableau, a predictive model, and an interactive Streamlit app.

![Happiness Word Cloud](data/images/happiness_wordcloud.png)

# 🌍 World Happiness Analytics (2015–2024)

This project explores the relationship between happiness and health across countries using data from the **World Happiness Reports** for the years **2015 to 2024**. The analysis aims to uncover how various factors — particularly health and well-being — influence happiness globally.

# Dataset and Preprocessing Overview

The dataset covers World Happiness data from 2015 to 2024, including all original columns.

Explored the dataset thoroughly and dropped the columns “Uncertainty” and “Dystopia” as they were not relevant to my analysis.

Created a custom analysis model based on the cleaned data.

Not all countries have data for all 10 years; I dropped some countries and finalized the dataset to include 131 countries.

Added a new column “Continent” to group countries by region.

Created a new column “Year” to track the data year.

Recalculated and created “Happiness Rank (Cleaned Data)” since original ranks became inconsistent after dropping countries.

This cleaned and structured dataset is ready for further analysis and modeling.

## 🧪 Key Questions Addressed

1. How much does health (life expectancy) contribute to happiness compared to income and freedom?
2. Which countries or regions show the strongest health-related effects on well-being?
3. Can improvements in health predict future happiness?
4. How does social support compare to health and income in influencing happiness?

## 🛠️ Tools Used

- **Python**, **Pandas**, **NumPy**
- **Scikit-learn** for preprocessing
- **Matplotlib**, **Seaborn**, **Plotly** for visualization
- **Jupyter Notebook** for interactive analysis

## 📊 Tableau Dashboard

View the interactive dashboard: [Click here](https://public.tableau.com/app/profile/angel.jayakumar/viz/Book2_17521895743850/Whatmakenationshappy)

## Word Cloud Visualization

The word cloud image displayed above was generated using the Python `WordCloud` library. It visually represents countries sized by their happiness rank, where countries with higher happiness appear larger. This visualization helps to quickly identify and compare happiness levels across different countries.

## 📁 Directory Structure
