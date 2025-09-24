#---IMPORTS---#
import pandas as pd


#---HEADER---#
pd.options.display.max_rows = 100  # default is 60 rows


#-----FUNCTION DEFS-----#

def data_importer():
    #set target dataset url
    target_url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv'
    #pull data in
    gutenberg_authors = pd.read_csv(target_url)
    

    return gutenberg_authors

