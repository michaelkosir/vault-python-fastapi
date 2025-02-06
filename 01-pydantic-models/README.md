## Python FastAPI - Pydantic Models

### Dependencies
```shell
python3 -m venv venv
./venv/bin/pip install --upgrade pip 
./venv/bin/pip install fastapi uvicorn
```

### Run Locally
```shell
./venv/bin/python main.py

INFO:     Started server process [55267]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://localhost:8000 (Press CTRL+C to quit)
```

### Automatic Documentation
FastAPI includes two documentation user interfaces automatically.
```
# Swagger UI
http://localhost:8000/docs

# ReDoc UI
http://localhost:8000/redoc
```

You can set the Swagger UI URL with the parameter `docs_url`. You can disable it by setting `docs_url=None`.

You can set the ReDoc URL with the parameter `redoc_url`. You can disable it by setting `redoc_url=None`.

```python
# ...

app = FastAPI(docs_url="/", redoc_url=None)

# ...
```