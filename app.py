# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import pickle

pickle_in = open('LR.pkl','rb')
LR=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predic(Pclass,Sex,Age,SibSp,Parch,Fare,Embarked):
    prediction = LR.predict([[Pclass,Sex,Age,SibSp,Parch,Fare,Embarked]])
    print(prediction)
    return prediction


def main():
  st.title("titanic prediction")
  html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
  st.markdown(html_temp,unsafe_allow_html=True)
  Pclass=st.number_input("pclass","Type Here")
  Sex=st.number_input("sex","Type Here")
  Age=st.number_input("age","Type Here")
  SibSp=st.number_input("sibsp","Type Here")
  Parch=st.number_input("parch","Type Here")
  Fare=st.number_input("fare","Type Here")
  Embarked=st.number_input("embarked","Type Here")
  result=""
  if st.button("predict"):
    result=predic(Pclass,Sex,Age,SibSp,Parch,Fare,Embarked)
  st.success('The output is {}'.format(result))
  if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
   main()
   
