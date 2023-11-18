from flask import Flask, render_template, jsonify, request, redirect, url_for
from database import engine
from sqlalchemy.orm import Session
from models.Transaction import Transaction
from routes.transactionRoutes import transaction_pages
import sys

app = Flask(__name__)

session = Session(engine)

app.register_blueprint(transaction_pages, url_prefix='/transaction')
# app.register_blueprint(transaction_pages)

@app.route('/', methods=["GET","POST"])
def get_home():
    transactions = session.query(Transaction).all()
    return render_template('dashboard.html', transactions=transactions)  

def get_table_data():
    data = []  # Initialize an empty list
    transactions = session.query(Transaction).all()
    # You should adapt this part to match the structure of your table
    for transaction in transactions:
        # Assuming 'transactions' is a list of dictionaries
        # Access 'isExpense' using dictionary key
        item = {
            "label": transaction.get('isExpense', True),  # Default to True if 'isExpense' is not present
            "value": transaction.get('amount', 0.0)  # Default to 0.0 if 'amount' is not present
        }
        data.append(item)
    return data

# This is for the D3 example
@app.route('/get_data')
def get_data():
    data = get_table_data()  # Get data from the table
    return jsonify(data)  # Return the data as JSON

if __name__ == '__main__':
    app.run(debug=True)