from flask import jsonify
from models.Transaction import load_transactions
from app import app

@app.route('/transactions')
def get_transactions():
    transactions = load_transactions()
    # If value is null default to expense
    for transaction in transactions:
        if transaction['isExpense'] == None:
            transaction['isExpense'] = True
    return jsonify(transactions)