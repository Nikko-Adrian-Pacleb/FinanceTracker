from flask import Flask, render_template, jsonify, request, redirect, url_for
from sqlalchemy.orm import Session
from database import engine
from models.Transaction import Transaction, load_transactions
import sys
app = Flask(__name__)

session = Session(engine)

@app.route('/', methods=["GET","POST"])
def get_home():
    transactions = load_transactions()
    return render_template('dashboard.html', transactions=transactions)
                           
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        title = request.form.get('title')
        isExpense = request.form.get('transactionOption') != 'isIncome'
        amount = request.form.get('amount')
        transactionDate = request.form.get('date')

        newTransaction = Transaction(title=title, isExpense=isExpense, amount=amount, transactionDate=transactionDate)
        # return newTransaction.__repr__()
        session.add(newTransaction)
        try:
            session.commit()
        except:
            session.rollback()
        
        return redirect(url_for('get_home'))
    
@app.route('/get_transactions')
def get_transactions():
    transactions = load_transactions()
    # If value is null default to expense
    for transaction in transactions:
        if transaction['isExpense'] == None:
            transaction['isExpense'] = True
    return jsonify(transactions)

def get_table_data():
    data = []  # Initialize an empty list
    transactions = load_transactions()
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