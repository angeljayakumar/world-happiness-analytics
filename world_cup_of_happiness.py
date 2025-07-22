import streamlit as st
import random

# Country data with happiness scores and flags
# Country list with happiness scores from World Happiness Report
countries_data = {
    "Afghanistan": 2.864,
    "Albania": 4.934,
    "Algeria": 5.405,
    "Argentina": 6.238,
    "Armenia": 4.812,
    "Australia": 7.21,
    "Austria": 7.143,
    "Bahrain": 6.222,
    "Bangladesh": 4.608,
    "Belgium": 6.886,
    "Benin": 4.314,
    "Bolivia": 5.76,
    "Bosnia and Herzegovina": 5.457,
    "Botswana": 3.639,
    "Brazil": 6.469,
    "Bulgaria": 4.976,
    "Burkina Faso": 4.383,
    "Cambodia": 4.408,
    "Cameroon": 4.86,
    "Canada": 7.197,
    "Chad": 4.191,
    "Chile": 6.422,
    "China": 5.393,
    "Colombia": 6.098,
    "Congo": 4.798,
    "Costa Rica": 6.997,
    "Croatia": 5.687,
    "Cyprus": 5.947,
    "Czechia": 6.774,
    "Denmark": 7.581,
    "Dominican Republic": 5.436,
    "Ecuador": 5.847,
    "Egypt": 4.274,
    "El Salvador": 6.174,
    "Estonia": 5.964,
    "Ethiopia": 4.277,
    "Finland": 7.671,
    "France": 6.588,
    "Gabon": 4.682,
    "Georgia": 4.652,
    "Germany": 6.953,
    "Ghana": 4.669,
    "Greece": 5.481,
    "Guatemala": 6.325,
    "Guinea": 4.419,
    "Honduras": 5.609,
    "Hong Kong": 5.43,
    "Hungary": 5.678,
    "Iceland": 7.522,
    "India": 4.075,
    "Indonesia": 5.298,
    "Iran": 4.752,
    "Iraq": 4.732,
    "Ireland": 6.979,
    "Israel": 7.218,
    "Italy": 6.218,
    "Ivory Coast": 4.727,
    "Jamaica": 5.79,
    "Japan": 5.967,
    "Jordan": 4.738,
    "Kazakhstan": 5.997,
    "Kenya": 4.493,
    "Kosovo": 6.012,
    "Kyrgyzstan": 5.452,
    "Latvia": 5.899,
    "Lebanon": 4.316,
    "Liberia": 4.181,
    "Lithuania": 6.215,
    "Luxembourg": 7.1,
    "Madagascar": 3.969,
    "Malawi": 3.722,
    "Malaysia": 5.798,
    "Mali": 4.346,
    "Malta": 6.514,
    "Mauritania": 4.375,
    "Mauritius": 5.847,
    "Mexico": 6.555,
    "Moldova": 5.766,
    "Mongolia": 5.358,
    "Montenegro": 5.457,
    "Morocco": 5.063,
    "Myanmar": 4.377,
    "Nepal": 5.037,
    "Netherlands": 7.407,
    "New Zealand": 7.249,
    "Nicaragua": 6.096,
    "Niger": 4.457,
    "Nigeria": 4.953,
    "North Macedonia": 5.184,
    "Norway": 7.457,
    "Pakistan": 5.107,
    "Palestinian Territories": 4.702,
    "Panama": 6.41,
    "Paraguay": 5.697,
    "Peru": 5.721,
    "Philippines": 5.63,
    "Poland": 6.108,
    "Portugal": 5.638,
    "Romania": 6.031,
    "Russia": 5.692,
    "Saudi Arabia": 6.436,
    "Senegal": 4.695,
    "Serbia": 5.729,
    "Sierra Leone": 4.053,
    "Singapore": 6.506,
    "Slovakia": 6.227,
    "Slovenia": 6.228,
    "South Africa": 4.903,
    "South Korea": 5.909,
    "Spain": 6.398,
    "Sri Lanka": 4.332,
    "Sweden": 7.343,
    "Switzerland": 7.45,
    "Taiwan": 6.458,
    "Tajikistan": 5.25,
    "Tanzania": 3.561,
    "Thailand": 6.113,
    "Togo": 3.848,
    "Tunisia": 4.606,
    "Turkey": 5.149,
    "Uganda": 4.257,
    "Ukraine": 4.6,
    "United Arab Emirates": 6.695,
    "United Kingdom": 6.926,
    "United States": 6.948,
    "Uruguay": 6.461,
    "Uzbekistan": 6.094,
    "Venezuela": 5.334,
    "Vietnam": 5.382,
    "Zambia": 4.2,
    "Zimbabwe": 3.602
}

