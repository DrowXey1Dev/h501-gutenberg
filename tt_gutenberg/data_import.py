import pandas as pd

"""
This function loads the data

inputs: nothing
outputs: returns the authors, metadata, and languages CSV files
"""
def load_datasets():
    authors_url = (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03/gutenberg_authors.csv"
    )

    metadata_url = (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03/gutenberg_metadata.csv"
    )

    languages_url = (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03/gutenberg_languages.csv"
    )

    #assign each loaded CSV to a variable and return it
    authors = pd.read_csv(authors_url)
    metadata = pd.read_csv(metadata_url)
    languages = pd.read_csv(languages_url)

    return authors, metadata, languages
