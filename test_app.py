import unittest
from app import date_format
from datetime import datetime


class TestDateFormat(unittest.TestCase):
    def testDateType(self):
        # Test whether the datetime values are being converted into strings

        # Test data
        testDates = [
            {"date_created": datetime.today()},
            {"date_created": datetime(2020, 5, 17)}]

        # Test function
        date_format(testDates)

        # Test data type equals string
        self.assertEqual(type(testDates[0]["date_created"]), type("string"))
        self.assertEqual(type(testDates[1]["date_created"]), type("string"))

    def testCorrectDate(self):
        # Test if the datetime values are being converted into the correct date

        # Test data
        testDates = [
            {"date_created": datetime.today()},
            {"date_created": datetime(2020, 5, 17)}]

        # Test function
        date_format(testDates)

        # Test data type equals string
        self.assertEqual(testDates[0]["date_created"], "Jan 05 2021")
        self.assertEqual(testDates[1]["date_created"], "May 17 2020")
