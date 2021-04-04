import csv
from flask_restful import reqparse, fields


# request parser for query parameters
get_parser = reqparse.RequestParser()
get_parser.add_argument("rows", type=int, required=True, help="Please pass a valid `rows` query parameter.")


class Page(fields.Raw):
    """ custom fields for marshalling pages properly """

    def format(self, value):
        return int(value) if value else None  # if no page present return null


# marshalling resources for uniform responses
books_fields = {
    "id": fields.Integer,
    "title": fields.String,
    "author": fields.String,
    "authors": fields.String,
    "isbn13": fields.Integer,
    "isbn10": fields.String,
    "price": fields.String,
    "publisher": fields.String,
    "pubyear": fields.Integer,
    "subjects": fields.String,
    "lexile": fields.String,
    "pages": Page,
    "dimensions": fields.String,
}


def load_books():
    """Loads the csv file from books.csv

    Args:
    None

    Returns:
    list<dict> : returns a list of book objects

    """
    with open("common/books.csv", encoding="utf-8") as f:
        return [x for x in csv.DictReader(f)]


def filter_books(books, filters):
    """filters out the books with no matching attributes

    Args:
    books (list<dict>): The whole books list.
    filters (dict): A dictionary containing the attributes to match the books for.

    Returns:
    books (list<dict>): The filtered list of the books.
    """

    filters = list(filters.items())
    # print(filters, filters[0][0], filters[0][1])
    for attr in filters:
        books = [
            x for x in books if x[attr[0]].lower() == (attr[1].lower() if type(attr[1]) == str else attr[1])
        ]  # list comprehension for matching the attributes
        if not books:  # if no book(s) found return empty list
            return []
    return books
