import unittest

from helper_functions.keyword_extractor import extract_keywords
from mock_data.mock_data import mock_input


class TestExtractKeywords(unittest.TestCase):

    def test_extract_keywords__entry1__return_success(self):
        expected_count = 1
        expected_data = {"shoulder": expected_count}
        data = extract_keywords(mock_input["entry_1"]["data"])

        self.assertIsNotNone(data)
        self.assertEqual(expected_data, data)

    def test_extract_keywords__entry2__return_success(self):
        expected_count = 3
        expected_data = {"bilateral": expected_count}
        data = extract_keywords(mock_input["entry_2"]["data"])

        self.assertIsNotNone(data)
        self.assertEqual(expected_data, data)

    def test_extract_keywords__entry3__return_success(self):
        expected_count_1 = 1
        expected_count_3 = 3
        expected_data = {"bilateral": expected_count_3, "shoulder": expected_count_1}
        data = extract_keywords(mock_input["entry_3"]["data"])

        self.assertIsNotNone(data)
        self.assertEqual(expected_data, data)
