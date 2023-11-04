from flask import Flask, render_template, jsonify, request, redirect, url_for
from database import engine
from sqlalchemy.orm import Session
from models.Transaction import Transaction, load_transactions
from routes.transactionRoutes import transaction_pages
import sys

app = Flask(__name__)

session = Session(engine)

app.register_blueprint(transaction_pages)

@app.route('/', methods=["GET","POST"])
def get_home():
    transactions = load_transactions()
    return render_template('dashboard.html', transactions=transactions)  

# This is for the D3 example
@app.route('/get_data')
def get_data():
    # Process and prepare your data
    data = [{"label": "A", "value": 50}, {"label": "B", "value": 20}, {"label": "C", "value": 15}]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)