import streamlit as st
from datetime import datetime
import numpy as np

def calculate_interest(principal, start_date, end_date):
    monthly_rate = 2 / 100  # monthly interest rate 
    annual_rate = monthly_rate * 12 # annualize rate
    duration_in_years = (end_date - start_date).days / 365
    # Apply compound interest formula
    compound_interest = principal * ((1 + annual_rate) ** duration_in_years) - principal
    return compound_interest

st.title("Interest Calculator")

# Take the inputs from the user
principal = st.number_input("Enter Principal Amount", min_value=0.0, value=0.0, step=0.01)
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

if st.button("Calculate Interest"):
    if end_date < start_date:
        st.error("End date should be after start date.")
    else:
        interest = calculate_interest(principal, start_date, end_date)
        st.write(f'The compound interest for the given period is: Rs. :blue{np.round(interest, 2)}')
        
        st.write(f'Total money owed Rs. :blue{np.round(principal + interest, 2)}')
