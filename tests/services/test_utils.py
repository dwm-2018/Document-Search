from unittest import TestCase

from services.utils import print_result


class UtilsTests(TestCase):
    def setUp(self):
        pass

    def test_print_result_should_print_result(self):
        test_result = [{'file_name': 'test_file.txt', 'occurences': 2},
                       {'file_name': 'test_file_2.txt', 'occurences': 5},
                       {'file_name': 'test_file_3.txt', 'occurences': 1}]
        result = print_result(test_result)
        self.assertTrue(True)
