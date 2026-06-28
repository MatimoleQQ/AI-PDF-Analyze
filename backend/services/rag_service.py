import os

from dotenv import load_dotenv



from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI

from langchain_chroma import Chroma
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

embeddings = OpenAIEmbeddings(api_key=api_key)

DB_PATH = "chroma_db"

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


def save_document(text: str):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    docs = splitter.create_documents([text])

    vector_store = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=DB_PATH
    )

    return len(docs)


def ask_question(question: str):

    vector_store = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )

    docs = vector_store.similarity_search(
        question,
        k=4
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    Answer ONLY using the context below.

    Context:
    {context}

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return response.content