import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import plotly.graph_objects as go
from src.data_importer import get_student_names, get_objectives_for_student
from src.nlp.parent_meeting_preparation import create_advanced_chat
import pandas as pd

st.set_page_config(
    page_title="Prepare Parent Meeting",
    page_icon="🤝",
    layout="wide"
)

st.write("# Prepare Parent Meeting.")

students = get_student_names()
name_list = [student.name for student in students]

selection = st.selectbox("Prepare meeting for the parents of", name_list)

st.write(create_advanced_chat(str(get_objectives_for_student(selection))))
