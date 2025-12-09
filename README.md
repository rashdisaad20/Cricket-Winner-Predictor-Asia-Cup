





# **Cricket Match Winner Predictor (Asia Cup)**
A machine learning web application that predicts the **winner of a cricket match** using historical Asia Cup data.  
Built with **Python, Random Forest Classifier, and Streamlit**.

---

##  **Project Overview**
This project uses machine learning to predict the outcome of a cricket match based on:

- Team 1  
- Team 2  
- Venue  
- Match Type (ODI or T20)  
- Year  

The app is interactive and deployed using **Streamlit**, allowing anyone to input match details and instantly get a predicted winner.

---

##  **Features**
- ✔ Predict match winner in real-time  
- ✔ Clean and simple Streamlit UI  
- ✔ Random Forest model trained on Asia Cup dataset  
- ✔ Handles categorical feature encoding  
- ✔ Ready for online deployment (Streamlit Cloud / HF Spaces)

---

##  **Machine Learning Pipeline**

### **1. Data Preprocessing**
- Loaded the Asia Cup dataset  
- Selected useful features: Team1, Team2, Venue, Match_Type, Year  
- Used `LabelEncoder` for categorical encoding  

### **2. Model Training**
Algorithm used:  
- **RandomForestClassifier**  
Trained and saved using:  
- `pickle` → `cricket_model.pkl`  

### **3. Deployment**
The trained model is integrated into a Streamlit app.

---


## **Project Structure** 
- app.py   # Streamlit Web app
- cricket_model.pkl   # Trained ML model
- asia_cup_dataset.csv  # Dataset
- requirments.txt   # Requirments
- README.md    # Documentation

## 📂 Project Structure

