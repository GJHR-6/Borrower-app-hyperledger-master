import json
import uuid
from typing import OrderedDict
from PIL import Image

import requests
import streamlit as st
from google.protobuf.symbol_database import Default

st.title("Borrower application form")
image = Image.open("logo.png")
st.image(image, width=300)
col1, col2, col3 = st.columns(3)

my_form = col1.form("my_form")
form_data_1 = {
    "name": my_form.text_input("First Name", placeholder=""),
    "phone": my_form.text_input("Primary phone number"),
    "email": my_form.text_input("Email address"),
    "street": my_form.text_input("Property Address line 1", placeholder=""),
    "street_2": my_form.text_input("Property Address line 2", placeholder=""),
    "property_city": my_form.text_input("Property City", placeholder=""),
    "property_country": my_form.text_input("Property County", placeholder=""),
    "property_state": my_form.text_input("Property State", placeholder=""),
    "property_zip_code": my_form.text_input("Property Zip code", placeholder=""),
    "tell_us_about_your_loan": my_form.text_input(
        "Tell us about the property you want to use as collateral for your loan."
    ),
    "property_location": my_form.text_input("Propery Location"),
}
my_form.form_submit_button(label="Submit")


my_form_2 = col2.form(key="my_form_2")
form_data_2 = {
    "property_use": my_form_2.text_input("What is the property's.  use?"),
    "property_value": my_form_2.text_input("Estimated property value"),
    "line_of_credit": my_form_2.text_input("Line of credit amount"),
    "plans_for_the_funds": my_form_2.text_input("How do you plan to use the funds?"),
    "loan_used_for_business": my_form_2.text_input(
        "Will loan proceeds be used primary for business purposes?"
    ),
    "suffix": my_form_2.text_input("Suffix"),
    "time_at_address": my_form_2.text_input("Time at this address"),
    "best_time_to_call": my_form_2.text_input("Best time to call"),
    "secondary_phone_number": my_form_2.text_input("Secondary phone number"),
    "country_of_citizenship": my_form_2.text_input("Country of Citizenship"),
    "country_of_residence": my_form_2.text_input("Country of Residence"),
}
my_form_2.form_submit_button(label="Submit")


my_form_3 = col3.form(key="my_form_3")
form_data_3 = {
    "social_security_number": my_form_3.text_input("Social Security Number"),
    "date_of_birth": my_form_3.text_input("Date of Birth"),
    "marital_status": my_form_3.text_input("Marital Status"),
    "preferred_language": my_form_3.text_input("Choose your preferred language?"),
    "employment_status": my_form_3.text_input("Employment Status"),
    "anual_income": my_form_3.text_input("Annual income"),
    "source_of_income": my_form_3.text_input("Your source of income"),
    "additional_income": my_form_3.text_input(
        "Do you have additioinal income from other sources?"
    ),
    "coapplicant": my_form_3.text_input("Co-applicant"),
}
submit_button = my_form_3.form_submit_button(label="Submit")

form_data = {**form_data_1, **form_data_2, **form_data_3}

form_data["vendor"] = "receive_borrower"

# Lender node API

url = "https://mr9w0zhxw7.execute-api.us-east-1.amazonaws.com/prod"

headers = {"Content-Type": "application/json"}


if submit_button:
    st.write("Generating Loan number")
    unique_id = str(uuid.uuid4())
    st.write(unique_id)
    form_data["topics"] = unique_id
    response = requests.request(
        "POST", url, headers=headers, data=json.dumps(form_data)
    )
    st.write("Response received.")
    response_json = response.text
