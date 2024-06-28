import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# PostgreSQL configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tanggal = db.Column(db.String(10), nullable=False)
    keterangan = db.Column(db.String(255), nullable=False)
    debit = db.Column(db.Float, nullable=True)
    kredit = db.Column(db.Float, nullable=True)
    saldo = db.Column(db.Float, nullable=False)

@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = Transaction.query.all()
    return jsonify([{
        'id': t.id,
        'tanggal': t.tanggal,
        'keterangan': t.keterangan,
        'debit': t.debit,
        'kredit': t.kredit,
        'saldo': t.saldo
    } for t in transactions])

@app.route('/transactions', methods=['POST'])
def add_transaction():
    data = request.json['data']
    # Here, you would process the input data and create a new transaction
    # For simplicity, we'll just create a dummy transaction
    new_transaction = Transaction(
        tanggal='2024-06-28',
        keterangan=data,
        debit=1000.00,
        kredit=None,
        saldo=6500.00
    )
    db.session.add(new_transaction)
    db.session.commit()
    return jsonify({'message': 'Transaction added successfully'}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
