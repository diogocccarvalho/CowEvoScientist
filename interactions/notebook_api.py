import json
import os

NOTEBOOK_FILE = "assets/notebook/manual.json"

def load_notebook():
    if not os.path.exists(NOTEBOOK_FILE)
        return {}

    with open(NOTEBOOK_FILE, "r") as f:
        return json.load(f)

def write(entry_id, data):
    notebook = load_notebook()
    notebook[entry_id] = data
    save_notebook