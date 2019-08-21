import re


class RegexSearchService:
    def __init__(self):
        pass

    def search(self, search_term, search_files):
        for search_file in search_files:
            search_file.searchTerm = search_term
            search_file.occurrences = self.conduct_regular_expression_search(search_term, search_file.fileBuffer)

        return search_files

    @staticmethod
    def conduct_regular_expression_search(search_term, buffer_to_search):
        return len(re.findall(search_term, buffer_to_search))
