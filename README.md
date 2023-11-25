# GlassdoorInterviewExpert
![Image](img.png)
Scrape Glassdoor Interview Questions for a company of your interest and have GPT-4 summarize these questions for you.

## Features
- **Customizable Query**: Specify the company whose interview questions you're interested in, and the tool will fetch relevant questions from Glassdoor.
- **GPT-4 Summarization**: Utilizes the advanced capabilities of GPT-4 to provide clear, concise summaries of the fetched interview questions.
- **Interactive Question Addition**: Add your own questions about the interview process in a simple text file for personalized insights.


## Getting Started
### Prerequisites
- An active OpenAI API key.
- Python environment capable of running the script.

### Installation
1. Clone the repository to your local machine.
2. Install the required dependencies using Poetry: `poetry install`.

### Configuration
- Add your OpenAI API key to a `.env` file in the project directory.
- Set the `base_url` in `main.py` to the Glassdoor interview start page of the company you are interested in.

### Usage
1. Add any specific questions you have regarding the interview process to `questions.txt`. There are some example questions already provided to get you started.
2. Run the script using the command: `poetry run python main.py`.
3. The script will first scrape Glassdoor for interview questions and then proceed to summarize them using GPT-4.

## Development Tools
### Pre-commit

Pre-commit is used in this project to ensure that git commits adhere to a consistent style and prevent committing problematic code. The hooks configured in `.pre-commit-config.yaml` will automatically check and fix issues (where possible) in the staged files when you run `git commit`.

Using this project's pyproject.toml, poetry already installs pre-commit for you, so no need to take care of it manually!

If you want to run pre-commit manually, enter the poetry shell and use:
```
pre-commit run
```

### Poetry

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. If you would like to add a package, simple run:
```bash
poetry add <name-of-dependency>
```


## Contributing
Contributions to enhance GlassdoorInterviewExpert are warmly welcomed. Whether it's bug fixing, feature adding, or documentation improvements, feel free to create a pull request.
