# example

Example for DECODE - simple echo message server

## Running the example

### Prepare the environment

```
python -m venv venv

venv/Scripts/activate              (Windows)
source venv/Scripts/activate       (Unix/macOS)

pip install -r requirements.txt
```

### Run the example

```
fastapi dev main.py
```

### Play around

Few calls
- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- [http://127.0.0.1:8000/echo/Hello%20world](http://127.0.0.1:8000/echo/Hello%20world)
