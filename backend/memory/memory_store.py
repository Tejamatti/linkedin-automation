import json, os

MEMORY_PATH = "memory/profiles.json"

def load_memory():
    if not os.path.exists(MEMORY_PATH):
        return {}
    with open(MEMORY_PATH, "r") as f:
        return json.load(f)

def save_memory(data):
    with open(MEMORY_PATH, "w") as f:
        json.dump(data, f, indent=2)

def add_profile(profile_id, data):
    memory = load_memory()
    memory[profile_id] = data
    save_memory(memory)
