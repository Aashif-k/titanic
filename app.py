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
    st.subheader("Pclass:")
  Pclass=st.slider("Select the class",min_value=1.0,max_value=3.0,step=1.0)
  Sex=st.slider("Sex",min_value=0.0,max_value=1.0,step=1.0)
  Age=st.number_input("age")
  SibSp=st.slider("SibSp",min_value=0.0,max_value=2.0,step=1.0)
  Parch=st.slider("Parch",min_value=0.0,max_value=3.0,step=1.0)
  Fare=st.number_input("fare")
  Embarked=st.slider("Embarked",min_value=0.0,max_value=2.0,step=1.0)
  result=""
  if st.button("predict"):
    result=predic(Pclass,Sex,Age,SibSp,Parch,Fare,Embarked)
  st.success('The output is {}'.format(result))
  if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
   main()
   
