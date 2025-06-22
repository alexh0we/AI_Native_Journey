import json
import os

DATA_FILE = "habits.json" # Assumes the file is in the same directory

def load_data():
    """Handles loading habits from the JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

# Example of how you might test this function:
if __name__ == "__main__":
    # To test, you would need a 'habits.json' file in this directory
    habits = load_data()
    print("Loaded habits:")
    print(habits) 