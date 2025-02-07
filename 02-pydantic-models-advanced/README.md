## Python FastAPI - Pydantic Models Advanced

### Dependencies
```shell
python3 -m venv venv
./venv/bin/pip install --upgrade pip 
./venv/bin/pip install fastapi uvicorn bcrypt 'pydantic[email]'
```

### Run Locally
```shell
./venv/bin/python main.py

INFO:     Started server process [55267]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://localhost:8000 (Press CTRL+C to quit)
```

### Test API
#### Swagger UI
```
http://localhost:8000
```

#### cURL
Create a user
```shell
curl -X 'POST' \
  'http://localhost:8000/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "John Doe",
  "age": 42,
  "email": "foobar@example.com",
  "sensitive": "foobar"
}'
```

Get user data
```shell
export USER_ID="..."

curl -X 'GET' \
  "http://localhost:8000/users/${USER_ID}" \
  -H 'accept: application/json'
```

Get raw user data
```shell
export USER_ID="..."

curl -X 'GET' \
  "http://localhost:8000/users/raw/${USER_ID}" \
  -H 'accept: application/json'
```
