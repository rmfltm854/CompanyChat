import sys

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
import os
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

def loadQA():
    os.environ['OPENAI_API_KEY'] = ""

    vectorstore = Chroma(persist_directory="/Users/jominsu/Desktop/EmbeddingDirectory/",embedding_function=OpenAIEmbeddings())

    return vectorstore

def chat(query):
    vector = loadQA()
    pdf_qa = ConversationalRetrievalChain.from_llm(
        ChatOpenAI(temperature=0.7, model_name='gpt-3.5-turbo-16k'),
        retriever=vector.as_retriever(search_kwargs={'k': 6}),
        return_source_documents=True,
        verbose=False
    )
    chat_history = []
    result = pdf_qa(
        {"question": query, "chat_history": chat_history})
    print(result["question"])
    print(result["answer"])
    chat_history.append((query, result["answer"]))
    return result["answer"]