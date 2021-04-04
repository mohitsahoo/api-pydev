import csv
from flask_restful import reqparse, fields


get_parser = reqparse.RequestParser()
get_parser.add_argument("rows", type=int, required=True, help="Please enter a valid number.")


class Page(fields.Raw):
	def format(self, value):
		return int(value) if value else None


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


def parse_list(books):
	return [dict(zip(books_fields.keys(), x)) for x in books]


def load_books():
	with open("common/books.csv", encoding="utf-8") as f:
		return [x for x in csv.reader(f)][1:]


def filter_list(books, filters):
	filters = list(filters.items())
	# print(filters, filters[0][0], filters[0][1])
	for attr in filters:
		books = [x for x in books if x[attr[0]].lower() == (attr[1].lower() if type(attr[1]) == str else attr[1])]
		if not books:
			return []
	return books
