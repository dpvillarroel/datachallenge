import pandas as pd
import sqlite3

# DATA CHALLENGE PART 1

def write_db():

    # Read json and convert to a DataFrame
    data = pd.read_json('price_payload.json')

    #If we want to drop de NaN values 
    #data = data.dropna()

    # Create database
    conn = sqlite3.connect('products_data')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS products (product number, timestamp text , price number)')
    conn.commit()

    #Write into database

    data.to_sql('products', conn, if_exists='replace', index = False)

    return "Products Updated"


