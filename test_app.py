import unittest
from app import change_date_format
from datetime import datetime


class TestDateFormat(unittest.TestCase):
    def test_correctly_converts_data_to_string(self):
        # Test whether the datetime values are being converted into strings

        # Test data
        testDates = [
            {"date_created": datetime(2021, 10, 26)},
            {"date_created": datetime(2020, 5, 17)}]

        # Test function
        modified_testDates = change_date_format(testDates)

        # Test data type equals string
        self.assertEqual(
            type(modified_testDates[0]["date_created"]), type("string"))
        self.assertEqual(
            type(modified_testDates[1]["date_created"]), type("string"))

    def test_string_displays_correct_date(self):
        # Test if the datetime values are being converted into the correct date

        # Test data
        testDates = [
            {"date_created": datetime(2021, 10, 26)},
            {"date_created": datetime(2020, 5, 17)}]

        # Test function
        modified_testDates = change_date_format(testDates)

        # Test data type equals string
        self.assertEqual(modified_testDates[0]["date_created"], "Oct 26 2021")
        self.assertEqual(modified_testDates[1]["date_created"], "May 17 2020")
