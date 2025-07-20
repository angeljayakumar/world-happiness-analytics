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

<details>
  <summary><strong>04_diagnostic_analysis</strong></summary>

This notebook explores why India ranks lower in happiness compared to top countries. It shows that India scores less in income, health, and social support—key factors linked to happiness. It also tracks how India’s happiness score dropped from 2015 to 2020 and only partly recovered by 2024. These insights help identify what India needs to improve for better well-being.

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

<details>
<summary>5. Why is India less happy than top-ranked countries?</summary>

India ranks lower in happiness because it scores significantly less in income, healthy life expectancy, and social support compared to top countries like Finland and Denmark. These three factors are closely linked to happiness. The top-performing countries maintain a strong balance across all of them, highlighting where India can focus to improve national well-being.

</details>

<details>
<summary>6. How has India’s happiness changed since 2015?</summary>

India’s happiness score declined from 4.5 in 2015 to around 3.5 in 2020, with the sharpest drop during the COVID-19 pandemic. By 2024, it recovered slightly to about 4.2 but remains below pre-2018 levels. This trend points to lasting effects of socioeconomic challenges that still impact overall happiness.

</details>

### Project Structure and Development Overview

This project is organized into **4 Jupyter notebooks**, each addressing a distinct phase of the India happiness analysis:

- **01_etl_pipeline:** Handles data extraction, cleaning, and feature engineering to prepare a comprehensive dataset from 2015 to 2024.
- **02_descriptive_analysis:** Performs exploratory data analysis with visualizations to reveal global happiness trends and factor relationships.
- **03_hypothesis_testing:** Applies statistical tests to identify significant factors influencing happiness across different regions and groups.
- **04_diagnostic_analysis:** Focuses on diagnosing India’s lower happiness scores by benchmarking and trend analysis over time.

Each notebook was developed in its own **feature branch**, enabling modular, focused development and easier collaboration. This approach ensures clear separation of tasks and smooth integration of different analysis components.

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
