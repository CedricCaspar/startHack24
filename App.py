import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import plotly.graph_objects as go
from src.data_importer import get_student_names





st.set_page_config(
    page_title="Students",
    page_icon="🏫",
    layout="wide"
)

st.write("# Class 4b.")
col1, col2 = st.columns(2)

with col1:

    st.header("Students")
    students = get_student_names()

    for student in students:
        with st.expander(student):
            st.write(f"Opening {student}")


with col2:

    with stylable_container(
            key="container_with_border",
            css_styles="""
                {
                    border: 1px solid rgba(49, 51, 63, 0.2);
                    border-radius: 0.5rem;
                    background-color: #EFF6E0;
                    padding: calc(1em - 1px)
                }
                """,
    ):

        categories = ['Reading Comprehension', 'Critical Thinking', 'Research Skills', 'Science and Exploration', 'Writing and Grammar', 'Advanced Math Skills']
        values = [4, 3, 2, 5, 4, 4]

        # Create a radar chart
        fig = go.Figure()

        # Custom color for the radar chart
        custom_color = '#124559'  # Tomato color
        fill_color = '#598392'

        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            fillcolor=fill_color,  # Custom fill color
            line=dict(color=custom_color),  # Custom line color
            name='Product A'
        ))

        # Update layout for transparency and custom radial axis color
        fig.update_layout(
            polar=dict(
                bgcolor='rgba(0,0,0,0)',  # Transparent polar background
                radialaxis=dict(
                    visible=True,
                    range=[0, 5],
                    color=custom_color  # Custom radial axis tick color
                )),
            paper_bgcolor='rgba(0,0,0,0)',  # Transparent overall background
            plot_bgcolor='rgba(0,0,0,0)',  # Transparent plot background
            showlegend=False
        )

        # Configuration to disable interactivity
        config = {'staticPlot': True}

        # Display the chart in Streamlit
        st.plotly_chart(fig, use_container_width=True, config=config)
        st.subheader("Semester Progress")
        st.write("21.02.24")