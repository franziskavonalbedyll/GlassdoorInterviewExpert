import os
import random
import time

import undetected_chromedriver as uc
from bs4 import BeautifulSoup


def extract_interview_questions_from_html(html):
    # Create a BeautifulSoup object
    soup = BeautifulSoup(html, "html.parser")

    # Searching for elements with 'data-test' attribute that contains 'Interview' and 'QuestionsContainer'
    interview_questions_elements = soup.find_all(
        attrs={
            "data-test": lambda value: value
            and value.startswith("Interview")
            and value.endswith("QuestionsContainer")
        }
    )

    # Removing "Interview Questions" and "Answer Question" from the strings
    cleaned_interview_questions = [
        " ".join(element.stripped_strings)
        .replace("Interview Questions", "")
        .replace("Answer Question", "")
        .strip()
        for element in interview_questions_elements
    ]

    return cleaned_interview_questions  # Display first 3 entries for review


def write_questions_to_file(questions):
    if not os.path.exists("data"):
        os.makedirs("data")

    with open("data/collected_questions.txt", "w") as f:
        for question in questions:
            f.write(question + "\n")


def collect_questions(base_url, stop_after=float("inf")):
    page_number = 1
    questions = []
    driver = uc.Chrome(headless=False)
    while True:
        if page_number == stop_after:
            write_questions_to_file(questions)
            return questions

        # Construct the URL for the current page
        if page_number == 1:
            url = base_url
        else:
            url = f"{base_url[:-4]}_P{page_number}.htm"

        time.sleep(random.randint(10, 60))
        driver.get(url)
        html = driver.page_source
        cleaned_interview_questions = extract_interview_questions_from_html(
            html
        )

        if cleaned_interview_questions == []:
            # write collected_questions to txt
            write_questions_to_file(questions)
            return
        else:
            questions += cleaned_interview_questions

        page_number += 1
