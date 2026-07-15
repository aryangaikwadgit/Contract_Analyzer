import streamlit as st

from pathlib import Path

from frontend.api import analyze_contract
from frontend.components import (
    hero,
    metrics,
    summary,
    clauses,
)

from frontend.api import analyze_contract, ask_question

st.set_page_config(page_title="ContractIQ", page_icon="📄", layout="wide")

with open("frontend/styles.css") as f:

    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

hero()

uploaded_file = st.file_uploader("Upload Contract", type=["pdf"])

if uploaded_file:

    if st.button("Analyze Contract"):

        with st.spinner("Analyzing Contract..."):

            report = analyze_contract(uploaded_file)

        st.success("Analysis Completed")

        metrics(report)

        summary(report)

        clauses(report)
# ---------------------- CHAT ----------------------

st.divider()

st.subheader("💬 Ask ContractIQ")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Ask anything about your contract...")

if prompt:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = ask_question(prompt)

            answer = response["answer"]

            st.markdown(answer)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )



