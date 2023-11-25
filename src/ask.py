from chromadb import PersistentClient
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import Chroma

MEMORY = ConversationBufferMemory(
    memory_key="chat_history", return_messages=True
)


def ask_question(question: str) -> str:
    """Generate answer to user question.

    :param question: question to ask
    :param embeddings: word embeddings
    :return: answer
    """

    # get embeddings from database
    client = PersistentClient(path="embeddings")
    embeddings = Chroma(
        client=client,
        collection_name="interview_questions_embeddings",
        embedding_function=OpenAIEmbeddings(),
    )

    chat = ChatOpenAI(model_name="gpt-4")
    chain = ConversationalRetrievalChain.from_llm(
        llm=chat,
        retriever=embeddings.as_retriever(),
        memory=MEMORY,
        max_tokens_limit=4096,
    )

    response = chain({"question": question})
    answer = response["answer"]

    return answer
