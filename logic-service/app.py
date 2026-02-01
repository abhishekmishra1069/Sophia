import os
import psycopg2
import requests
from flask import Flask, jsonify

app = Flask(__name__)

# Database connection details from environment variables
DB_HOST = os.getenv('DB_HOST', 'postgres-db')
DB_NAME = os.getenv('DB_NAME', 'stockdb')
DB_USER = os.getenv('DB_USER', 'user')
DB_PASS = os.getenv('DB_PASS', 'pass')

def get_db_connection():
    return psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)

@app.route('/price/<symbol>')
def get_stock(symbol):
    symbol = symbol.upper()
    conn = get_db_connection()
    cur = conn.cursor()

    # 1. Check DB first
    cur.execute("SELECT price FROM stock_prices WHERE symbol = %s", (symbol,))
    row = cur.fetchone()

    if row:
        price = float(row[0])
    else:
        # 2. Mock Internet Search (Real apps would use a Finance API here)
        price = 100.0 + (50.0 * (sum(ord(c) for c in symbol) % 10) / 10.0)
        
        # 3. Store in DB
        cur.execute("INSERT INTO stock_prices (symbol, price) VALUES (%s, %s)", (symbol, price))
        conn.commit()

    cur.close()
    conn.close()
    return jsonify({"symbol": symbol, "price": price})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)