import streamlit as st
from vectorization import *
import QnA
from scrape import *

st.header("Semantic search engine for Q&A")
url = False
query = False
options = st.radio(
    'Choose task',
    ('Ask a question', 'Update the Database'))

if 'Update the Database' in options:
    url = st.text_input("Enter the url")

if 'Ask a question' in options:
    query = st.text_input("Enter your question")

button = st.button("Submit")

if button and (url or query):
    if 'Update the Database' in options:
        with st.spinner("Updating Database..."):
            corpusData = scrape_text_from_url(url)
            addData(corpusData, url)
            st.success("Database Updated")
    if 'Ask a question' in options:
        with st.spinner("Searching for the answer..."):
            urls, res = find_match(query, 2)
            context = "\n\n".join(res)
            st.expander("Context").write(context)
            prompt = QnA.create_prompt(context, query)
            answer = QnA.generate_answer(prompt)
            st.success("Answer: " + answer)