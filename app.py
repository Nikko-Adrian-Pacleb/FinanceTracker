import datetime 
from flask import Flask, render_template
from database import engine
from sqlalchemy import create_engine, text
app = Flask(__name__)

def load_transactions_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from transactions"))

        transactions = []
        for row in result:
            transactions.append(dict(row._mapping))
        return transactions

@app.route('/', methods=["GET","POST"])
def get_home():
    transactions = load_transactions_from_db()
    return render_template('dashboard.html',
                           transactions=transactions
                            )

if __name__ == "__main__":
    app.run(debug=True)