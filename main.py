from dotenv import load_dotenv

from src.ask import ask_question
from src.build_index import create_embeddings
from src.get_interviewquestions_from_glassdoor import collect_questions

# load openai key
load_dotenv(".env")

# Collect interview questions
base_url = "https://www.glassdoor.com/Interview/Spotify-Interview-Questions-E408251.htm"
questions = collect_questions(base_url, stop_after=4)
create_embeddings(questions)

print(
    ask_question(
        "Name three different topics that were discussed in the job interviews"
    )
)
print(
    ask_question(
        "Categorize all interview questions which where asked. For each category, list 5 example questions"
    )
)
