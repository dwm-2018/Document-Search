from unittest import TestCase

from services.fileService import FileService


class FileServiceTests(TestCase):
    def setUp(self):
        self.fs = FileService()

    def test_get_search_files_should_return_files_in_resources_dir(self):
        expected = ["french_armed_forces.txt", "hitchhikers.txt", "warp_drive.txt"]
        actual = self.fs.get_search_files()
        self.assertEqual(expected, actual)
