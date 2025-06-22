import json

DATA_FILE = "habits.json" # Assumes the file is in the same directory

def save_data(habits):
    """Handles saving habits to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(habits, f, indent=2)
    print(f"Data saved to {DATA_FILE}")

# Example of how you might test this function:
if __name__ == "__main__":
    sample_habits = {
        "drink water": {"total": 10, "streak": 3, "last_done": "2023-10-26"},
        "read a book": {"total": 5, "streak": 5, "last_done": "2023-10-26"}
    }
    save_data(sample_habits) 