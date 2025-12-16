#---IMPORTS---#
from tt_gutenberg.data_import import data_importer


#---FUNCTION DEFS---#
def list_authors(by_languages=False, alias=False):
    """
    This functtion returns author aliases ordered by translation count
    """

    if not (by_languages and alias):
        return []

    gutenberg_data = data_importer()

    #filter for authors with a non-null alias
    author_aliases_df = gutenberg_data[gutenberg_data['alias'].notna()].copy()

    #count translations per alias
    translation_count = (
        author_aliases_df
        .groupby('alias')['languages']
        .count()
        .reset_index(name='translation_count')
        .sort_values(by='translation_count', ascending=False)
    )

    #return
    return translation_count['alias'].tolist()
