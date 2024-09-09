"""
Dhruti Vadlamudi
Intermediate Data Programming
"""
from cse163_utils import normalize_token


class Document:
    '''
    The Document object is responsible for handling each word inside the document.
    It is also responsible for handling the Term Frequency (TF) of each term
        Has:
    Relative path of document
    Dictionary that maps terms in the document to their TF. This is stored as cache data.
        Does:
    get_words()
    term_frequency(term)
    get_path()
    '''

    def __init__(self, path):
        '''
        Initializer for the Document object
        '''
        self._relative_path = path
        self._term_frequency = {}
        self._make_tf()

    def _make_tf(self):
        '''
        Initializes term frequency for each term.
        Takes in no arguments and returns nothing.
        '''
        words = self.get_words()
        size = len(words)
        for word in words:
            if word not in self._term_frequency:
                # Number of times the given term occurs divided by total words in a document
                # 0 if word not in document
                self._term_frequency[word] = words.count(word) / size if size > 0 else 0

    def term_frequency(self, term):
        '''
        Returns term frequency of a term.
        It takes term as the argument.
        '''
        # 0 is set as the default value if the term is not in the document
        return self._term_frequency.get(normalize_token(term), 0)

    def get_words(self):
        '''
        Returns a list of words in the document.
        '''
        with open(self._relative_path) as f:
            # Adds all words in a document to a list with all special characters removed
            return [normalize_token(word) for word in f.read().split()]

    def get_path(self):
        '''
        Returns the relative path of the document
        '''
        return self._relative_path
