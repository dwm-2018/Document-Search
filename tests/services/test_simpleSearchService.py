from unittest import TestCase

from services.fileService import FileService
from services.simpleSearchService import SimpleSearchService


class SimpleSearchServiceTests(TestCase):
    def setUp(self):
        self.sss = SimpleSearchService()

    def test_conduct_simple_string_search_should_find_occurances_of_substring_in_string(self):
        expected = 5
        test_string = "test string should testreturntest a certain test number of test words."
        result = self.sss.conduct_simple_string_search("test", test_string)
        self.assertEqual(expected, result)

    # INTEGRATION TEST
    def test_simple_string_search_should_search_files_for_terms(self):
        search_files = FileService.get_search_files()
        result = self.sss.search("works", search_files)
        self.assertEqual(1, len(result))
