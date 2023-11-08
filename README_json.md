# fund_management_system

task 1-3 referred to app_json.py & investment_funds.json
task 4,6 referred to app_sql.py & investment_funds.db
task 5 referred to migration_scrip.py and check_migration.py
task 7 referred to test_app_sql.py
task 8 referred to README_json and README_sql

read README_json first before README_sql.
run app_json.py first, before app_sql.py

curl -X GET http://localhost:5001/funds

## setup, run and testing

1. clone the repository.
2. create env: `conda create --name aham` and activate: `conda activate aham`
3. install requirements: `pip3 install -r requirements.txt`
4. run the API flask server: `python3 app_json.py`
5. open another terminal to manually check API run using curl commands provided and check request and response examples.

## API endpoints

### 1. add a fund
method: POST
path: /funds
request example:
```
curl -X POST \
  http://localhost:5001/funds \
  -H 'Content-Type: application/json' \
  -d '{
    "fund_id" : 12345,
    "fund_name" : "raqif_invest",
    "fund_manager" : "raqif",
    "description" : "raqif investment",
    "nav" : 1.11,
    "creation_date" : 12345,
    "performance" : 1.00
}'
```
response example:
```
{
  "creation_date": 12345,
  "description": "raqif investment",
  "fund_id": 12345,
  "fund_manager": "raqif",
  "fund_name": "raqif_invest",
  "id": 0,
  "nav": 1.11,
  "performance": 1.0
}
```

### 2. get all funds

method: GET
path: /funds
request example:
```
curl -X GET http://localhost:5001/funds
```
response example:
```
[
  {
    "creation_date": 12345,
    "description": "raqif investment",
    "fund_id": 12345,
    "fund_manager": "raqif",
    "fund_name": "raqif_invest",
    "id": 0,
    "nav": 1.11,
    "performance": 1.0
  },
  {
    "creation_date": 12345,
    "description": "mahat investment",
    "fund_id": 12346,
    "fund_manager": "mahat",
    "fund_name": "mahat_invest",
    "id": 1,
    "nav": 1.12,
    "performance": 1.02
  }
]
```
### 3. get a specific fund
method: GET
path: /funds/:id (Replace :id with the fund ID)
request example:
```
curl -X GET http://localhost:5001/funds/1
```
response example:
```
{
  "creation_date": 12345,
  "description": "mahat investment",
  "fund_id": 12346,
  "fund_manager": "mahat",
  "fund_name": "mahat_invest",
  "id": 1,
  "nav": 1.12,
  "performance": 1.02
}
```

### 4. update a fund
method: PUT
path: /funds/:id (Replace :id with the fund ID)
request example:
```
curl -X PUT \
  http://localhost:5001/funds/1 \
  -H 'Content-Type: application/json' \
  -d '{
    "performance": 0.01
}'
```

response example:
```
{
  "creation_date": 12345,
  "description": "mahat investment",
  "fund_id": 12346,
  "fund_manager": "mahat",
  "fund_name": "mahat_invest",
  "id": 1,
  "nav": 1.12,
  "performance": 0.01
}
```

### 5. delete a fund
method: DELETE
path: /funds/:id (Replace :id with the fund ID)
request example:
```
curl -X DELETE http://localhost:5001/funds/1
```
response example:
```
{
  "deleted_fund": {
    "creation_date": 12345,
    "description": "mahat investment",
    "fund_id": 12346,
    "fund_manager": "mahat",
    "fund_name": "mahat_invest",
    "id": 1,
    "nav": 1.12,
    "performance": 0.01
  },
  "message": "Fund deleted successfully"
}
```

## manual curl examples

### 1. get initial list of funds

request example:
```
curl -X GET http://localhost:5001/funds
```
response example:
```
[]
```

### 2. add the first fund
request example:
```
curl -X POST \
  http://localhost:5001/funds \
  -H 'Content-Type: application/json' \
  -d '{
    "fund_id" : 12345,
    "fund_name" : "raqif_invest",
    "fund_manager" : "raqif",
    "description" : "raqif investment",
    "nav" : 1.11,
    "creation_date" : 12345,
    "performance" : 1.00
}'
```
response example:
```
{
  "creation_date": 12345,
  "description": "raqif investment",
  "fund_id": 12345,
  "fund_manager": "raqif",
  "fund_name": "raqif_invest",
  "id": 0,
  "nav": 1.11,
  "performance": 1.0
}
```

### 3. add a second fund
request example:
```
curl -X POST \
  http://localhost:5001/funds \
  -H 'Content-Type: application/json' \
  -d '{
    "fund_id" : 12346,
    "fund_name" : "mahat_invest",
    "fund_manager" : "mahat",
    "description" : "mahat investment",
    "nav" : 1.12,
    "creation_date" : 12345,
    "performance" : 1.02
}'
```
response example:
```
{
  "creation_date": 12345,
  "description": "mahat investment",
  "fund_id": 12346,
  "fund_manager": "mahat",
  "fund_name": "mahat_invest",
  "id": 1,
  "nav": 1.12,
  "performance": 1.02
}
```

### 4. get all funds
request example:
```
curl -X GET http://localhost:5001/funds
```
response example:
```
[
  {
    "creation_date": 12345,
    "description": "raqif investment",
    "fund_id": 12345,
    "fund_manager": "raqif",
    "fund_name": "raqif_invest",
    "id": 0,
    "nav": 1.11,
    "performance": 1.0
  },
  {
    "creation_date": 12345,
    "description": "mahat investment",
    "fund_id": 12346,
    "fund_manager": "mahat",
    "fund_name": "mahat_invest",
    "id": 1,
    "nav": 1.12,
    "performance": 1.02
  }
]
```

### 5. get a specific fund
request example:
```
curl -X GET http://localhost:5001/funds/1
```
response example:
```
{
  "creation_date": 12345,
  "description": "mahat investment",
  "fund_id": 12346,
  "fund_manager": "mahat",
  "fund_name": "mahat_invest",
  "id": 1,
  "nav": 1.12,
  "performance": 1.02
}
```

### 6. update a fund
request example:
```
curl -X PUT \
  http://localhost:5001/funds/1 \
  -H 'Content-Type: application/json' \
  -d '{
    "performance": 0.01
}'
```

response example:
```
{
  "creation_date": 12345,
  "description": "mahat investment",
  "fund_id": 12346,
  "fund_manager": "mahat",
  "fund_name": "mahat_invest",
  "id": 1,
  "nav": 1.12,
  "performance": 0.01
}
```


### 7. delete a fund
request example:
```
curl -X DELETE http://localhost:5001/funds/1
```
response example:
```
{
  "deleted_fund": {
    "creation_date": 12345,
    "description": "mahat investment",
    "fund_id": 12346,
    "fund_manager": "mahat",
    "fund_name": "mahat_invest",
    "id": 1,
    "nav": 1.12,
    "performance": 0.01
  },
  "message": "Fund deleted successfully"
}
```

### 8. get all funds after deleted
request example:
```
curl -X GET http://localhost:5001/funds
```
response example:
```
[
  {
    "creation_date": 12345,
    "description": "raqif investment",
    "fund_id": 12345,
    "fund_manager": "raqif",
    "fund_name": "raqif_invest",
    "id": 0,
    "nav": 1.11,
    "performance": 1.0
  }
]
```