from flask import Blueprint, jsonify , request, redirect, url_for
from models.Transaction import Transaction, load_transactions
from database import engine
from sqlalchemy.orm import Session

session = Session(engine)
transaction_pages = Blueprint('transaction_pages', __name__, template_folder='templates')

@transaction_pages.route('/transactions')
def get_transactions():
    transactions = load_transactions()
    # If value is null default to expense
    for transaction in transactions:
        if transaction['isExpense'] == None:
            transaction['isExpense'] = True
    return jsonify(transactions)

@transaction_pages.route('/create_transaction', methods=['POST'])
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