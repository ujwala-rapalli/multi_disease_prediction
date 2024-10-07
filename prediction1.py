# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 17:30:29 2024

@author: raji9
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


 #loading the model
try:
    model1 = pickle.load(open('diabetes_model .sav', 'rb'))
except FileNotFoundError:
    st.error("Diabetes model file not found.")

try:
    model2 = pickle.load(open('heart_disease_model.sav', 'rb'))
except FileNotFoundError:
    st.error("Heart disease model file not found.")

try:
    model3 = pickle.load(open('parkinsons_model.sav', 'rb'))
except FileNotFoundError:
    st.error("Parkinsons model file not found.")

#sidebar
with st.sidebar:
    selected=option_menu('Mutilple Disease prediction system',
                         ['Diabetes Prediction','Heart disease Prediction','Parkinsons prediction'],
                        
                         default_index=0)
    
if(selected=='Diabetes Prediction'):
    #titlepage
    st.title('Diabetes Prediction using ML')
    #getting input from user
    col1,col2,col3=st.columns(3)
    with col1:
        preg=st.text_input('Number of pregancies')
    with col2:
        glucose=st.text_input('Glucose Level')
    with col3:
        bp=st.text_input('Blood Pressure level')
    with col1:
        skin=st.text_input('Skin Thinkness value')
    with col2:
        insulin=st.text_input('Insulin Level')
    with col3:
        bmi=st.text_input('BMI level')
    with col1:
        function=st.text_input('Diabetes pedigree Function value')
    with col2:
        age=st.text_input('Age') 
    
    
  #prediction
    diab_diagnosis=''
    
    #creting a button
    if st.button('Diabetes Test Result'):
        try:
            diab_prediction = model1.predict([[int(preg), float(glucose), float(bp), float(skin), float(insulin), float(bmi), float(function), int(age)]])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is Diabetic'
            else:
                diab_diagnosis = 'The person is NOT Diabetic'
        except ValueError:
            diab_diagnosis = 'Please enter valid numeric values'

    st.success(diab_diagnosis)

    
    
if(selected=='Heart disease Prediction'):
    st.title('Heart disease Prediction using ML')
    #getting user input
    col1,col2,col3=st.columns(3)
    with col1:
        age=st.text_input('Age')
    with col2:
        sex=st.text_input('Sex')
    with col3:
        cp=st.text_input('Chest pain type')
    with col1:
        trestbps=st.text_input('Resting Blood Pressure')
    with col2:
        chol=st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs=st.text_input('Fasting blood sugar > 120 mg/dl')
    with col1:
        restecg=st.text_input('Resting Electrocardiographic Results')
    with col2:
        thalach=st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang=st.text_input('Exercise induced angina')
    with col1:
        oldpeak=st.text_input('Oldpeak')
    with col2:
        slope=st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca=st.text_input('Number of major vessels')
    with col1:
        thal=st.text_input('Thal')
    
    heart_diagnosis=''
    if st.button('Heart disease Test Result'):
        try:
            heart_prediction = model2.predict([[int(age), int(sex), int(cp), float(trestbps), float(chol), int(fbs), int(restecg), float(thalach), int(exang), float(oldpeak), int(slope), int(ca), int(thal)]])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person has Heart Disease'
            else:
                heart_diagnosis = 'The person DOES NOT have Heart Disease'
        except ValueError:
            heart_diagnosis = 'Please enter valid numeric values'

    st.success(heart_diagnosis)
if selected == 'Parkinsons prediction':
    st.title('Parkinsons Prediction using ML')
    col1, col2, col3 = st.columns(3)

    # Input fields with default values set
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)', value=0.0)
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)', value=0.0)
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)', value=0.0)
    with col1:
        jitter = st.number_input('MDVP:Jitter(%)', value=0.0)
    with col2:
        jitter_abs = st.number_input('MDVP:Jitter(Abs)', value=0.0)
    with col3:
        rap = st.number_input('MDVP:RAP', value=0.0)
    with col1:
        ppq = st.number_input('MDVP:PPQ', value=0.0)
    with col2:
        ddp = st.number_input('Jitter:DDP', value=0.0)
    with col3:
        shimmer = st.number_input('MDVP:Shimmer', value=0.0)
    with col1:
        shimmer_db = st.number_input('MDVP:Shimmer(dB)', value=0.0)
    with col2:
        shimmer_apq3 = st.number_input('Shimmer:APQ3', value=0.0)
    with col3:
        shimmer_apq5 = st.number_input('Shimmer:APQ5', value=0.0)
    with col1:
        mdvp_apq = st.number_input('MDVP:APQ', value=0.0)
    with col2:
        shimmer_dda = st.number_input('Shimmer:DDA', value=0.0)
    with col3:
        nhr = st.number_input('NHR', value=0.0)
    with col1:
        hnr = st.number_input('HNR', value=0.0)
    with col2:
        rpde = st.number_input('RPDE', value=0.0)
    with col3:
        dfa = st.number_input('DFA', value=0.0)
    with col1:
        spread1 = st.number_input('Spread1', value=0.0)
    with col2:
        spread2 = st.number_input('Spread2', value=0.0)
    with col3:
        d2 = st.number_input('D2', value=0.0)
    with col1:
        pe = st.number_input('PE', value=0.0)

    parkinsons_diagnosis = ''

    # Prediction button and logic
    if st.button('Parkinsons Test Result'):
        try:
            # Convert input values to a list of features for the model
            input_features = [
                float(fo), float(fhi), float(flo), float(jitter), float(jitter_abs), float(rap),
                float(ppq), float(ddp), float(shimmer), float(shimmer_db), float(shimmer_apq3),
                float(shimmer_apq5), float(mdvp_apq), float(shimmer_dda), float(nhr),
                float(hnr), float(rpde), float(dfa), float(spread1), float(spread2),
                float(d2), float(pe)
            ]
            
            # Model prediction
            parkinsons_prediction = model3.predict([input_features])
            
            # Generate result text
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = 'The person has Parkinson\'s Disease'
            else:
                parkinsons_diagnosis = 'The person DOES NOT have Parkinson\'s Disease'

        except ValueError:
            parkinsons_diagnosis = 'Please enter valid numeric values'
        except Exception as e:
            st.error(f"An error occurred: {e}")

    st.success(parkinsons_diagnosis)

    

 
    
    
        
        
        
        
        
        
        
        
        
