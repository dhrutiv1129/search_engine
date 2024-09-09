'''
Dhruti Vadlamudi
'''

from search_engine import SearchEngine


def main():
    # Gets directory and builds search engine
    directory = input('Please enter the name of a directory: ')
    print('Building Search Engine...')
    engine = SearchEngine(directory)
    print()
    while True:
        query = input('Enter a search term to query (Enter=Quit): ')
        # Enter handled
        if query == '':
            print('Thank you for searching.')
            break
        document_list = engine.search(query)
        print("Displaying results for '" + query + "':")
        if len(document_list) == 0:
            print('    No results :(')
        else:
            # Creates a shortened list that only contains the first 10 results of a search query
            trunc_doc = document_list[:10]
            for document in trunc_doc:
                index = trunc_doc.index(document) + 1
                print('    ' + str(index) + ". " + document)
            print()


if __name__ == '__main__':
    main()
