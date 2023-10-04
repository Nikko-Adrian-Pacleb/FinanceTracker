import datetime 
from flask import Flask, render_template
app = Flask(__name__)

transactions = [
    {
        'TransactionID': '1',
        'TransactionDate': datetime.datetime(2020, 1, 1),
        'TransactionAmount': 1000,
    },
    {
        'TransactionID': '2',
        'TransactionDate': datetime.datetime(2020, 1, 2),
        'TransactionAmount': 2000,
    },
    {
        'TransactionID': '3',
        'TransactionDate': datetime.datetime(2020, 1, 1),
        'TransactionAmount': 3000,
    }

]

@app.route('/')
def hello_geek():
    return render_template('index.html', 
                           transactions=transactions,
                           title='Home')


if __name__ == "__main__":
    app.run(debug=True)