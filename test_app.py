import unittest
from app import app, change_date_format
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


class TestFlaskRouting(unittest.TestCase):

    # executed before each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    # executed after each test
    def tearDown(self):
        pass

    # test the status code 200 when rendering routes
    def test_status_code_is_200(self):
        response = self.app.get('/home', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # test the correct template is being rendered
    def test_correct_template_is_rendered(self):
        response = self.app.get('/home', follow_redirects=True)
        self.assertIn(
            b"FIND THE BEST RECIPES TO FUEL YOUR PERFORMANCE", response.data)


if __name__ == "__main__":
    unittest.main()
