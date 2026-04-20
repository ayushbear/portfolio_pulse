import json
import os

DB_FILE = 'portfolio.json'

def load_portfolio():
    if not os.path.exists(DB_FILE): return []
    with open(DB_FILE, 'r') as f:
        try: return json.load(f)
        except: return []

def save_portfolio(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)