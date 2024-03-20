import streamlit as st
import pandas as pd


df = pd.read_json('src/sg_files/lehrplan-21-kanton-st-gallen.json')


    # Display the DataFrame as a table
st.write("Lehrplan 21:")
st.dataframe(df, use_container_width=True)  # Using st.dataframe or st.table to display the DataFrame