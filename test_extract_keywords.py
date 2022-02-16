import unittest

from keyword_extractor import extract_keywords


class TestExtractKeywords(unittest.TestCase):

    def test_extract_keywords(self):
        expected_data = {"shoulder": 1}
        data = extract_keywords()

        self.assertIsNotNone(data)
        self.assertEqual(expected_data, data)
