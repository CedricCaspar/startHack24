import random

import pandas as pd
import streamlit as st

from src.data import Result

from src.data_importer import data_dict

data = data_dict
exams = [[exam.subject, exam.teacher, exam.creation, " ", [random.randint(0, 50) / 10 for _ in range(16)], " ", " ", "✏️",
          True if i % 2 == 0 else False] for i, exam in enumerate(data["exams"])]
exams = pd.DataFrame(exams, columns=['subject', 'date', 'teacher', 'acpase2', 'plot', 'space', 'acpase', 'icon', 'check'])


st.set_page_config(layout='wide')

st.markdown(
    """
    <style>
        div[data-testid="column"]:nth-of-type(1)
        {
        } 

        div[data-testid="column"]:nth-of-type(2)
        {
            text-align: center;
        }
        div[data-testid="column"]:nth-of-type(3)
        {
            text-align: end;
        } 
    </style>
    """, unsafe_allow_html=True
)
col1, col2, col3 = st.columns([20, 1, 1])

with col1:
    st.markdown("## Exams")

with col2:
    st.button("A-Z")
with col3:
    st.button("➕")

st.divider()
for i, row in exams.iterrows():
    print(row)
    with st.container(border=1):
        col1, col2, col3, col4, col5, col6 = st.columns([2,2,2,8,2,1])
        with col1:
            st.markdown(f"#### {row[0]}")
        with col2:
            st.markdown(f"#### {row[1]}")
        with col3:
            st.markdown(f"#### {row[2]}")
        with col5:
            st.button("completed", key=str(i))
            #st.line_chart(row[4], height=50)
        with col6:
            st.write("✏️")


