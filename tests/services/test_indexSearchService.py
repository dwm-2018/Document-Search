from unittest import TestCase

from services.fileService import FileService
from services.indexSearchService import IndexSearchService


class IndexSearchServiceTests(TestCase):
    def setUp(self):
        self.iss = IndexSearchService()

    def test_add_word_to_dict_should_create_new_entry_if_none_exists(self):
        test_index = {'test1': 1, 'test2': 1, 'test3': 1}
        expected = {'test1': 1, 'test2': 1, 'test3': 1, 'test4': 1}
        result = self.iss.add_word_to_dict('test4', test_index)
        self.assertEqual(expected, result)

    def test_add_word_to_dict_should_increment_count_if_entry_exists(self):
        test_index = {'test1': 1, 'test2': 1, 'test3': 1}
        expected = {'test1': 1, 'test2': 1, 'test3': 2}
        result = self.iss.add_word_to_dict('test3', test_index)
        self.assertEqual(expected, result)

    def test_add_inverted_index_to_master_index_should_create_new_entries_in_master(self):
        master_index = {}
        inverted_index = {'test1': 1, 'test2': 1, 'test3': 1}
        expected = {'test1': [{'test_file': 1}], 'test2': [{'test_file': 1}], 'test3': [{'test_file': 1}]}
        result = self.iss.add_inverted_index_to_master_index(master_index, inverted_index, 'test_file')
        self.assertEqual(expected, result)

    def test_add_inverted_index_to_master_index_should_merge_inverted_index_into_master(self):
        master_index = {'test1': [{'test_file': 1}], 'test2': [{'test_file': 1}], 'test3': [{'test_file': 1}]}
        inverted_index = {'test3': 5, 'test4': 4}
        expected = {'test1': [{'test_file': 1}], 'test2': [{'test_file': 1}], 'test3': [{'test_file': 1}, {'test_file_2': 5}], 'test4': [{'test_file_2': 4}]}
        result = self.iss.add_inverted_index_to_master_index(master_index, inverted_index, 'test_file_2')
        self.assertEqual(expected, result)

    # INTEGRATION TESTS
    def test_build_inverted_index_should_build_index_from_string_buffer(self):
        search_files = FileService.get_search_files()
        result = self.iss.build_inverted_index(search_files[0].fileBuffer)
        self.assertEqual(349, len(result))