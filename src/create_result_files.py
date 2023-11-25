import os

from mdutils.mdutils import MdUtils


def generate_report(qa_pairs, filename):
    mdFile = MdUtils(
        file_name=f"results/{filename}", title="Interview Questions Summary"
    )

    for i, (question, answer) in enumerate(qa_pairs):
        mdFile.new_header(level=1, title=f"Question {i+1}")
        mdFile.new_paragraph(question)
        mdFile.new_header(level=2, title="Answer")
        mdFile.new_paragraph(answer)

    if not os.path.exists("results"):
        os.makedirs("results")

    mdFile.create_md_file()
