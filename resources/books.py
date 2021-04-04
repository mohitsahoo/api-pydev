from flask import request
from flask_restful import Resource, abort, marshal_with
from common.utils import get_parser, parse_list, books_fields, load_books, filter_list

library = load_books()


class Books(Resource):
	@marshal_with(books_fields, envelope="books")
	def get(self):
		args = get_parser.parse_args()
		if args.rows < 0:
			abort(404, message="Number of rows should be a positive number.")
		elif args.rows == 0:
			return []
		return parse_list(library[: args.rows])

	@marshal_with(books_fields, envelope="books")
	def post(self):
		filters = request.form
		for x in filters:
			if x not in books_fields:
				abort(404, message=f"Invalid column: `{x}`")
				break
		return filter_list(parse_list(library), filters)
