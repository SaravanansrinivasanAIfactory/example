import streamlit as st

# Title of the application
st.title("Hello, Streamlit!")

# A simple line of text
st.text("Welcome to this simple Streamlit application.")

# Display a checkbox on the sidebar
if st.sidebar.checkbox("Show/Hide"):
    # Display text when the checkbox is checked
    st.text("Showing the widget")

# Display a radio button
status = st.radio("Select Gender: ", ('Male', 'Female'))
if status == 'Male':
    st.success("You selected Male.")
else:
    st.success("You selected Female.")

# Display a selection box
hobby = st.selectbox("Hobbies: ", ['Dancing', 'Reading', 'Sports'])
st.write("Your hobby is: ", hobby)
