import os

from dotenv import load_dotenv

from langchain_text_splitters import CharacterTextSplitter

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_openai import ChatOpenAI

# CHANGED IMPORT
from langchain_classic.chains import RetrievalQA


# LOAD ENV VARIABLES
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")


# LOAD COMPANY DATA
loader = TextLoader("data/company.txt")

documents = loader.load()


# SPLIT TEXT
text_splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)


# LOCAL EMBEDDINGS
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# VECTOR DATABASE
db = FAISS.from_documents(
    docs,
    embeddings
)

retriever = db.as_retriever()


# LOAD MODEL
llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    base_url=BASE_URL,
    model=MODEL_NAME,
    temperature=0
)


# QA CHAIN
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)


# QUESTION FUNCTION
def ask_question(question):

    response = qa.run(question)

    return response