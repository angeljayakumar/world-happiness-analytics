# Alfie's Happiness Predictor App with A/B Testing

## Design Thinking Approach

This app is being developed following the Design Thinking process to keep Alfie’s needs and experience at the center:

- **Empathize:** Understand Alfie’s goal — a curious 9-year-old who loves maths and building things, wanting to explore how different factors affect happiness.
- **Define:** The app helps Alfie predict happiness scores based on features like Economy, Family, Health, Freedom, and Generosity.
- **Ideate:** Two versions of the app are designed:
  - Version A: Minimal UI, simple inputs, straightforward results.
  - Version B: Rich UI with interactive charts, gamified challenges, and detailed explanations.
- **Prototype:** Both versions are built in Streamlit with interactive sliders and prediction features.
- **Test:** A/B testing randomly assigns users to either version to collect feedback and determine which version better engages young users like Alfie.

## User Persona

- Alfie: A 9-year-old who loves maths, Roblox, Minecraft,Football and LEGO.

## App Goal

- Help Alfie explore how factors like Economy, Family, Health, Freedom, and Generosity  
  affect a country's happiness score.
- Make learning fun using maths, gamification, and interactive building blocks.

## Key Features

1. Interactive sliders as “building blocks” of happiness.
2. Predict happiness score using a trained model.
3. Show weighted contributions of each factor (maths behind the score).
4. Gamified “Happiness Builder Challenge” – try to reach a target score by adjusting sliders.
5. Friendly, playful language inspired by Roblox/Minecraft/LEGO.

## Model Details and Prediction Accuracy

The app uses a linear regression model named **`linear_regression_model.pkl`** to predict happiness scores based on input features.

### Model Performance and Selection

We trained two models to predict the Happiness Score based on features like Economy, Family, and Health:

- **Linear Regression Model**

  - Achieved an **R² score of 0.58 (58%)**, meaning it explains 58% of the variation in happiness scores.
  - This indicates it captures most important patterns in the data and provides relatively reliable predictions.

- **Random Forest Model**
  - Achieved an **R² score of 0.53 (53%)**, slightly lower than Linear Regression.
  - It explains less variation in happiness scores for this dataset.

**Decision:**  
We selected the **Linear Regression model** for the app because of its higher R² score (0.58 vs 0.53) and its simplicity, which makes it easier to explain and understand — important for educational use.

**Note:**  
While the model captures over half of the variation, some factors affecting happiness are not included or are unpredictable. Therefore, predictions are approximate and meant to be used as a learning tool rather than exact forecasts.

## A/B Testing Structure

- Version A: Minimal UI with simple inputs and plain prediction results.
- Version B: Rich UI with interactive charts, detailed explanations, gamified challenges.
- Randomly assign users to Version A or B on session start.
- Collect user feedback on satisfaction and suggestions to compare versions.
- Use feedback and usage data to determine which version better engages Alfie and similar users.

## User Experience Focus

- Make app accessible and engaging for young users who love maths and games.
- Encourage exploration and learning through playful interaction.
- Use A/B testing to iteratively improve design based on real user preferences.

## This app combines

- Data science (predictive modelling)
- UX design (child-friendly gamification)
- Analytics (A/B testing and feedback collection)
- Visualization (charts, formulas)
- Educational storytelling (maths + fun building blocks)
