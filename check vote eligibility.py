import streamlit as st
from datetime import datetime, timedelta

def check_voting_eligibility(dob):
    # Calculate the date 18 years ago from today
    eighteen_years_ago = datetime.now() - timedelta(days=18*365)
    
    # Check if the user is eligible to vote
    if dob <= eighteen_years_ago:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

# Title of the application
st.title("Voting Eligibility Check")

# Instructions
st.write("Please enter your date of birth:")

# Date input
dob = st.date_input("")

# Button to check eligibility
if st.button("Check Eligibility"):
    # Display eligibility status
    st.write(check_voting_eligibility(dob))