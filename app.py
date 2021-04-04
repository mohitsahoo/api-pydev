from flask import Flask
from flask_restful import Api
from resources.books import Books


app = Flask(__name__)  # Flask intialization
api = Api(app)  # API intialization


api.add_resource(Books, "/books")  # api url

if __name__ == "__main__":
    app.run(debug=True)
