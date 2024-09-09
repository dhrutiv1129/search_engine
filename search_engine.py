"""
Dhruti Vadlamudi
"""
import os
from document import Document
import math
from cse163_utils import normalize_token


class SearchEngine:
    '''
    This is the Search Engine class. It uses and goes through documents to
    find the most relevant. It implements Inverse Document Frequency (IDF) to calculate this.
        Has:
    Relative path of directory that contains all of the documents used
    Dictionary that maps terms to a list of documents which have contain
    a term, stored as cache data.
    List of all the documents in the corpus
        Does:
    search(term)
    '''

    def __init__(self, relative_path):
        '''
        Initializer for the Search Engine object
        '''
        self.relative_path = relative_path
        self._dir = os.listdir(relative_path)
        self._files = []
        for file in self._dir:
            # Recieves the full path from the relative path and the file and concatenates them
            abs_path = os.path.join(relative_path, file)
            doc = Document(abs_path)
            self._files.append(doc)
        self._inverted_index = self._inverted_index()

    def _inverted_index(self):
        '''
        Creates an inverted index of the search engine.
        Takes no arguments and returns a dictionary
        '''
        main_dict = {}
        for doc in self._files:
            # Converts to a set in order to eliminate any duplicates
            words = set(doc.get_words())
            for word in words:
                # If term is not already in the dict, sets the term as the key and 
                # creates a new list and adds the document name that contains the term
                if word not in main_dict:
                    main_dict[word] = [doc]
                else:
                    # Adds the document to the list of documents that contain the term
                    if doc not in main_dict[word]:
                        main_dict[word].append(doc)
        return main_dict

    def _calculate_idf(self, term):
        '''
        Calculates the IDF of a specific term
        Takes term as the argument
        Returns the IDF of the term
        '''
        # Checks if not in the inverted index to return 0
        if term not in self._inverted_index:
            return 0
        number_of_docs = len(self._files)
        length_of_idf = len(self._inverted_index[term])
        return math.log(number_of_docs / length_of_idf)

    def search(self, query):
        '''
        Searches for a query in the search engine
        Takes in a query as the argument
        Returns a list of documents ranked by relevance to the query
        '''
        # Creates a list of all words in a query with all special characters removed
        query_list = [normalize_token(word) for word in query.split()]
        query_dict = {}
        for term in query_list:
            # Gets each item from the dictionary and unpacks into 
            # term and list of documents that contain the term
            for doc in self._inverted_index.get(term, list()):
                # Updates the TF-IDF score
                if doc not in query_dict:
                    query_dict[doc] = 0
                tf_idf = self._calculate_idf(term) * doc.term_frequency(term)
                query_dict[doc] += tf_idf
        tf_idf_list = query_dict.items()
        # Sorts the documents by relevance by using lambda with the TF-IDF values
        final_documents = sorted(tf_idf_list, key=lambda x: x[1], reverse=True)
        # Returns the path of each document in the list 
        return [document[0].get_path() for document in final_documents]
