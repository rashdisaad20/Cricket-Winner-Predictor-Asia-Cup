import streamlit as st     
import pandas as pd   
import pickle     




# Loading data      
with open("cricket_model.pkl", "rb") as f:
    data = pickle.load(f)

model = data["model"]
encoders = data["encoders"]
target_encoder = data["target_encoder"]







# Streamlit UI

st.title("Asia Cup Match Winner Predictor")
st.subheader("Predict the winning team based on match details")


# Input feilds 

team1 = st.selectbox("team1", encoders['Team1'].classes_)
team2 = st.selectbox("Team2", encoders['Team2'].classes_)
venue = st.selectbox("Venue", encoders['Venue'].classes_)
match_type = st.selectbox("Match Type", encoders['Match_Type'].classes_)
year = st.number_input("Year", min_value=2000, max_value=2030, value=2022)




# Predict button 

if st.button("Predict Winner"):
    input_data = {
        "Team1": team1,
        "Team2": team2,
        "Venue": venue,
        "Match_Type": match_type,
        "Year": year,
    }


# Converting into DataFrame
input_df = pd.DataFrame([input_data])






for col in input_df.columns:
    if col in encoders:
        input_df[col] = encoders[col].transform(input_df[col])


# Make prediction 

prediction = model.predict(input_df)[0]
prediction_team = target_encoder.inverse_transform([prediction])[0]

# output 
st.success(f"Predicted Winner:  {prediction_team}**")