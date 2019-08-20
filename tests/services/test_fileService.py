from unittest import TestCase
from unittest.mock import patch
from services.fileService import FileService


class FileServiceTests(TestCase):
    def setUp(self):
        self.fs = FileService()

    def test_get_search_file_names_should_return_files_in_resources_dir(self):
        expected = ["french_armed_forces.txt", "hitchhikers.txt", "warp_drive.txt"]
        actual = self.fs.get_search_file_names()
        self.assertEqual(expected, actual)

    def test_read_file_should_return_None_if_file_does_not_exist(self):
        self.assertEqual(None, self.fs.read_file("NonExistent"))

    @patch.object(FileService, "get_search_file_names")
    def test_get_search_files_should_return_empty_array_if_files_names_is_empty(self, mock_get_search_file_names):
        mock_get_search_file_names.return_value = []
        result = self.fs.get_search_files()
        self.assertEqual([], result)
