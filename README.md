# api-pydev

API implementation using Flask, currently hosted [here](http://18.222.189.94/books). Check out the examples.

### Problem Statment
We have one file with the name books.csv. The CSV file contains the general information about the
books, like book name, author, year of publication, etc.

1. API will return number of rows requested from the books.csv file.
	- Input : rows=3
	- Output: (JSON)

### Result
![Screenshot_2021-04-04_20:30:38:520](https://user-images.githubusercontent.com/10359228/113512988-f2672600-9584-11eb-9b80-f5af81812f7f.png)

2. 2nd API will give freedom to the user to filter and see any data from the file. The user could
only able to filter from the given column list. If a column is not present then a graceful error
message should return. Even if the API didn’t find any filter response then the user should
get a empty response.
	- Input: Ex. (JSON)
		{"authors":"Jesse Grant"}
	- Output: (JSON)

### Result
![Screenshot_2021-04-04_20:32:20:704](https://user-images.githubusercontent.com/10359228/113512992-f72bda00-9584-11eb-9323-d6399982e794.png)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need these software for this project to install.

```
git
python3
```

### Installing

Follow these steps to get the server running:

First, clone this project using git.
```
git clone https://github.com/mohitsahoo/api-pydev.git
```

Then, cd into the directory and install the required libraries using pip.
```
cd api-pydev/
python3 -m pip install -r requirements.txt
```

Then run it using:
```
python run.py
```

## Running the tests

You can run the unit tests using the `tests.py` file.

To run it simply go to your terminal in the project directory and type this and enter:

```
python tests.py
```

## Deployment

For deployment, we have to move from the default server to a production server. More info on deployment instructions [here](https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/).

For development purposes, you can deploy it using the following command:
```
sudo flask run --host=0.0.0.0 --port=80
```

## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [Flask RESTFul](https://flask-restful.readthedocs.io/en/latest/) - REST API Management

## Authors

* **Mohit Sahoo** - *Initial work* - [(website)](https://mohitsahoo.com/)


## License

This project is unlicensed you're free to copy, modify, publish, use, compile, sell, or
distribute this software - see the [LICENSE.md](LICENSE.md) file for details.
