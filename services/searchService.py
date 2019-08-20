import re

from services.fileService import FileService


class SearchService:
    def __init__(self):
        pass

    def simple_string_search(self, search_term):
        search_files = FileService.get_search_files()
        for search_file in search_files:
            search_file.searchTerm = search_term
            search_file.occurrences = self.conduct_simple_string_search(search_term, search_file.fileBuffer)

        return search_files

    def regular_expression_search(self, search_term):
        search_files = FileService.get_search_files()
        for search_file in search_files:
            search_file.searchTerm = search_term
            search_file.occurrences = self.conduct_regular_expression_search(search_term, search_file.fileBuffer)

        return search_files

    def index_search(self, search_term):
        pass

    def build_search_index(self):
        pass

    @staticmethod
    def conduct_simple_string_search(search_term, buffer_to_search):
        return buffer_to_search.count(search_term)

    @staticmethod
    def conduct_regular_expression_search(search_term, buffer_to_search):
        return len(re.findall(search_term, buffer_to_search))
