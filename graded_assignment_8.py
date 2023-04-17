# -*- coding: utf-8 -*-
"""Graded Assignment 8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MWDQZFropBT9ekUrvpgqDA2gOsjemmpq
"""

import streamlit as st
import pandas as pd

st.write("""
# An app that finds the largest among the 3 given numbers

This app returns the value greater than the other two
""")

st.header('User Input Parameters')

def user_input_features():
    n1 = st.number_input("n1",min_value=-9999999999.999,max_value=9999999999.999,step=0.0000000001)
    n2 = st.number_input("n2",min_value=-9999999999.999,max_value=9999999999.999,step=0.0000000001)
    n3 = st.number_input("n3",min_value=-9999999999.999,max_value=9999999999.999,step=0.0000000001)

    data = {'n1': n1,
            'n2':n2,
            'n3':n3
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())

#Preprocessing


for col in df.columns:
    if df[col].dtype != 'float64':
        df[col] = df[col].values.astype('float64')

st.subheader('Pre-processed Input to the Model')
st.table(df)

# Model Loading
N1 = df[0][0]
N2 = df[0][1]
N3 = df[0][2]

#Model Inferencing

st.subheader('Prediction Probability')

if (N1>N2 and N1>N3) or (N1>N2 and N2==N3):
  st.write(N1 + " is the largest value")
elif (N2>N1 and N2>N3) or (N2>N1 and N1==N3):
  st.write(N2 + " is the largest value")
elif (N3>N1 and N3>N2) or (N3>N1 and N1==N2):
  st.write(N3 + " is the largest value")
else:
  st.write(N1 + " is the largest value")
