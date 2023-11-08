import requests
import time
import uuid

BASE_URL = 'http://localhost:5004'

def test_clear_fund_before_testing():
    response = requests.get(f'{BASE_URL}/funds')
    print(response)
    response_json = response.json()
    print(response_json)
    funds = response_json['funds']

    print(funds)
    for fund in funds:
        fund_id = fund['id']
        response_delete = requests.delete(f'{BASE_URL}/funds/{fund_id}')
        print(response_delete)

def test_create_fund():
    new_fund = {
        'fund_id' : 1,
        'fund_name' : 'raqif_invest',
        'fund_manager' : 'raqif',
        'description' : 'raqif investment',
        'nav' : 1.11,
        'creation_date' : int (time.time()),
        'performance' : 1.00
    }

    response = requests.post(f'{BASE_URL}/funds', json=new_fund)
    # print('wasap', response.json())
    data = response.json()
    assert response.status_code == 201
    assert data['fund']['fund_id'] == new_fund['fund_id']

def test_get_all_funds():
    response = requests.get(f'{BASE_URL}/funds')
    assert response.status_code == 200
    assert 'funds' in response.json()

def test_get_fund():
    response = requests.get(f'{BASE_URL}/funds/1')
    data = response.json()
    print("test_get_fund", data)
    assert response.status_code == 200
    assert 'fund' in response.json()
    assert data['fund']['id'] == 1

def test_update_fund():
    updated_fund = {
        'fund_id' : int (time.time()),
        'fund_name' : 'raqif_invest',
        'fund_manager' : 'raqif',
        'description' : 'raqif investment (updated)',
        'nav' : 0.11,
        'performance' : 0.01
    }

    response = requests.put(f'{BASE_URL}/funds/1', json=updated_fund)
    data = response.json()
    print(data)
    assert response.status_code == 200
    assert data['fund']['performance'] == 0.01

def test_delete_fund():
    response = requests.delete(f'{BASE_URL}/funds/1')
    response2 = requests.get(f'{BASE_URL}/funds/1')
    # print("test_delete_fund", response2.json())

    assert response.status_code == 200
    assert response2.status_code == 404

if __name__ == '__main__':
    test_clear_fund_before_testing()
    test_create_fund()
    test_get_all_funds()
    test_get_fund()
    test_update_fund()
    test_delete_fund()
    print('all tests passed!')
