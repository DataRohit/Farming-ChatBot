# Imports
import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Farming ChatBot 🌾",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Title of the page
st.markdown("# Farming ChatBot 🌾")
st.markdown("Welcome to the Farming ChatBot! 🚜🌾")
st.markdown("")

# Introduction
st.markdown("## Introduction")
st.markdown(
    """
The Farming ChatBot is your digital companion for all things agriculture. Whether you're a seasoned farmer or just getting started, our chatbot is here to assist you with a wide range of farming queries and tasks.
"""
)

# Features
st.markdown("## Features")

# Simple ChatBot
st.markdown("### Simple ChatBot")
st.markdown(
    """
Need quick answers to common farming questions? Our Simple ChatBot is perfect for you. It collects basic information and provides straightforward solutions to your queries.
"""
)

# Advanced ChatBot
st.markdown("### Advanced ChatBot")
st.markdown(
    """
For more complex farming scenarios, our Advanced ChatBot steps in. It gathers detailed information about your farming setup and offers tailored advice on crop selection, land management, weather conditions, and more.
"""
)

# Technologies Used
st.markdown("## Technologies Used")
st.markdown(
    """
-   **Hugging Face Chat Model**: Powering our chatbot with the latest advancements in natural language processing.
-   **Streamlit**: Building our user-friendly web interface with Streamlit, making it easy to interact with the chatbot.
-   **Hugging Face Chat API**: Enabling seamless communication between our chatbot and users through the API.
"""
)

# Getting Started
st.markdown("## Getting Started")
st.markdown(
    """
1. Clone this repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the Streamlit application using `streamlit run 00_🌾_Home.py`.
4. Choose between the Simple or Advanced ChatBot and start interacting!
"""
)

# Contribution Guidelines
st.markdown("## Contribution Guidelines")
st.markdown(
    """
We welcome contributions from the community to enhance the functionality and performance of our Farming ChatBot. Please follow these guidelines when contributing:

-   Fork the repository and create your branch from `master`.
-   Open a pull request with a clear description of the changes proposed.
-   Ensure your code follows the project's coding standards and practices.
"""
)

# Note about ChatGPT API
st.markdown("### **Note:**")
st.markdown(
    """
ChatGPT API requires a premium account and thus I have used Hugging Face Chat API.
"""
)
