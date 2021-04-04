from flask import Flask
from flask_restful import Api
from resources.books import Books

app = Flask(__name__)
api = Api(app)


api.add_resource(Books, "/books")

if __name__ == "__main__":
	app.run(debug=True)
