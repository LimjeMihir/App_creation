import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyDPiKu1s7joS0Z55iDTUzDQAvYHgvoOc0E")
model = genai.GenerativeModel("gemini-1.5-pro")

st.title("My Assistant")
prompt = st.text_input("Enter your Question")

if st.button("Ask Me"):
    response = model.generate_content(prompt)
    st.write(response.text)
