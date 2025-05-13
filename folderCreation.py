import os
from pathlib import Path
from tkinter import Tk, filedialog

# Hide the root Tk window
root = Tk()
root.withdraw()

# Ask the user to choose a directory
save_dir = filedialog.askdirectory(title="Select folder to save ENGLISH project")

if not save_dir:
    print("No directory selected. Exiting.")
    exit()

base_dir = Path(save_dir) / "ENGLISH"

# Year folders
year_folders = [
    "2016 to current",
    "B16",
    "B17",
    "B18",
    "B19",
    "B21",
    "B22",
    "B23",
    "B24",
    "B25",
    "B26",
    "B27",
]

# English 1st paper topics
first_paper_topics = [
    "MCQ",
    "QnA",
    "Flowchart",
    "WithClues",
    "WithoutClues",
    "Rearrange",
    "summary",
    "theme",
    "paragraph",
    "story",
    "email",
    "graph",
]

# English 2nd paper topics
second_paper_topics = [
    "Article",
    "Preposition",
    "Phrase and Idioms",
    "Completing",
    "Right Forms of Verbs",
    "Narration",
    "Modifiers",
    "Connectors",
    "Synonym and Antonym",
    "Pronoun Reference",
    "Transformation",
    "Punctuation",
    "Application",
    "Report Writing",
    "Paragraph",
]


def create_structure():
    # English 1st paper topicwise
    for topic in first_paper_topics:
        for year in year_folders:
            (base_dir / "HSC" / "English 1st paper" / "Topicwise" / topic / year).mkdir(
                parents=True, exist_ok=True
            )

    # Board folders
    for year in year_folders:
        (base_dir / "HSC" / "Board" / year).mkdir(parents=True, exist_ok=True)

    # BestCollegeAndCadet with dummy files
    cadet_dir = base_dir / "HSC" / "BestCollegeAndCadet"
    cadet_dir.mkdir(parents=True, exist_ok=True)
    for name in ["Abc.docx", "Def.docx", "Ghi.docx"]:
        (cadet_dir / name).touch()

    # English 2nd paper topicwise
    for topic in second_paper_topics:
        for year in year_folders:
            (base_dir / "English 2nd" / "Topicwise" / topic / year).mkdir(
                parents=True, exist_ok=True
            )


create_structure()
print(f"ENGLISH project folder created at: {base_dir}")
