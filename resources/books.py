from flask import request
from flask_restful import Resource, abort, marshal_with
from common.utils import get_parser, books_fields, load_books, filter_books

library = load_books()


class Books(Resource):
    @marshal_with(books_fields, envelope="books")
    def get(self):  # GET request handling
        args = get_parser.parse_args()
        if args.rows < 0:
            abort(
                404, message="Number of rows should be a positive number."
            )  # abort if query for rows is less than 0
        elif args.rows == 0:
            return []  # return empty list if query for rows is 0
        return library[: args.rows]

    @marshal_with(books_fields, envelope="books")
    def post(self):  # POST request handling
        filters = request.form
        for x in filters:
            if x not in books_fields:
                abort(404, message=f"Invalid column: `{x}`")  # abort with an error message if column not found
        return filter_books(library, filters)
