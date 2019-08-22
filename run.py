from services.fileService import FileService
from services.indexSearchService import IndexSearchService
from services.regexSearchService import RegexSearchService
from services.simpleSearchService import SimpleSearchService

if __name__ == "__main__":
    search_files = FileService.get_search_files()
    search_term = input("Enter the search term: ")
    search_type = input("1) String Match 2) Regular Expression 3) Indexed")

    if search_type == 1:
        sss = SimpleSearchService()
        result = sss.search(search_term, search_files)
        print(result)
    elif search_type == 2:
        rss = RegexSearchService()
        result = rss.search(search_term, search_files)
        print(result)
    elif search_type == 3:
        iss = IndexSearchService()
        search_index = iss.build_search_index(search_files)
        result = iss.search(search_term, search_index)
        print(result)


def print_result(result):
    for entry in result:
        print(key + " - " + value for (key, value) in entry)