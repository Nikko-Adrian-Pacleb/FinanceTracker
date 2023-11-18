from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import select
from sqlalchemy import String, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text
from database import engine

class Transaction(declarative_base()):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    isExpense = Column(Boolean)
    title = Column(String(255))
    amount = Column(Integer)
    transactionDate = Column(String(255))

    def __json__(self):
        return {
            'id': self.id,
            'isExpense': self.isExpense,
            'title': self.title,
            'amount': self.amount,
            'transactionDate': self.transactionDate
        }

    def __repr__(self):
        return "<Transaction(title='%s', isExpense=%s amount='%s', transactionDate='%s')>" % (
            self.title, self.isExpense, self.amount, self.transactionDate)

# Commented due to TransactionRoute code changes
# def load_transactions():
#     with engine.connect() as conn:
#         result = conn.execute(text("select * from transactions order by transactionDate desc"))

#         transactions = []
#         for row in result:
#             transactions.append(dict(row._mapping))
#         return transactions

