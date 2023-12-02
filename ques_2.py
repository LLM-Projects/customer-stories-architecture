from langchain.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import PromptTemplate
from langchain import hub
from env import OPENAI_API_KEY

def main():
    loader = CSVLoader(file_path="output.csv")
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    splits = text_splitter.split_documents(data)
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY),
    )
    retriever = vectorstore.as_retriever()
    rag_prompt = hub.pull("rlm/rag-prompt")
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=OPENAI_API_KEY,
    )
    template = """Use the following pieces of context to answer the question at the end. 
    If you don't know the answer, just say that you don't know, don't try to make up an answer. 
    Use three sentences maximum and keep the answer as concise as possible.
    {context}
    Question: {question}
    Helpful Answer:"""
    rag_prompt_custom = PromptTemplate.from_template(template)

    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | rag_prompt_custom
        | llm
    )
    return rag_chain


def driver2(customer_name):
    rag_chain = main()
    response = rag_chain.invoke(
        "Can you tell me more about customer"
        + customer_name
        + " and how they benefited from salesforce?"
    )
    print(response)
    return response.content
