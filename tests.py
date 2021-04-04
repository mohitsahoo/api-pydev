import unittest

from app import app
from common import utils


class TestApi(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

    def test_books_get(self):
        """ Test that books api works"""
        response = self.app.get("/books?rows=5")
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json.get("books"))

    def test_books_bad_rows(self):
        """ Test that we get error on negative rows"""
        response = self.app.get("/books?rows=-5")
        self.assertEqual(response.status_code, 404)
        self.assertIsNone(response.json.get("books"))

    def test_books_zero_rows(self):
        """ Test that we get no books when row is 0"""
        response = self.app.get("/books?rows=0")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json["books"]), 0)

    def test_books_invalid_column(self):
        """ Test that we get invalid column error when bad column is sent"""
        response = self.app.post("/books", data={"badcolumn": 0})
        self.assertEqual(response.status_code, 404)
        self.assertIsNone(response.json.get("books"))
        self.assertIn("invalid column", str(response.data).lower())

    def test_books_filter(self):
        """ Test that we get proper data through books api data filter"""
        response = self.app.post("/books", data={"id": 1})
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json.get("books"))
        self.assertEqual(response.json.get("books")[0]["id"], 1)

    def test_utils(self):
        """ Test that the utils module is working properly"""
        books = utils.load_books()
        self.assertNotEqual(len(books), 0)  # books are not empty

        books = utils.filter_books(books, {"author": "barbara parisi"})
        self.assertIsNotNone(books)


if __name__ == "__main__":
    unittest.main()
