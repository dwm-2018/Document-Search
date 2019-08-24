import time
from random import choice

from services.fileService import FileService
from services.indexSearchService import IndexSearchService
from services.regexSearchService import RegexSearchService
from services.simpleSearchService import SimpleSearchService
from services.utils import has_non_alphanumeric


class PerformanceService:
    def __init__(self):
        pass

    def evaluate(self):
        search_files = FileService.get_search_files()
        iss = IndexSearchService()
        search_index = iss.build_search_index(search_files)
        terms = self.get_terms_from_search_index(search_index)
        print("Running performance tests:\n")

        self.run_simple_search_test(terms, search_files)
        self.run_regex_search_test(terms, search_files)
        self.run_index_search_test(terms, search_index)

    @staticmethod
    def run_simple_search_test(terms, search_files):
        start_time_ms = int(round(time.time() * 1000))

        for x in range(2000000):
            sss = SimpleSearchService()
            sss.search(choice(terms), search_files)

        end_time_ms = int(round(time.time() * 1000))

        print("Simple Search Elapsed Time: {ex_time}ms".format(ex_time=end_time_ms - start_time_ms))

    @staticmethod
    def run_regex_search_test(terms, search_files):
        start_time_ms = int(round(time.time() * 1000))

        for x in range(2000000):
            rss = RegexSearchService()
            term = choice(terms)
            while has_non_alphanumeric(term):
                term = choice(terms)
            rss.search(term, search_files)

        end_time_ms = int(round(time.time() * 1000))

        print("Regular Expression Search Elapsed Time: {ex_time}ms".format(ex_time=end_time_ms - start_time_ms))

    @staticmethod
    def run_index_search_test(terms, search_index):
        start_time_ms = int(round(time.time() * 1000))

        for x in range(2000000):
            iss = IndexSearchService()
            iss.search(choice(terms), search_index)

        end_time_ms = int(round(time.time() * 1000))

        print("Index Search Elapsed Time: {ex_time}ms".format(ex_time=end_time_ms - start_time_ms))

    @staticmethod
    def get_terms_from_search_index(search_index):
        return [*search_index]
