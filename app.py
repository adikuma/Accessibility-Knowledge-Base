# app.py
import streamlit as st
import requests

st.set_page_config(page_title="Document Chat", page_icon="📄")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Accessibility Knowledge Base")
st.caption("Ask questions about your documents")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Searching documents..."):
        try:
            response = requests.post(
                "https://multi-document-agents.onrender.com/query",
                json={'text': prompt},
                headers={'Content-Type': 'application/json'},
                timeout=30
            )
            response_data = response.json()
            answer = response_data.get("response", "No answer found")
        except Exception as e:
            answer = f"Error: {str(e)}"

    with st.chat_message("assistant"):
        st.markdown(answer)
    
    st.session_state.messages.append({"role": "assistant", "content": answer})