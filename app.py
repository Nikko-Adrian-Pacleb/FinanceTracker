import datetime 
from flask import Flask, render_template, jsonify, request, redirect, url_for
from database import engine
from sqlalchemy import create_engine, text
app = Flask(__name__)

# def load_transactions_from_db():
#     with engine.connect() as conn:
#         result = conn.execute(text("select * from transactions"))

#         transactions = []
#         for row in result:
#             transactions.append(dict(row._mapping))
#         return transactions
transactions=[]

@app.route('/', methods=["GET","POST"])
def get_home():
    # transactions = load_transactions_from_db()
    return render_template('dashboard.html', transactions=transactions)
                           
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        title = request.form.get('title')
        amount = request.form.get('amount')
        date = request.form.get('date')
        transactions.append({'title': title, 'amount': amount, 'transactionDate': date})
        return redirect(url_for('get_home'))
    
@app.route('/get_data')
def get_data():
    # Process and prepare your data
    data = [{"label": "A", "value": 50}, {"label": "B", "value": 20}, {"label": "C", "value": 15}]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)