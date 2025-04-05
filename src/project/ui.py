import streamlit as st
from main import run


st.title("Streamlit App with Sidebar")

email = st.chat_input("Enter the email you want to classify:")

if email:
        result = run(email)
        st.table({
                key:[value]
                for key, value in result.items()
            }
        )

