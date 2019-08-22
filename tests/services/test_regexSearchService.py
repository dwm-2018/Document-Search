from unittest import TestCase

from services.fileService import FileService
from services.regexSearchService import RegexSearchService


class RegexSearchServiceTests(TestCase):
    def setUp(self):
        self.rss = RegexSearchService()

    def test_conduct_regular_expression_search_should_find_occurances_of_regexp_in_string(self):
        expected = 1
        test_string = "test string should (1942) a certain test number of test words."
        result = self.rss.conduct_regular_expression_search("\(1942\)", test_string)
        self.assertEqual(expected, result)

    def test_conduct_regular_expression_search_should_do_pattern_matching_in_string(self):
        expected = 2
        test_string = "test lystring should (1942) a certainly test numberly [3] of test words."
        result = self.rss.conduct_regular_expression_search("\w+ly", test_string)
        self.assertEqual(expected, result)

    def test_conduct_regular_expression_search_should_return_0_if_pattern_not_found_in_string(self):
        expected = 0
        test_string = "test lystring should (1942) a certainly test numberly [3] of test words."
        result = self.rss.conduct_regular_expression_search("\w+er\s", test_string)
        self.assertEqual(expected, result)

    # INTEGRATION TEST
    def test_search_should_search_files_using_regex(self):
        search_files = FileService.get_search_files()
        result = self.rss.search("\(\d{4}\)", search_files)
        self.assertEqual(1, len(result))

    def test_search_should_return_empty_array_if_no_result(self):
        search_files = FileService.get_search_files()
        result = self.rss.search("teststringreturnsnothing", search_files)
        self.assertEqual(0, len(result))
