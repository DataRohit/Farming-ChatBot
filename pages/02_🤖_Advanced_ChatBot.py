# Imports
import streamlit as st
from helper import get_response


# Configure the page
st.set_page_config(
    page_title="Advanced Farming ChatBot 🌾",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


##### Title Start #####

# Title of the page
st.markdown("# Advanced Farming ChatBot 🌾")

# Subtitle of the page
st.markdown("#### **Welcome to the Farming ChatBot! 🚜🌾**")
st.markdown("<br>", unsafe_allow_html=True)

##### Title End #####


##### Helpers Start #####

# Create 2 columns for the page
col1, col2 = st.columns(2)

# Initialize a dictionary to store user inputs
user_inputs = {}

##### Helpers End #####


#### Input Fields Start ####

# Field to take user input for Crop Selection
with col1:
    user_inputs["Crop Selection"] = st.multiselect(
        "Crop Selection",
        ["Rice", "Wheat", "Sugarcane", "Cotton", "Maize", "Soybean"],
        default=["Rice"],
    )

# Field to take user input for Land Size
with col2:
    user_inputs["Land Size"] = st.selectbox(
        "Land Size",
        [
            "Small (0 - 2 acres)",
            "Medium (2 - 5 acres)",
            "Large (5 - 10 acres)",
            "Very Large (10 - 20 acres)",
            "Large Scale (20+ acres)",
            "Not Applicable",
        ],
    )

# Field to take user input for Fertilizer Usage
with col1:
    user_inputs["Fertilizer Used"] = st.multiselect(
        "Fertilizer Used",
        [
            "Organic", "Chemical", "Mixed (Organic + Chemical)",
            "Bio-Fertilizers", "Vermicompost", "Not Applicable"
        ],
        default=["Organic"],
    )

# Field to take user input for Weather Conditions
with col2:
    user_inputs["Weather Conditions"] = st.selectbox(
        "Weather Conditions",
        [
            "Rainy",
            "Sunny",
            "Cloudy",
            "Windy",
            "Foggy",
            "Snowy",
            "Hailstorm",
            "Thunderstorm",
            "Not Applicable",
        ],
    )

# Field to take user input for Pesticide Usage
with col1:
    user_inputs["Pesticide Used"] = st.multiselect(
        "Pesticide Used",
        [
            "Organic", "Chemical", "Integrated Pest Management (IPM)",
            "Herbal/Ayurvedic", "Bio-Pesticides", "Not Applicable"
        ],
        default=["Organic"],
    )

# Field to user input for Previous Year Crop Yield
with col2:
    user_inputs["Crop Yield"] = st.selectbox(
        "Crop Yield",
        [
            "Low (<50% of expectation)",
            "Average (50-75% of expectation)",
            "Above Average (75-100% of expectation)",
            "Good (100-125% of expectation)",
            "Excellent (125-150% of expectation)",
            "Outstanding (>150% of expectation)",
        ],
    )

# Field to take user input for Soil Type
with col1:
    user_inputs["Soil Type"] = st.multiselect(
        "Soil Type",
        [
            "Clay", "Sandy", "Loamy", "Peaty", "Chalky", "Silty", "Not Applicable"
        ],
        default=["Clay"],
    )

# Field to take user input for Irrigation Type
with col2:
    user_inputs["Irrigation Type"] = st.selectbox(
        "Irrigation Type",
        ["Drip Irrigation", "Sprinkler Irrigation", "Flood Irrigation", "Not Applicable"],
    )

# Field to take user input for Seed Type
with col1:
    user_inputs["Seed Type"] = st.multiselect(
        "Seed Type",
        ["Hybrid", "GM (Genetically Modified)", "Traditional", "Organic", "Not Applicable"],
        default=["Hybrid"],
    )

# Field to take user input for Financial Constraints
with col2:
    user_inputs["Financial Constraints"] = st.selectbox(
        "Financial Constraints",
        ["Yes", "No"],
    )

# Field to take user input for Location
user_inputs["Location"] = st.text_input(
    "Location",
    placeholder="City / Town / Village, State, Country",
)

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
    if user_inputs["Location"] == "" or user_inputs["Issue Description"] == "":
        st.error("Please fill in the Location and Issue Description fields!")
    
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