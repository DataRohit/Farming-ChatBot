# Imports
import streamlit as st


# Set the page configuration
st.set_page_config(
    page_title="Farming ChatBot 🌾",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)


##### Title Start #####

# Title of the page
st.markdown("# Farming ChatBot 🌾")

# Subtitle of the page
st.markdown("#### **Welcome to the Farming ChatBot! 🚜🌾**")
st.markdown("<br>", unsafe_allow_html=True)

##### Title End #####


# Description of Simple ChatBot
st.markdown("### **Simple ChatBot**")
st.markdown("""
This is a simple chatbot designed to assist with general farming queries. It collects basic information such as issue description and language preference.
""")

# Link to redirect to Simple ChatBot
st.markdown("[Click here to use the Simple ChatBot](/Simple_ChatBot)")

# Description of Advanced ChatBot
st.markdown("### **Advanced ChatBot**")
st.markdown("""
The Advanced ChatBot provides more detailed assistance tailored to specific farming scenarios. It collects information about crop selection, land size, fertilizer usage, weather conditions, etc.
""")

# Link to redirect to Advanced ChatBot
st.markdown("[Click here to use the Advanced ChatBot](/02_Advanced_ChatBot)")

# Technologies Used
st.markdown("### **Technologies Used**")
st.markdown("""
- Hugging Face Chat Model: The chatbot is powered by the Hugging Face Chat Model, specifically using the OpenChat/OpenChat-3.5-0106 model.
- Hugging Face Chat API: The chatbot interacts with the Hugging Face Chat API to generate responses.
- Streamlit: The web application is built using Streamlit, a Python library for building interactive web applications.
""")

# Note about ChatGPT API
st.markdown("### **Note:**")
st.markdown("""
ChatGPT API requires a premium account and thus I have used Hugging Face Chat API.
""")