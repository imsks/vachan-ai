import streamlit as st
from utils.pdf_loader import extract_text_from_pdf
from utils.qa_chain import build_qa_chain, run_qa
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Convert the generator to a list
models = list(genai.list_models())

# Print model names
for model in models:
    print("HERE",model.name)

st.set_page_config(page_title="Vachan - Political Manifesto QA")
st.markdown("Ask questions to understand what parties have promised")

pdf_files = os.listdir("data")
selected_pdf = st.selectbox("Choose a Party Manifesto:", pdf_files)

if selected_pdf:
    with st.spinner("Loading manifesto..."):
        text = extract_text_from_pdf(f"data/{selected_pdf}")
        qa_chain = build_qa_chain()

query = st.text_input("Ask something:", placeholder="e.g. What are their plans for women safety?")

if st.button("Ask") and query:
    with st.spinner("Analyzing..."):
        response = run_qa(qa_chain, text, query)
        st.success(response)