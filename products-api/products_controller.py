import sqlite3
import pandas as pd

def get_products():
    conn = sqlite3.connect('products_data')
    c = conn.cursor()
    query = "SELECT * FROM products"
    c.execute(query)
    return c.fetchall()

def get_by_id(id):
    conn = sqlite3.connect('products_data')
    c = conn.cursor()
    statement = "SELECT product, timestamp, price FROM products WHERE product=? ORDER BY timestamp DESC LIMIT 60"
    id_products = c.execute(statement,[id]).fetchall()
    all_prices = pd.DataFrame(id_products, columns=['product','timestamp','price'])
    average = all_prices['price'].mean()

    return round(average,2)
