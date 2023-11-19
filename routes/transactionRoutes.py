from flask import Blueprint, jsonify , request, redirect, url_for
from models.Transaction import Transaction
from database import engine
from sqlalchemy.orm import Session

# --- Contents --- #
# Setup
# Routes List
# -- /transactions
# -- /<id>
# -- /create_transaction


# --- Setup --- #
session = Session(engine)
transaction_pages = Blueprint('transaction_pages', __name__, template_folder='templates')

# --- Routes List --- #
@transaction_pages.route('/transactions')
def get_transactions():
    transactions = session.query(Transaction).order_by(Transaction.transactionDate.desc(), Transaction.id.desc()).all()
    transactionJSON = []
    for t in transaction:
        transactionJSON.append(t.__json__())

    return jsonify(transactionJSON)

@transaction_pages.route('/<id>')
def get_transaction(id):
    transaction = session.query(Transaction).filter(Transaction.id == id).first()
    if transaction is None:
        return jsonify({'error': 'Transaction not found'}), 404
    return jsonify(transaction.__json__())

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
    

