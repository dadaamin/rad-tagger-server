## Installation
```bash
conda create -n tagger python=3.9
pip install -r requirements.txt
```

## Run
Run server on localhost:
```bash
python -m flask run
curl -X POST http://127.0.0.1:5000/tag -H "Content-Type: application/json" -d '{"text":"Hello, lung!"}'
```

