from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# Load data from JSON file if it exists
def load_data():
    if os.path.exists('investment_funds.json'):
        with open('investment_funds.json') as file:
            return json.load(file)
    else:
        with open('investment_funds.json', 'w') as file:
            json.dump([], file)
            return []

# create data to JSON file
def create_data(new_fund, investment_funds):
    max_id = 0
    with open('investment_funds.json') as file:
        data_file = json.load(file)
        print('file', data_file)
        for fund in data_file:
            print('fund', fund)
            fund_id = fund.get('id')
            if fund_id == max_id:
                max_id += 1
        new_fund['id'] = max_id
        print(new_fund)
    investment_funds.append(new_fund)
    save_data(investment_funds)

# save data to JSON file
def save_data(investment_funds):
    with open('investment_funds.json', 'w') as file:
        json.dump(investment_funds, file, indent=2)

# Load initial data
investment_funds = load_data()

# Endpoint to retrieve a list of all funds
@app.route('/funds', methods=['GET'])
def get_all_funds():
    return jsonify(investment_funds)

# Endpoint to create a new fund
@app.route('/funds', methods=['POST'])
def create_fund():
    data = request.get_json()
    new_fund = {
        'fund_id': data.get('fund_id'),
        'fund_name': data.get('fund_name'),
        'fund_manager': data.get('fund_manager'),
        'description': data.get('description'),
        'nav': data.get('nav'),
        'creation_date': data.get('creation_date'),
        'performance': data.get('performance')
    }
    create_data(new_fund, investment_funds)
    return jsonify(new_fund), 201

# Endpoint to retrieve details of a specific fund using its ID
@app.route('/funds/<int:fund_id>', methods=['GET'])
def get_fund_by_id(fund_id):
    # print('investment_funds', investment_funds)
    for fund in investment_funds:
        print('fund', fund)
        if fund['id'] == fund_id:
            return jsonify(fund)
    return jsonify({'error': 'fund not found'}), 404

# Endpoint to update the performance of a fund using its ID
@app.route('/funds/<int:fund_id>', methods=['PUT'])
def update_fund(fund_id):
    specific_fund = {}
    for fund in investment_funds:
        print('fund', fund)
        print(fund['id'] == fund_id, fund_id)
        if fund['id'] == fund_id:
            specific_fund = fund

    if specific_fund:
        print('true')
        data = request.get_json()
        specific_fund['performance'] = data.get('performance')
        save_data(investment_funds)
        return jsonify(specific_fund)
    return jsonify({'error': 'Fund not found'}), 404

# Endpoint to delete a fund using its ID
@app.route('/funds/<int:fund_id>', methods=['DELETE'])
def delete_fund(fund_id):
    deleted_fund = {}
    for fund in investment_funds:
        print('fund', fund)
        if fund['id'] == fund_id:
            deleted_fund = fund
            investment_funds.remove(fund)
            print('investment_funds', investment_funds)
            save_data(investment_funds)
            break

    return jsonify({'message': 'Fund deleted successfully', 'deleted_fund': deleted_fund})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
