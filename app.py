import csv
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("rows", type=int, required=True)


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


def load_books():
	with open("books.csv", encoding="utf-8") as f:
		return [x for x in csv.reader(f)][1:]


def parse_list(books):
	return [dict(zip(books_fields.keys(), x)) for x in books]


class Books(Resource):
	@marshal_with(books_fields, envelope="books")
	def get(self):

		args = parser.parse_args()
		if args.rows < 0:
			abort(404, message="Number of rows should be a positive number.")
		elif args.rows == 0:
			return {"books": []}
		return parse_list(library[: args.rows])


api.add_resource(Books, "/books")

if __name__ == "__main__":
	library = load_books()
	app.run(debug=True)
