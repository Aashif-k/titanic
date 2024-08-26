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
  Pclass=st.number_input("pclass")
  Sex=st.number_input("sex")
  Age=st.number_input("age")
  SibSp=st.number_input("sibsp")
  Parch=st.number_input("parch")
  Fare=st.number_input("fare")
  Embarked=st.number_input("embarked")
  result=""
  if st.button("predict"):
    result=predic(Pclass,Sex,Age,SibSp,Parch,Fare,Embarked)
  st.success('The output is {}'.format(result))
  if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
   main()
   
