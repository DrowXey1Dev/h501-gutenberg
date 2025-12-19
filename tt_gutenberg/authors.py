from tt_gutenberg.data_import import load_datasets


def list_authors(by_languages=False, alias=False):
    """
    This function return a list of author aliases sorted by the number of unique
    languages their works have been translated into.

    inputs: by_languages, and alias (if by_languages is true we compute the author rankings based on the number of unique languages associated with their works)
    (if alias is trueu then we use author aliases instead of author names)

    outputs: returns a list of author aliases sorted in descending order by translation count
    """

    #only proceed if both flags are explicitly enabled
    if not (by_languages and alias):
        return []

    #load the Gutenberg datasets
    authors, metadata, languages = load_datasets()

    #remove rows with missing alias data (cleaning)
    authors = authors[authors["alias"].notna()]

    #merge authors with metadata using the author ID
    #this associates each author alias with their works
    am = authors.merge(
        metadata,
        on="gutenberg_author_id",
        how="inner"
    )

    #merge metadata with language information using the Gutenberg work ID
    aml = am.merge(
        languages[["gutenberg_id", "language"]],
        on="gutenberg_id",
        how="inner",
        suffixes=("_meta", "_lang")
    )

    #count the number of uniqeue languages per author aliase
    counts = (
        aml.groupby("alias")["language_lang"]
        .nunique()
        .reset_index(name="translation_count")
        .sort_values("translation_count", ascending=False)
    )

    #return the sorted list of author aliases
    return counts["alias"].tolist()
