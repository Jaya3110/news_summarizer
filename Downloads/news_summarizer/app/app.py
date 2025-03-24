import streamlit as st
import requests

st.title("News Summarizer and TTS App")

# Problem: This input field might be missing an autocomplete attribute
company_name = st.text_input("Enter Company Name:", "")

if st.button("Analyze News"):
    if company_name:
        try:
            response = requests.post("http://127.0.0.1:5000/api/analyze", json={"company": company_name})
            
            if response.status_code == 200:
                data = response.json()
                st.success("News analyzed successfully!")
                st.write(data["report"])
            else:
                st.error(f"Error: {response.json().get('error', 'Unknown error')}")
        
        except requests.RequestException as e:
            st.error(f"Request Error: {e}")
    else:
        st.error("Please enter a valid company name.")
