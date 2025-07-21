<h1 style="color:#C71585;">World Happiness Analytics (2015–2024)</h1>

This project explores World Happiness Report data from 2015 to 2024 to understand how health and family support influence national happiness. It covers data cleaning, visual analysis in Tableau, and statistical testing. A predictive model is also built to explore future trends. The project includes an interactive Streamlit app to make insights more accessible and engaging.

![Happiness Word Cloud](data/images/happiness_wordcloud.png)

<h3 style="color:#C71585;">Column Descriptions</h3>

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

<h3 style="color:#C71585;">Project Structure and Development Overview</h3>

This project is organized into **5 Jupyter notebooks**, each addressing a distinct phase of happiness analysis:

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

<details>
  <summary><strong>05_predictive_analysis</strong></summary>

This notebook builds a model to predict future happiness scores of countries using data from 2015 to 2024. It includes data cleaning, creating lag features to capture past trends, and training models like Linear Regression and Random Forest. The notebook evaluates model performance and saves the Linear Regression model for future use. This helps forecast happiness trends and supports informed decision-making.

</details>

### Branches

This project is developed using feature branches for modular and organized development. The main branches are:

- `main` — The main production branch containing the stable, integrated code.
- `happyblazer-etl-pipeline` — Handles data extraction, transformation, and loading (ETL) of the happiness report data.
- `happyblazer-descriptive-analysis` — Contains notebooks and scripts for descriptive and exploratory data analysis.
- `happyblazer-hypothesis-testing` — Dedicated to statistical testing and hypothesis validation.
- `happyblazer-diagnostic-analysis` — Focuses on diagnostic analysis, including case studies like India's happiness trends.
- `happyblazer-predictive--analysis` — Contains the predictive modeling work, including data preprocessing, lag feature creation, model training, evaluation, and saving the Linear Regression model.

<h3 style="color:#C71585;">Key Questions Addressed</h3>

<details>
<summary><span style="font-weight: bold; font-size: 1.2em;">1. How does health (life expectancy) relate to world happiness?</span></summary>
<span style="font-size: 0.95em; font-family: 'Times New Roman', Times, serif;">
There is a strong positive correlation between healthy life expectancy and happiness scores across countries from 2015 to 2024. Countries with higher life expectancy generally report higher happiness levels. European nations tend to show both high life expectancy and happiness, while many African countries fall into the lower ranges. This suggests that improving health outcomes could be an effective way to increase national well-being.
</span>
</details>

<details>
<summary><span style="font-weight: bold; font-size: 1.2em;">2. How has world happiness changed over time (2015–2024)?</span></summary>
<span style="font-size: 0.95em; font-family: 'Times New Roman', Times, serif;">
Nordic countries like Finland, Denmark, Norway, and Sweden consistently rank among the happiest globally with stable scores. Their resilience reflects strong social systems and quality of life, even during crises such as the COVID-19 pandemic. Conversely, countries like Afghanistan and many Sub-Saharan African nations remain at the lowest happiness levels. India’s happiness scores fluctuate but generally stay in the lower-middle range, indicating ongoing challenges.
</span>
</details>

<details>
<summary><span style="font-weight: bold; font-size: 1.2em;">3. Which factors most strongly influence world happiness?</span></summary>
<span style="font-size: 0.95em; font-family: 'Times New Roman', Times, serif;">
Family and social connections show the strongest positive correlation with happiness at 0.82, highlighting their importance. Economic prosperity (GDP per capita) closely follows with a correlation of 0.81. Healthy life expectancy is also a major contributor with a correlation of 0.79. Perceptions of corruption negatively impact happiness, while generosity has only a weak positive correlation.
</span>
</details>

