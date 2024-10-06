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
    diab_dignosis=''
    
    #creting a button
    if st.button('Diabetes Test Result'):
        diab_prediction=model1.predict([[preg,glucose,bp,skin,insulin,bmi,function,age]])
        if(diab_prediction[0]==1):
            diab_dignosis='The person is Diabetic'
        else:
            diab_dignosis='The person is NOT Diabetic'
    st.success(diab_dignosis)
    
    
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
    
    heart_dignosis=''
    if st.button('Heart disease Test Result'):
        heart_prediction=model2.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if(heart_prediction[0]==1):
            heart_dignosis='The person have Heart Disease'
        else:
            heart_dignosis='The person DOES NOT have Heart Disease'
    st.success(heart_dignosis)
    
if(selected=='Parkinsons prediction'):
    st.title('Parkinsons prediction using ML')
    col1,col2,col3=st.columns(3)
    with col1:
        fo=st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi=st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo=st.text_input('MDVP:Flo(Hz)')
    with col1:
        Jitter=st.text_input('MDVP:Jitter(%)')
    with col2:
        Jitter_Abs=st.text_input('MDVP:Jitter(Abs)')
    with col3:
        rap=st.text_input('MDVP:RAP')
    with col1:
        ppq=st.text_input('MDVP:PPQ')
    with col2:
        ddp=st.text_input('Jitter:DDP')
    with col3:
        Shimmer=st.text_input('MDVP:Shimmer')
    with col1:
        Shimmer_db=st.text_input('MDVP:Shimmer(dB)')
    with col2:
        Shimmer_APQ3=st.text_input('Shimmer:APQ3')
    with col3:
        Shimmer_APQ5=st.text_input('Shimmer:APQ5')
    with col1:
        MDVP_APQ=st.text_input('MDVP:APQ')
    with col2:
        Shimmer_DDA=st.text_input('Shimmer:DDA')
    with col3:
        NHR=st.text_input('NHR')
    with col1:
        HNR=st.text_input('HNR')
    with col2:
        rpde=st.text_input('RPDE')
    with col3:
        dfa=st.text_input('DFA')
    with col1:
        spread1=st.text_input('spread1')
    with col2:
        spread2=st.text_input('spread2')
    with col3:
        d2=st.text_input('D2')
    with col1:
        pe=st.text_input('PE')
        
    parkinsons_dignosis=''
    if st.button('Parkinsons Test Result'):
        parkinsons_prediction=model3.predict([[fo,fhi,flo,Jitter,rap,ppq,ddp,Shimmer,Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,
             Shimmer_DDA,NHR,HNR,rpde,dfa,spread1,spread2,d2,pe]])
        if(parkinsons_prediction[0]==1):
            parkinsons_dignosis='The person have Heart Disease'
        else:
            parkinsons_dignosis='The person DOES NOT have Heart Disease'
    st.success(parkinsons_dignosis)
    
    
        
        
        
        
        
        
        
        
        
