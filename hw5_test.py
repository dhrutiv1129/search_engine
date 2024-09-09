'''
Dhruti Vadlamudi
'''

from cse163_utils import assert_equals
from cse163_utils import normalize_paths
import math
from document import Document
from search_engine import SearchEngine


def test_search():
    '''
    This method tests the search function of the SearchEngine class.
    '''
    e1 = SearchEngine('test_corpus')
    e2 = SearchEngine('my_test_corpus')
    # Test normal - test_corpus
    expected = normalize_paths(['test_corpus/document3.txt', 'test_corpus/document2.txt'])
    assert_equals(expected, normalize_paths(e1.search('like')))
    # Test normal - my_test_corpus
    expected = normalize_paths(['my_test_corpus/test3.txt', 'my_test_corpus/test1.txt'])
    assert_equals(expected, normalize_paths(e2.search('in')))
    # Test empty
    assert_equals([], normalize_paths(e2.search(' ')))
    # Test numbers
    expected = normalize_paths(['my_test_corpus/test4.txt'])
    assert_equals(expected, normalize_paths(e2.search('3')))
    # Test punctuation
    expected = normalize_paths(['my_test_corpus/test6.txt'])
    assert_equals(expected, normalize_paths(e2.search('%')))
    

def test_tf():
    '''
    Tests the TF function in Document.
    '''
    e1 = SearchEngine('test_corpus')
    e2 = SearchEngine('my_test_corpus')
    # Test normal - test_corpus
    assert_equals(1/3, Document('test_corpus/document1.txt').term_frequency('love'))
    # Test normal - my_test_corpus
    assert_equals(6/159, Document('my_test_corpus/test1.txt').term_frequency('it'))
    # Test empty
    assert_equals(0, Document('my_test_corpus/test5.txt').term_frequency(''))
    # Tests same word throughout all document
    assert_equals(1, Document('my_test_corpus/test2.txt').term_frequency('like'))
    # Tests word doesn't exist
    assert_equals(0, Document('my_test_corpus/test2.txt').term_frequency('Dhruti'))


def test_idf():
    '''
    Tests the IDF function in SearchEngine.
    '''
    e1 = SearchEngine('test_corpus')
    e2 = SearchEngine('my_test_corpus')
    # Tests normal - test_corpus
    assert_equals(math.log(4/2), e1._calculate_idf('like'))
    # Test normal - my_test_corpus
    assert_equals(math.log(7/2), e2._calculate_idf('like'))
    # Tests empty
    assert_equals(0, e1._calculate_idf(' '))
    # Tests no such value in engine
    assert_equals(0, e2._calculate_idf('Iknowforafactthatthisisnotintheengine'))
    # Tests normalized term
    assert_equals(math.log(7/1), e2._calculate_idf('i'))


def test_get_words():
    '''
    Tests get_words in Document.
    '''
    e1 = SearchEngine('test_corpus')
    e2 = SearchEngine('my_test_corpus')
    # Tests normal
    expected = ['random', 'small', 'line']
    assert_equals(expected, Document('my_test_corpus/test7.txt').get_words())
    # Tests empty
    assert_equals([], Document('my_test_corpus/test5.txt').get_words())
    # Tests numbers
    expected = ['5236542345', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    assert_equals(expected, Document('my_test_corpus/test4.txt').get_words())
    # Tests punctuation
    expected = ['', '', '', '', '', '', '', '']
    assert_equals(expected, Document('my_test_corpus/test6.txt').get_words())

def test_get_path():
    '''
    Tests get_path in Document.
    '''
    e1 = SearchEngine('test_corpus')
    e2 = SearchEngine('my_test_corpus')
    # Tests normal
    assert_equals('my_test_corpus/test1.txt', Document('my_test_corpus/test1.txt').get_path())
    
if __name__ == "__main__":
    test_search()
    test_tf()
    test_idf()
    test_get_words()
    test_get_path()
    print("All tests passed!")