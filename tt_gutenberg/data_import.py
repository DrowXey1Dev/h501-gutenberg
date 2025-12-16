#---IMPORTS---#
import pandas as pd


#-----FUNCTION DEFS-----#
def data_importer():
    """
    This function imports the data set
    """
    target_url = (
        "https://raw.githubusercontent.com/"
        "rfordatascience/tidytuesday/main/data/2025/2025-06-03/"
        "gutenberg_authors.csv"
    )

    return pd.read_csv(target_url)
