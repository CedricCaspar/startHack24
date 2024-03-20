import streamlit as st

# List of options
options = ['Option 1', 'Option 2', 'Option 3']

# Dictionary to hold the checkbox state
selected_options = {}

for option in options:
    # Create a checkbox for each option
    selected_options[option] = st.checkbox(option)

# Display which options were selected
selected = [option for option, selected in selected_options.items() if selected]
if selected:
    st.write('You selected:', ', '.join(selected))
else:
    st.write('No options selected')