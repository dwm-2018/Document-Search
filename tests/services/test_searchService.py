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

    def test_conduct_regular_expression_search_should_find_occurances_of_regexp_in_string(self):
        expected = 1
        test_string = "test string should (1942) a certain test number of test words."
        result = self.ss.conduct_regular_expression_search("\(1942\)", test_string)
        self.assertEqual(expected, result)

    def test_conduct_regular_expression_search_should_do_pattern_matching_in_string(self):
        expected = 2
        test_string = "test lystring should (1942) a certainly test numberly [3] of test words."
        result = self.ss.conduct_regular_expression_search("\w+ly", test_string)
        self.assertEqual(expected, result)

    def test_conduct_regular_expression_search_should_return_0_if_pattern_not_found_in_string(self):
        expected = 0
        test_string = "test lystring should (1942) a certainly test numberly [3] of test words."
        result = self.ss.conduct_regular_expression_search("\w+er\s", test_string)
        self.assertEqual(expected, result)

    # INTEGRATION TEST
    def test_simple_string_search_should_search_files_for_terms(self):
        result = self.ss.simple_string_search("works")
        self.assertEqual(0, result[0].occurrences)
        self.assertEqual(0, result[1].occurrences)
        self.assertEqual(1, result[2].occurrences)

    def test_regular_expression_search_search_should_search_files_using_regex(self):
        result = self.ss.regular_expression_search("\(\d{4}\)")
        self.assertEqual(1, result[0].occurrences)
        self.assertEqual(0, result[1].occurrences)
        self.assertEqual(0, result[2].occurrences)
