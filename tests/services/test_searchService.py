from unittest import TestCase

from services.searchService import SearchService


class SearchServiceTests(TestCase):
    def setUp(self):
        self.ss = SearchService()

    def test_conduct_simple_string_search_should_find_occurances_of_substring_in_string(self):
        expected = 5
        test_string = "test string should testreturntest a certain test number of test words."
        result = self.ss.conduct_simple_string_search("test", test_string)
        self.assertEqual(expected, result)

    # INTEGRATION TEST
    def test_simple_string_search_should_search_files_for_terms(self):
        result = self.ss.simple_string_search("works")
        self.assertEqual(0, result[0].occurrences)
        self.assertEqual(0, result[1].occurrences)
        self.assertEqual(1, result[2].occurrences)
