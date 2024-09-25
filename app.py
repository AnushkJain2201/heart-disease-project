import streamlit as st
import pickle
import numpy as np
import sklearn

# Load the trained model
loaded_model = pickle.load(open("saved_models/log_reg.pkl", "rb"))

# Creating a function for prediction
def predict_heart_disease(input_data):
    # Changing the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # Reshaping the input data to match the expected input shape of the model
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    
    # Making a prediction using the loaded model
    prediction = loaded_model.predict(input_data_reshaped)
    
    print(prediction)
    
    if(prediction[0] == 0):
        return "NO HEART DISEASE"
    else:
        return "YES, THE PERSON HAS HEART DISEASE"


def main():
    
    # Giving a title
    st.title("Heart Disease Prediction App")
    
    # Getting the input data from the user
    # age	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal
    age = st.number_input("Age", min_value=0, max_value=100)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
    trestbps = st.number_input("Resting Blood Pressure", min_value=0, max_value=200)
    chol = st.number_input("Serum Cholesterol", min_value=0, max_value=600)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
    restecg = st.selectbox("Resting ECG Results", ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0, max_value=200)
    exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
    oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest", min_value=0.0, max_value=10.0, step=0.1, format="%.1f")
    slope = st.selectbox("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
    ca = st.number_input("Number of Major Vessels Colored by Flourosopy", min_value=0, max_value=3)
    thal = st.selectbox("Thal", ["Normal", "Fixed Defect", "Reversible Defect"])
    
    # Code for predictions
    diagnosis = ""
    if st.button("Predict"):
        # age = str(age)
        
        if sex == "Male":
            sex = 0
        elif sex == "Female":
            sex = 1
        
        if cp == "Typical Angina":
            cp = 0
        elif cp == "Atypical Angina":
            cp = 1
        elif cp == "Non-Anginal Pain":
            cp = 2
        elif cp == "Asymptomatic":
            cp = 3
            
        # trestbps = str(trestbps)
        
        # chol = str(chol)
            
        if fbs == "No":
            fbs = 0
        elif fbs == "Yes":
            fbs = 1
        
        if restecg == "Normal":
            restecg = 0
        elif restecg == "ST-T Wave Abnormality":
            restecg = 1
        elif restecg == "Left Ventricular Hypertrophy":
            restecg = 2
            
        # thalach = str(thalach)
        
        if exang == "No":
            exang = 0
        elif exang == "Yes":
            exang = 1
            
        # oldpeak = str(oldpeak)
            
        if slope == "Upsloping":
            slope = 0
        elif slope == "Flat":
            slope = 1
        elif slope == "Downsloping":
            slope = 2
            
        # ca = str(ca)
            
        if thal == "Normal":
            thal = 0
        elif thal == "Fixed Defect":
            thal = 1
        elif thal == "Reversible Defect":
            thal = 2
        
        input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        diagnosis = predict_heart_disease(input_data)
        
    st.success(diagnosis)
    
    
if __name__ == "__main__":
    main()