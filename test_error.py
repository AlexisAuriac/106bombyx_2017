import unittest
from error import error


class ErrorTest(unittest.TestCase):
    def test_len(self):
        arg = ["1", "1", "1", "1"]
        self.assertEqual(error(arg), 84)
        arg = []
        self.assertEqual(error(arg), 84)

    def test_badTypes(self):
        arg = ["aze", "1"]
        self.assertEqual(error(arg), 84)
        arg.append(3)
        self.assertEqual(error(arg), 84)

    def test_k(self):
        arg = ["10", "5.5"]
        self.assertEqual(error(arg), 84)
        arg = ["10", "0"]
        self.assertEqual(error(arg), 84)

    def test_start_end(self):
        arg = ["10", "100", "90"]
        self.assertEqual(error(arg), 84)