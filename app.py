# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/166A0GZVnMKeVfCDJ6Atr0IJqrVwjoV9K
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle
pickle_in = open('LR.pkl','rb')
LR = pickle.load(pickle_in)
def main():
  st.title("titanic prediction")
  Pclass=st.text_input("pclass")
  Sex=st.text_input("sex")
  Age=st.text_input("age")
  SibSp=st.text_input("sibsp")
  Parch=st.text_input("parch")
  Fare=st.text_input("fare")
  Embarked=st.text_input("embarked")
  result=""
  if st.button("predict"):
    result=predic(Pclass,Sex,Age,SibSp,Parch,Fare,Embarked)
  st.success('The output is {}'.format(result))
if __name__=='__main__':
  main()
def predic(Pclass,Sex,Age,SibSp,Parch,Fare,Embarked):
    prediction = LR.predict([[Pclass,Sex,Age,SibSp,Parch,Fare,Embarked]])
    print(prediction)
    return prediction
