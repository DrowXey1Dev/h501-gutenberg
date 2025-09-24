#---IMPORTS---#
from data_import import data_importer


#---FUNCTION DEFS---#
def author_aliases_retriever():
    #retrieve aliases and sort based off num taranslations

    gutenberg_data = data_importer()

    #test code
    #print(gutenberg_data.head())
    
    
    #filter for authors with a non null alias
    author_aliases_df = gutenberg_data[gutenberg_data['alias'].notna()].copy()

    #count translations for each 
    translation_count = author_aliases_df.groupby('alias')['gutenberg_author_id'].count().reset_index()
    translation_count.columns = ['alias', 'translation_count']

    #sort aliases by translation count in descending order
    sorted_aliases_df = translation_count.sort_values(
        by = 'translation_count', 
        ascending = False
    )

    #convert the sorted column to list
    sorted_aliases_list = sorted_aliases_df['alias'].tolist()
    
    
    return sorted_aliases_list


#---MAIN---# (temporary main)

print(author_aliases_retriever())

    


