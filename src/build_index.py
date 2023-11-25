import os

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma


def create_embeddings(db_dir: str = "embeddings") -> Chroma:
    """
    Create embeddings for each individual question which was asked.

    :param protocols: list of protocols
    :param db_dir: directory to store the database
    :return: None
    """
    # no need to recreate embeddings if they already exist
    if os.path.exists("embeddings/chroma.sqlite3"):
        return

    # With Chroma we can store and retrieve word embeddings in a database
    embedding_database = Chroma(
        "interview_questions_embeddings",
        embedding_function=OpenAIEmbeddings(),
        persist_directory=db_dir,
    )

    # read questions
    with open("data/collected_questions.txt", "r") as f:
        questions = [q.replace("\n", "") for q in f.readlines()]

    # Iterate over each protocol and add its embedding to the database
    for question in questions:
        embedding_database.add_texts([question])

    embedding_database.persist()

    return embedding_database
