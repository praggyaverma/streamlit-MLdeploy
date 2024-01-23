import pickle
import streamlit as st
import pandas as pd
import numpy as np

st.title("Classification of Handwritten Digit")

photo = st.file_uploader(label = "Upload image for classification")

model = pickle.load(open('model.pkl', 'rb'))

st.header("Predicted")

st.text('')
st.text('')
st.markdown(
    '`Create by` [praggyaverma](https://linkedin.com/praggyaverma/) | \
         `Code:` [GitHub](https://github.com/praggya/streamlit-MLdeploy)')
