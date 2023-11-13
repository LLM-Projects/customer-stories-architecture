import streamlit as st
from ques_1 import driver1
from ques_2 import driver2

st.title("Custormer stories architecture")

industry_type = st.text_input(
    "Enter your industry to know more about the customers that use salesforce: "
)

if industry_type:
    response = driver1(industry_type)
    st.markdown(response)

    if(response):
        customer_name = st.text_input(
            "Enter your customer to know more about how they leverage salesforce: "
        )
        if customer_name:
            response = driver2(customer_name)
            st.markdown(response)
