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


def get_html(url):
    driver = uc.Chrome(headless=False)
    driver.get(url)

    return driver.page_source


def collect_questions(base_url, stop_after=float("inf")):
    page_number = 1
    questions = []
    while True:
        if page_number == stop_after:
            return questions

        # Construct the URL for the current page
        if page_number == 1:
            url = base_url
        else:
            url = f"{base_url[:-4]}_P{page_number}.htm"

        html = get_html(url)
        cleaned_interview_questions = extract_interview_questions_from_html(
            html
        )

        if cleaned_interview_questions == []:
            return questions
        else:
            questions += cleaned_interview_questions

        page_number += 1
