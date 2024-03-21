import streamlit as st

# List of options
options = ['Option 1', 'Option 2', 'Option 3']

selected_options = {}


def printOption():
    selected = [option for option, selected in selected_options.items() if selected]
    if selected:
        st.write('You selected:', ', '.join(selected))
    else:
        st.write('No options selected')


# Dictionary to hold the checkbox state

form = st.form("test")

for option in options:
    # Create a checkbox for each option
    selected_options[option] = form.checkbox(option)
form.form_submit_button("Submit", "give me", printOption)
# Display which options were selected