<details>
<summary><span style="font-weight: bold; font-size: 1.2em;">4. Do certain factors lead to statistically significant differences in world happiness?</span></summary>
<span style="font-size: 0.95em; font-family: 'Times New Roman', Times, serif;">
Statistical tests reveal that family support and life expectancy affect happiness levels. These factors show clear differences in average happiness scores between groups. Generosity, despite being positively viewed, does not have a significant statistical impact on happiness. This underscores the key role of social and health factors in well-being.
</span>
</details>

<details>
<summary><span style="font-weight: bold; font-size: 1.2em;">5. If India is a happy place, why does it rank lower than top countries like Finland?</span></summary>
<span style="font-size: 0.95em; font-family: 'Times New Roman', Times, serif;">
India is a happy place in many ways — people often find joy in family, traditions, festivals, and strong community bonds. However, the World Happiness Report measures happiness using factors like income, healthy life expectancy, social support, and perceived freedom. Compared to top-ranked countries such as Finland and Denmark, India scores lower in these areas. In addition, India’s large population combined with deep economic and social inequality affects access to basic services and opportunities, which lowers the average national well-being score. So while many individuals may feel personally happy, the overall ranking reflects broader structural challenges that need to be addressed.
</span>
</details>

<details>
<summary><span style="font-weight: bold; font-size: 1.2em;">6. How has India’s happiness changed since 2015?</span></summary>
<span style="font-size: 0.95em; font-family: 'Times New Roman', Times, serif;">
India’s happiness score declined from 4.5 in 2015 to around 3.5 in 2020, with the sharpest drop during the COVID-19 pandemic. By 2024, it had slightly recovered to about 4.2 but still remains below pre-2018 levels. This downward trend highlights how large-scale socioeconomic challenges, such as inequality, unemployment, and healthcare access, continue to affect the nation’s overall happiness.
</span>
</details>

<h3 style="color:#C71585;">Tools Used</h3>

- **Python** for data processing and modeling
- **Pandas** and **NumPy** for data cleaning, manipulation, and numerical operations
- **Matplotlib**, **Seaborn**, and **Plotly** for data visualization and exploratory data analysis
- **OneHotEncoder** from scikit-learn for encoding categorical variables
- **Scikit-learn** for building and evaluating predictive models (Linear Regression, Random Forest)
- **StandardScaler** for feature scaling
- **SharpWalk** to guide selection between parametric and non-parametric statistical tests for hypothesis analysis
- **Joblib** for saving/loading models

<h3 style="color:#C71585;">Analysis Used</h3>

- **Exploratory Data Analysis (EDA)** with visualizations
- **Feature Engineering** including lag features to capture temporal trends
- **Predictive Modeling** using regression and ensemble methods
- **Model Evaluation** using metrics like R² Score and Mean Squared Error (MSE)
- **Hypothesis Testing** decision support guided by SharpWalk

This combination of tools and analysis techniques supports thorough understanding and forecasting of country happiness scores using data from 2015 to 2024.

<h3 style="color:#C71585;">Tableau Dashboard</h3>

View the interactive dashboard: [Click here](https://public.tableau.com/app/profile/angel.jayakumar/viz/Book2_17521895743850/Whatmakenationshappy)

<h3 style="color:#C71585;">Word Cloud Visualization</h3>

The word cloud image displayed above was generated using the Python `WordCloud` library. It visually represents countries sized by their happiness rank, where countries with higher happiness appear larger. This visualization helps to quickly identify and compare happiness levels across different countries.

<h3 style="color:#C71585;">Data Source and Credits</h3>

This project uses data from two Kaggle datasets:

- [World Happiness Report 2015–2019](https://www.kaggle.com/datasets/unsdsn/world-happiness?select=2019.csv)
- [World Happiness Report 2020–2024](https://www.kaggle.com/datasets/samithsachidanandan/world-happiness-report-2020-2024)

The original data is based on the **Gallup World Poll**, which surveys over 160 countries and includes key well-being indicators such as happiness score, GDP per capita, social support, healthy life expectancy, and more. All 10 CSV files were cleaned and merged to create a unified dataset for analysis covering the years 2015 to 2024.
