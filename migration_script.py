from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investment_funds.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class InvestmentFund(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fund_id = db.Column(db.Integer, unique=True, nullable=False)
    fund_name = db.Column(db.String(255), nullable=False)
    fund_manager = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    nav = db.Column(db.Float, nullable=False)
    creation_date = db.Column(db.String(10), nullable=False)
    performance = db.Column(db.Float, nullable=False)

def migrate_data():
    with open('investment_funds.json') as file:
        data = json.load(file)

    with app.app_context():
        db.create_all()

        for fund_data in data:
            new_fund = InvestmentFund(
                fund_id=fund_data['fund_id'],
                fund_name=fund_data['fund_name'],
                fund_manager=fund_data['fund_manager'],
                description=fund_data['description'],
                nav=fund_data['nav'],
                creation_date=fund_data['creation_date'],
                performance=fund_data['performance']
            )
            db.session.add(new_fund)

        db.session.commit()

if __name__ == '__main__':
    migrate_data()
