import pandas as pd
import joblib
import streamlit as st

# Load your full dataset with historical data per country
df = pd.read_csv('data/cleaned/winsorized_df_all.csv')

# Load your trained happiness prediction model
model = joblib.load('model/linear_regression_happiness_model.joblib')

st.title("Alfie's Happiness Predictor App")

# Select country from unique list in the dataset
selected_country = st.selectbox('Select a Country', df['Country'].unique())

# Filter dataset for the chosen country
country_data = df[df['Country'] == selected_country]

# Define features you want user to control
features = ['Economy', 'Family', 'Health', 'Freedom', 'Generosity']

input_values = {}

for feature in features:
    min_val = float(country_data[feature].min())
    max_val = float(country_data[feature].max())
    mean_val = float(country_data[feature].mean())
    
    # Slider defaults to the mean value, with range between min and max
    input_values[feature] = st.slider(
        label=f"{feature}",
        min_value=min_val,
        max_value=max_val,
        value=mean_val
    )

# Prepare list of feature inputs for prediction
input_list = [input_values[feature] for feature in features]

# Predict happiness score when button pressed
if st.button('Predict Happiness Score'):
    prediction = model.predict([input_list])[0]
    st.success(f"Predicted Happiness Score for {selected_country}: {prediction:.2f}")





