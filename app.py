
import streamlit as st

from backend import ask_question

st.title("Company Chatbot")

question = st.text_input(
    "Ask a question about the company"
)

if st.button("Ask"):

    answer = ask_question(question)

    st.write(answer)