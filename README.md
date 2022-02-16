# Data Engineer Challenge

Service that connects to the database and has an endpoint that returns the 60 days average price per product

## Getting Started 🚀

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites 📋

What things you need to install.

```
pip install Flask
pip install pandas

```

### Running ⚙️

A step by step  how to get a the challenge running.

Go to the products-api folder. And run main.py 

```
python3 main.py
```

This will redirect you to your localhost  http://127.0.0.1:8000/

## Running the tests ⚙️

Part 1 of the challenge is in productsDB.py. To see all the products and their price go to  http://127.0.0.1:8000/


Part 2: The endpoint to try the api is the url from your localhost/product/id. For example:

```
http://127.0.0.1:8000/product/39688874

```

## Database 📌

How to connect to the database:

```
conn = sqlite3.connect('products_data')
c = conn.cursor()

```

Table name is *products* and structure:

| product| timestamp | price |
| ------------- | ------------- |------------ |
| number  | text  | number  |
|39688874 | "2021-10-31 13:03:46" | 34.89  |

## Built With

* [Flask](https://flask.palletsprojects.com/en/2.0.x/quickstart/) - The framework used


## Authors

* **Daniela Villlarroel** - *Data Challenge* - [Github](https://github.com/dpvillarroel/datachallenge)




