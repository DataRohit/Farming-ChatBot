# Imports
import streamlit as st
from helper import get_response

# Configure the page
st.set_page_config(
    page_title="Simple Farming ChatBot 🌾",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

##### Title Start #####

# Title of the page
st.markdown("# Simple Farming ChatBot 🌾")

# Subtitle of the page
st.markdown("#### **Welcome to the Farming ChatBot! 🚜🌾**")
st.markdown("<br>", unsafe_allow_html=True)

##### Title End #####


##### Helpers Start #####

# Initialize a dictionary to store user inputs
user_inputs = {}

##### Helpers End #####


#### Input Fields Start ####

# Field to take user input for Issue Description
user_inputs["Issue Description"] = st.text_area(
    "Issue Description",
    placeholder="Describe the issue you are facing...",
)

#### Input Fields End ####


#### Language Selection Start ####

# Dropdown for language selection
user_inputs["Selected Language"] = st.selectbox(
    "Select Language",
    ["English", "Hindi", "Bengali", "Telugu", "Marathi", "Tamil"]
)

#### Language Selection End ####


#### Submit Button Start ####

# Button to submit the user inputs
if st.button("Submit"):
    # Check for empty fields in location and issue description
    if user_inputs["Issue Description"] == "":
        st.error("Please fill the Issue Description field!")
    
    # If all fields are filled, display the user inputs
    else:
        # Display the processing message
        processing_message = st.markdown("### **Processing...**")
        
        # Get the response from the chatbot
        response = get_response(user_inputs)
        
        # Once response is received, display it and remove the processing message
        processing_message.empty()
        st.markdown("### **ChatBot Response:**")
        st.markdown(response)

#### Submit Button End ####