# Mapping country names to flag emojis
flag_emojis = {
    "Afghanistan": "🇦🇫",
    "Albania": "🇦🇱",
    "Algeria": "🇩🇿",
    "Argentina": "🇦🇷",
    "Armenia": "🇦🇲",
    "Australia": "🇦🇺",
    "Austria": "🇦🇹",
    "Bahrain": "🇧🇭",
    "Bangladesh": "🇧🇩",
    "Belgium": "🇧🇪",
    "Benin": "🇧🇯",
    "Bolivia": "🇧🇴",
    "Bosnia and Herzegovina": "🇧🇦",
    "Botswana": "🇧🇼",
    "Brazil": "🇧🇷",
    "Bulgaria": "🇧🇬",
    "Burkina Faso": "🇧🇫",
    "Cambodia": "🇰🇭",
    "Cameroon": "🇨🇲",
    "Canada": "🇨🇦",
    "Chad": "🇹🇩",
    "Chile": "🇨🇱",
    "China": "🇨🇳",
    "Colombia": "🇨🇴",
    "Congo": "🇨🇬",
    "Costa Rica": "🇨🇷",
    "Croatia": "🇭🇷",
    "Cyprus": "🇨🇾",
    "Czechia": "🇨🇿",
    "Denmark": "🇩🇰",
    "Dominican Republic": "🇩🇴",
    "Ecuador": "🇪🇨",
    "Egypt": "🇪🇬",
    "El Salvador": "🇸🇻",
    "Estonia": "🇪🇪",
    "Ethiopia": "🇪🇹",
    "Finland": "🇫🇮",
    "France": "🇫🇷",
    "Gabon": "🇬🇦",
    "Georgia": "🇬🇪",
    "Germany": "🇩🇪",
    "Ghana": "🇬🇭",
    "Greece": "🇬🇷",
    "Guatemala": "🇬🇹",
    "Guinea": "🇬🇳",
    "Honduras": "🇭🇳",
    "Hong Kong": "🇭🇰",
    "Hungary": "🇭🇺",
    "Iceland": "🇮🇸",
    "India": "🇮🇳",
    "Indonesia": "🇮🇩",
    "Iran": "🇮🇷",
    "Iraq": "🇮🇶",
    "Ireland": "🇮🇪",
    "Israel": "🇮🇱",
    "Italy": "🇮🇹",
    "Ivory Coast": "🇨🇮",
    "Jamaica": "🇯🇲",
    "Japan": "🇯🇵",
    "Jordan": "🇯🇴",
    "Kazakhstan": "🇰🇿",
    "Kenya": "🇰🇪",
    "Kosovo": "🇽🇰",
    "Kyrgyzstan": "🇰🇬",
    "Latvia": "🇱🇻",
    "Lebanon": "🇱🇧",
    "Liberia": "🇱🇷",
    "Lithuania": "🇱🇹",
    "Luxembourg": "🇱🇺",
    "Madagascar": "🇲🇬",
    "Malawi": "🇲🇼",
    "Malaysia": "🇲🇾",
    "Mali": "🇲🇱",
    "Malta": "🇲🇹",
    "Mauritania": "🇲🇷",
    "Mauritius": "🇲🇺",
    "Mexico": "🇲🇽",
    "Moldova": "🇲🇩",
    "Mongolia": "🇲🇳",
    "Montenegro": "🇲🇪",
    "Morocco": "🇲🇦",
    "Myanmar": "🇲🇲",
    "Nepal": "🇳🇵",
    "Netherlands": "🇳🇱",
    "New Zealand": "🇳🇿",
    "Nicaragua": "🇳🇮",
    "Niger": "🇳🇪",
    "Nigeria": "🇳🇬",
    "North Macedonia": "🇲🇰",
    "Norway": "🇳🇴",
    "Pakistan": "🇵🇰",
    "Palestinian Territories": "🇵🇸",
    "Panama": "🇵🇦",
    "Paraguay": "🇵🇾",
    "Peru": "🇵🇪",
    "Philippines": "🇵🇭",
    "Poland": "🇵🇱",
    "Portugal": "🇵🇹",
    "Romania": "🇷🇴",
    "Russia": "🇷🇺",
    "Saudi Arabia": "🇸🇦",
    "Senegal": "🇸🇳",
    "Serbia": "🇷🇸",
    "Sierra Leone": "🇸🇱",
    "Singapore": "🇸🇬",
    "Slovakia": "🇸🇰",
    "Slovenia": "🇸🇮",
    "South Africa": "🇿🇦",
    "South Korea": "🇰🇷",
    "Spain": "🇪🇸",
    "Sri Lanka": "🇱🇰",
    "Sweden": "🇸🇪",
    "Switzerland": "🇨🇭",
    "Taiwan": "🇹🇼",
    "Tajikistan": "🇹🇯",
    "Tanzania": "🇹🇿",
    "Thailand": "🇹🇭",
    "Togo": "🇹🇬",
    "Tunisia": "🇹🇳",
    "Turkey": "🇹🇷",
    "Uganda": "🇺🇬",
    "Ukraine": "🇺🇦",
    "United Arab Emirates": "🇦🇪",
    "United Kingdom": "🇬🇧",
    "United States": "🇺🇸",
    "Uruguay": "🇺🇾",
    "Uzbekistan": "🇺🇿",
    "Venezuela": "🇻🇪",
    "Vietnam": "🇻🇳",
    "Zambia": "🇿🇲",
    "Zimbabwe": "🇿🇼"
}

