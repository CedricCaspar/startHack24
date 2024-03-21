import streamlit as st
import pandas as pd


df = pd.read_json('src/sg_files/lehrplan-21-kanton-st-gallen.json')

# Display the DataFrame as a table
st.markdown("## Lehrplan 21 Data:")
st.dataframe(df, use_container_width=True, column_order=['code', 'sprache', 'strukturtyp', 'bezeichnung', 'fb_id', 'f_id', 'kb_id', 'ha_id', 'k_id'], height=600)  # Using st.dataframe or st.table to display the DataFrame