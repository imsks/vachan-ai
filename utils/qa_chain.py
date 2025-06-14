from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain.schema import Document

def build_qa_chain():
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

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