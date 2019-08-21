
class SimpleSearchService:
    def __init__(self):
        pass

    def search(self, search_term, search_files):
        for search_file in search_files:
            search_file.searchTerm = search_term
            search_file.occurrences = self.conduct_simple_string_search(search_term, search_file.fileBuffer)

        return search_files

    @staticmethod
    def conduct_simple_string_search(search_term, buffer_to_search):
        return buffer_to_search.count(search_term)