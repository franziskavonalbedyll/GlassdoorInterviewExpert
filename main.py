import os

from dotenv import load_dotenv

from src.ask import ask_question
from src.build_index import create_embeddings
from src.create_result_files import generate_report
from src.get_interviewquestions_from_glassdoor import collect_questions
from src.helpers import read_questions

# load openai key
load_dotenv(".env")

# Collect interview questions
base_url = "https://www.glassdoor.com/Interview/Spotify-Interview-Questions-E408251.htm"
if not os.path.exists(
    os.path.join(os.getcwd(), "data", "collected_questions.txt")
):
    collect_questions(base_url, stop_after=2)

# create embeddings, which will be stored to the embedding directory by default
create_embeddings()

# generate report
qa_pairs = []
questions = read_questions("questions.txt")
for question in questions:
    q = question.strip()
    qa_pairs.append((q, ask_question(q)))

generate_report(qa_pairs, "results")
