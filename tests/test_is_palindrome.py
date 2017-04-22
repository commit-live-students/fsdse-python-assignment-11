from unittest import TestCase
from errors import incorrect_output, no_function_found, succeed


class TestIs_palindrome(TestCase):
    def test_is_palindrome(self):
        try:
            from pallindrome import is_palindrome
        except ImportError:
            self.assertFalse(no_function_found("is_palindrome"))

        try:
            self.assertEqual(True, is_palindrome("helloolleh"))
            self.assertTrue(succeed("test cases are passed"))
        except:
            self.assertFalse(incorrect_output("incorrect output"))
