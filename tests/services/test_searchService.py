from unittest import TestCase

from services.searchService import SearchService


class SearchServiceTests(TestCase):
    def setUp(self):
        self.ss = SearchService()

    def test_simple_string_search_should_load_search_files_into_memory(self):
        pass
