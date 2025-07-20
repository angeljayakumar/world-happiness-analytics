## World Happiness Analytics (2015–2024)

This project explores World Happiness Report data from 2015 to 2024 to understand how health and family support influence national happiness. It covers data cleaning, visual analysis in Tableau, and statistical testing. A predictive model is also built to explore future trends. The project includes an interactive Streamlit app to make insights more accessible and engaging.

![Happiness Word Cloud](data/images/happiness_wordcloud.png)

### Column Descriptions

<details>
  <summary>Click to view Column descriptions</summary>

| **Column Name**                 | **Explanation**                                                                |
| ------------------------------- | ------------------------------------------------------------------------------ |
| `Country`                       | Name of the country                                                            |
| `Happiness Rank`                | Country’s position in the global happiness ranking for that year               |
| `Happiness Score`               | Overall happiness score based on survey data and contributing factors          |
| `Economy`                       | Contribution of GDP per capita to the happiness score                          |
| `Family`                        | Level of social support and family connections (based on survey responses)     |
| `Healthy life expectancy`       | Expected number of years a person can live in good health, starting from birth |
| `Freedom to make life choices`  | Level of freedom individuals feel in making life decisions                     |
| `Perceptions of corruption`     | Public perception of corruption in government and business                     |
| `Generosity`                    | Willingness to donate to others, based on survey data and donations            |
| `Continent`                     | Continent the country belongs to (added for regional analysis)                 |
| `Year`                          | Year the data was collected (2015–2024)                                        |
| `Happiness Rank (Cleaned Data)` | Adjusted rank after cleaning and standardizing the dataset                     |

</details>

### Notebooks

<details>
  <summary><strong>01_etl_pipeline</strong></summary>

This notebook handles the extraction, transformation, and loading (ETL) of happiness report data from 2015 to 2024. It combines and cleans data across 10 years, ensuring consistency and completeness. A final dataset of 131 countries with complete records is created by dropping countries with missing data. Additional feature engineering is performed to prepare the data for further analysis.

</details>

<details>
  <summary><strong>02_descriptive_analysis</strong></summary>

This notebook provides an overview of global happiness trends using descriptive analysis techniques. It includes key visualizations such as scatter plots, area charts, heatmaps, and bar charts. These explore relationships between health, happiness, and other contributing factors. The analysis also highlights differences in happiness patterns across continents and over time.

</details>

<details>
  <summary><strong>03_hypothesis_testing</strong></summary>

This notebook tests specific hypotheses to determine which factors significantly affect happiness. Statistical tests include the Kruskal-Wallis and Mann-Whitney U tests. Variables like family support, life expectancy, generosity, and continent are analyzed. The results provide evidence-based insights into which factors show significant differences in happiness levels.

</details>

### Key Questions Addressed

<details>
<summary>1. How does health (life expectancy) relate to happiness?</summary>

There is a strong positive correlation between healthy life expectancy and happiness scores across countries from 2015 to 2024. Countries with higher life expectancy generally report higher happiness levels. European nations tend to show both high life expectancy and happiness, while many African countries fall into the lower ranges. This suggests that improving health outcomes could be an effective way to increase national well-being.

</details>

<details>
<summary>2. How has happiness changed over time (2015–2024)?</summary>

Nordic countries like Finland, Denmark, Norway, and Sweden consistently rank among the happiest globally with stable scores. Their resilience reflects strong social systems and quality of life, even during crises such as the COVID-19 pandemic. Conversely, countries like Afghanistan and many Sub-Saharan African nations remain at the lowest happiness levels. India’s happiness scores fluctuate but generally stay in the lower-middle range, indicating ongoing challenges.

</details>

<details>
<summary>3. Which factors most strongly influence happiness?</summary>

Family and social connections show the strongest positive correlation with happiness at 0.82, highlighting their importance. Economic prosperity (GDP per capita) closely follows with a correlation of 0.81. Healthy life expectancy is also a major contributor with a correlation of 0.79. Perceptions of corruption negatively impact happiness, while generosity has only a weak positive correlation.

</details>

<details>
<summary>4. Do certain factors lead to statistically significant differences in happiness?</summary>

Statistical tests reveal that family support and life expectancy affect happiness levels. These factors show clear differences in average happiness scores between groups. Generosity, despite being positively viewed, does not have a significant statistical impact on happiness. This underscores the key role of social and health factors in well-being.

</details>

### Tools Used

- **Python**, **Pandas**, **NumPy**
- **Scikit-learn** for preprocessing
- **Matplotlib**, **Seaborn**, **Plotly** for visualization
- **Jupyter Notebook** for interactive analysis

### Tableau Dashboard

View the interactive dashboard: [Click here](https://public.tableau.com/app/profile/angel.jayakumar/viz/Book2_17521895743850/Whatmakenationshappy)

### Word Cloud Visualization

The word cloud image displayed above was generated using the Python `WordCloud` library. It visually represents countries sized by their happiness rank, where countries with higher happiness appear larger. This visualization helps to quickly identify and compare happiness levels across different countries.

### Data Source and Credits

This project uses data from two Kaggle datasets:

- [World Happiness Report 2015–2019](https://www.kaggle.com/datasets/unsdsn/world-happiness?select=2019.csv)
- [World Happiness Report 2020–2024](https://www.kaggle.com/datasets/samithsachidanandan/world-happiness-report-2020-2024)

The original data is based on the **Gallup World Poll**, which surveys over 160 countries and includes key well-being indicators such as happiness score, GDP per capita, social support, healthy life expectancy, and more. All 10 CSV files were cleaned and merged to create a unified dataset for analysis covering the years 2015 to 2024.
