import streamlit as st
import google.generativeai as genai
st.title("google generative AI with streamlit")
st.write("my app")
user_input = st.text_input("Enter your prompt:")
genai.configure(api_key="AIzaSyBkZpCpLi7juVZu9PWtZcK9EFIBJlo8srA")
model=genai.GenerativeModel("models/gemeni-2.5-flash")
if user_input:
 response=model.generate_content(user_input)
 st.write(response.text)

























