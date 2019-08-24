from unittest import TestCase

from services.utils import print_result, has_non_alphanumeric, remove_non_alphanumeric


class UtilsTests(TestCase):
    def setUp(self):
        pass

    def test_print_result_should_print_result(self):
        test_result = [{'file_name': 'test_file.txt', 'occurences': 2},
                       {'file_name': 'test_file_2.txt', 'occurences': 5},
                       {'file_name': 'test_file_3.txt', 'occurences': 1}]
        result = print_result(test_result)
        self.assertTrue(True)

    def test_has_non_alphanumeric_should_return_true_if_nonalphanumeric_exists(self):
        self.assertTrue(has_non_alphanumeric("nonalphanumeric!"))

    def test_has_non_alphanumeric_should_return_false_if_only_alphanumeric_exists(self):
        self.assertFalse(has_non_alphanumeric("alphanumeric"))

    def test_remove_non_alphanumeric_should_return_only_alphanumerics(self):
        test = "alp]ha!nume.rics"
        expected = "alphanumerics"
        result = remove_non_alphanumeric(test)
        self.assertEqual(expected, result)