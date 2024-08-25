# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import pickle

pickle_in = open('LR.pkl','rb')
LR=pickle.load(pickle_in)


def predic(Pclass,Sex,Age,SibSp,Parch,Fare,Embarked):
    prediction = LR.predict([[Pclass,Sex,Age,SibSp,Parch,Fare,Embarked]])
    print(prediction)
    return prediction


def main():
  st.title("titanic prediction")
  Pclass=st.text_input("pclass","Type Here")
  Sex=st.text_input("sex","Type Here")
  Age=st.text_input("age","Type Here")
  SibSp=st.text_input("sibsp","Type Here")
  Parch=st.text_input("parch","Type Here")
  Fare=st.text_input("fare","Type Here")
  Embarked=st.text_input("embarked","Type Here")
  result=""
  if st.button("predict"):
    result=predic(Pclass,Sex,Age,SibSp,Parch,Fare,Embarked)
  st.success('The output is {}'.format(result))

if __name__=='__main__':
   main()