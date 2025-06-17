from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain.schema import Document

import os
from dotenv import load_dotenv
load_dotenv()

def build_qa_chain():
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0)

    template = """
    You are an AI political analyst. Based on the following manifesto document:
    {context}
    Answer the question: {question}
    """
    prompt = PromptTemplate(template=template, input_variables=["context", "question"])
    chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)

    return chain

def run_qa(chain, text, query):
    docs = [Document(page_content=text)]
    response = chain.run(input_documents=docs, question=query)
    return response