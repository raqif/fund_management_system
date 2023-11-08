from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import uuid

app = Flask(__name__)
# configure sql database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investment_funds.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# define the model
class InvestmentFund(db.Model):
    # id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    id = db.Column(db.Integer, primary_key=True)
    fund_id = db.Column(db.Integer, unique=True, nullable=False)
    fund_name = db.Column(db.String(255), nullable=False)
    fund_manager = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    nav = db.Column(db.Float, nullable=False)
    creation_date = db.Column(db.String(10), nullable=False)
    performance = db.Column(db.Float, nullable=False)

# create the tables in the database
with app.app_context():
    db.create_all()

# Create
# Endpoint to create a new fund
@app.route('/funds', methods=['POST'])
def create_fund():
    data = request.get_json()

    required_fields = ['fund_id', 'fund_name', 'fund_manager', 'description', 'nav', 'creation_date', 'performance']
    for key in required_fields:
        if key not in data:
            return jsonify({'message': f'Missing required field: {key}'}), 400

    new_fund = InvestmentFund(
        fund_id = data.get('fund_id'),
        fund_name = data.get('fund_name'),
        fund_manager = data.get('fund_manager'),
        description = data.get('description'),
        nav = data.get('nav'),
        creation_date = data.get('creation_date'),
        performance = data.get('performance')
    )

    try:
        db.session.add(new_fund)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print("error", e)
        return jsonify({'message': e}), 409

    created_fund = {
        'id' : new_fund.id,
        'fund_id' : new_fund.fund_id,
        'fund_name' : new_fund.fund_name,
        'fund_manager' : new_fund.fund_manager,
        'description' : new_fund.description,
        'nav' : new_fund.nav,
        'creation_date' : new_fund.creation_date,
        'performance' : new_fund.performance
    }

    return jsonify({'message': 'fund added successfully', 'fund': created_fund}), 201

# Read All
# Endpoint to retrieve a list of all funds
@app.route('/funds', methods=['GET'])
def get_all_funds():
    funds = InvestmentFund.query.all()
    fund_list = []
    for fund in funds:
        fund_list.append({
            'id' : fund.id,
            'fund_id' : fund.fund_id,
            'fund_name' : fund.fund_name,
            'fund_manager' : fund.fund_manager,
            'description' : fund.description,
            'nav' : fund.nav,
            'creation_date' : fund.creation_date,
            'performance' : fund.performance
        })

    return jsonify({'funds': fund_list}), 200

# Read One
# Endpoint to retrieve details of a specific fund using its ID
@app.route('/funds/<int:fund_id>', methods=['GET'])
def get_fund_by_id(fund_id):
    fund = InvestmentFund.query.get(fund_id)
    if not fund:
        return jsonify({'message': 'fund not found'}), 404

    fund_data = {
        'id' : fund.id,
        'fund_id' : fund.fund_id,
        'fund_name' : fund.fund_name,
        'fund_manager' : fund.fund_manager,
        'description' : fund.description,
        'nav' : fund.nav,
        'creation_date' : fund.creation_date,
        'performance' : fund.performance
    }

    return jsonify({'fund': fund_data}), 200

# Update
# Endpoint to update the performance of a fund using its ID
@app.route('/funds/<int:fund_id>', methods=['PUT'])
def update_fund_performance(fund_id):
    fund = InvestmentFund.query.get(fund_id)
    if not fund:
        return jsonify({'message': 'fund not found'}), 404

    data = request.get_json()

    required_fields = ['performance']
    for key in required_fields:
        if key not in data:
            return jsonify({'message': f'Missing required field: {key}'}), 400

    fund.performance = data.get('performance')

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
        return jsonify({'message': 'Error updating fund'}), 500

    updated_fund = {
        'id' : fund.id,
        'fund_id' : fund.fund_id,
        'fund_name' : fund.fund_name,
        'fund_manager' : fund.fund_manager,
        'description' : fund.description,
        'nav' : fund.nav,
        'creation_date' : fund.creation_date,
        'performance' : fund.performance
    }

    return jsonify({'message': 'fund updated successfully', "fund": updated_fund}), 200


# Delete
# Endpoint to delete a fund using its ID
@app.route('/funds/<int:fund_id>', methods=['DELETE'])
def delete_fund(fund_id):
    fund = InvestmentFund.query.get(fund_id)
    if not fund:
        return jsonify({'message': 'fund not found'}), 404

    db.session.delete(fund)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
        return jsonify({'message': 'Error deleting fund'}), 500

    deleted_fund = {
        'id' : fund.id,
        'fund_id' : fund.fund_id,
        'fund_name' : fund.fund_name,
        'fund_manager' : fund.fund_manager,
        'description' : fund.description,
        'nav' : fund.nav,
        'creation_date' : fund.creation_date,
        'performance' : fund.performance
    }

    return jsonify({'message': 'fund deleted successfully', 'fund': deleted_fund}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5004)