all_countries = list(countries_data.keys())

st.set_page_config(page_title="Happy Kids Flag Games 🎉", page_icon="🌍")

st.title("🌟 Happy Kids Flag Games 🌟")
game_choice = st.radio("Choose a game:", ["🎯 Happy Flag Game", "🎌 Guess the Flag"])

# -------------------------------
# 🎯 GAME 1: Happy Score Game
# -------------------------------
if game_choice == "🎯 Happy score Game":
    st.header("🎯 How Happy is this Country?")
    st.write("Move the sliders and guess how happy people are!")

    country = st.selectbox("Choose a country:", sorted(countries_data.keys()))

    family = st.slider("Family & Friends (How much love and support?)", 0.0, 1.0, 0.5)
    economy = st.slider("Money & Jobs (How good is the economy?)", 0.0, 1.0, 0.5)
    health = st.slider("Health & Life (How healthy do people live?)", 0.0, 1.0, 0.5)

    if st.button("🧠 Make a Guess!"):
        predicted = (0.4 * family + 0.35 * economy + 0.25 * health) * 10
        predicted = round(min(max(predicted, 0), 10), 2)
        actual = countries_data[country]
        flag = flag_emojis.get(country, "")

        st.markdown(f"## {flag} {country}")
        st.write(f"**Your Happiness Guess:** {predicted} / 10")
        st.write(f"**Real Happiness Score:** {actual} / 10")

        diff = abs(predicted - actual)
        if diff < 1:
            st.balloons()
            st.success("🎉 Amazing! You were very close!")
        elif diff < 3:
            st.info("😊 Good guess! You're getting there.")
        else:
            st.warning("🤔 Keep trying! Adjust the sliders to guess better.")

        st.write("🔁 Change the country or sliders to guess again!")

# -------------------------------
# 🎌 GAME 2: Guess the Country by Flag
# -------------------------------
else:
    st.header("🎌 Guess the Country from the Flag!")
    st.write("Look at the flag and pick the correct country name!")

    if "target_country" not in st.session_state:
        st.session_state.target_country = random.choice(all_countries)

    if "choices" not in st.session_state:
        wrong = random.sample([c for c in all_countries if c != st.session_state.target_country], 3)
        st.session_state.choices = wrong + [st.session_state.target_country]
        random.shuffle(st.session_state.choices)

    flag = flag_emojis[st.session_state.target_country]
    st.markdown(f"### What country is this? {flag}")
    user_guess = st.radio("Pick one:", st.session_state.choices)

    if st.button("✅ Guess!"):
        if user_guess == st.session_state.target_country:
            st.success("🎉 Yay! You got it right!")
            st.balloons()
        else:
            st.error(f"Oops! It's actually **{st.session_state.target_country}**.")

        if st.button("🔄 Play Again"):
            st.session_state.target_country = random.choice(all_countries)
            wrong = random.sample([c for c in all_countries if c != st.session_state.target_country], 3)
            st.session_state.choices = wrong + [st.session_state.target_country]
            random.shuffle(st.session_state.choices)
            st.experimental_rerun()
