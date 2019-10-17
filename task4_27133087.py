############################################
# The solution is developed by Chengyao Xu #
# Student ID: 27133087                     #
############################################


# define choice function where term is a string indicating what term is being used to
# search and documents is an idf object outlined in Task 3
def choice(term,documents):
    # check is term in the document or not
    assert term in documents.data.keys(), term + "Term is not in documents"
    # get idf from document
    idf = documents.get_IDF(term)
    # get the column of the term form data frame and delete all NaN rows then change it to dictionary
    term_frequency_dic = documents.get_data()[term].dropna().to_dict()
    # calculate TF-IDF for each key in dictionary
    for key in term_frequency_dic.keys():
        term_frequency_dic[key] *= idf
    # finding the book with high TF-IDF value
    all_books = list(term_frequency_dic.keys())
    TFIDF = list(term_frequency_dic.values())
    selected_book = all_books[TFIDF.index(max(TFIDF))]
    return selected_book
