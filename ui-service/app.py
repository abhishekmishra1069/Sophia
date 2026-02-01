import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)
LOGIC_URL = os.getenv('LOGIC_URL', 'http://logic-service:5001')

@app.route('/', methods=['GET', 'POST'])
def index():
    price_data = None
    if request.method == 'POST':
        symbol = request.form.get('symbol')
        response = requests.get(f"{LOGIC_URL}/price/{symbol}")
        price_data = response.json()
    return render_template('index.html', data=price_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)