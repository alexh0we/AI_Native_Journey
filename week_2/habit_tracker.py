import json
import os
from datetime import date, timedelta

# --- Data Persistence Functions (I/O) ---
DATA_FILE = "week_2/habits.json"

def load_data():
    """Handles loading habits from the JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(habits):
    """Handles saving habits to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(habits, f, indent=2)

# --- Core Logic Functions (No I/O) ---

def core_add_habit(habits, habit_name):
    """Logic to add a new habit."""
    if habit_name and habit_name not in habits:
        habits[habit_name] = {"total": 0, "streak": 0, "last_done": ""}
        return habits, f"Added habit: {habit_name}"
    return habits, "Habit already exists or is invalid."

def core_delete_habit(habits, habit_name):
    """Logic to delete a habit."""
    if habit_name in habits:
        deleted_habit = habits.pop(habit_name)
        return habits, f"Deleted habit: {habit_name} (Total completions: {deleted_habit['total']}, Final streak: {deleted_habit['streak']})"
    return habits, f"Habit '{habit_name}' not found. Available habits: {', '.join(habits.keys()) if habits else 'none'}"

def core_mark_habit(habit_data, today):
    """Logic to update a single habit's progress."""
    yesterday = str(today - timedelta(days=1))
    today_str = str(today)

    if habit_data["last_done"] == today_str:
        return habit_data, f"Already marked for today."
    
    habit_data["total"] += 1
    if habit_data["last_done"] == yesterday:
        habit_data["streak"] += 1
    else:
        habit_data["streak"] = 1
    habit_data["last_done"] = today_str
    return habit_data, f"Great job! Current streak: {habit_data['streak']}"

def core_reset_streak(habit_data, today):
    """Logic to reset a habit's streak if not done."""
    if habit_data["last_done"] != str(today):
        habit_data["streak"] = 0
    return habit_data

# --- User Interface (UI) Functions (Handles I/O) ---

def ui_add_habit(habits):
    """Handles the user input and output for adding a habit."""
    habit_name = input("Enter a new habit to track: ").strip()
    updated_habits, message = core_add_habit(habits, habit_name)
    print(message)
    return updated_habits

def ui_mark_habits(habits):
    """Handles the user input and output for marking habits."""
    today = date.today()
    for habit, data in habits.items():
        response = input(f"Did you complete '{habit}' today? (y/n): ").strip().lower()
        if response == 'y':
            updated_data, message = core_mark_habit(data, today)
            habits[habit] = updated_data
            print(f"For '{habit}': {message}")
        else:
            habits[habit] = core_reset_streak(data, today)
    return habits

def ui_show_progress(habits):
    """Handles the output for displaying habit progress."""
    print("\n--- Your Habit Progress ---")
    if not habits:
        print("You haven't added any habits yet. Add one to get started!")
    for habit, data in habits.items():
        print(f"- {habit}: Total Completions: {data['total']}, Current Streak: {data['streak']} days")
    print("--------------------------")

def ui_delete_habit(habits):
    """Handles the user input and output for deleting a habit."""
    if not habits:
        print("No habits to delete. Add some habits first!")
        return habits
    
    print("\n--- Your Current Habits ---")
    for habit in habits.keys():
        print(f"- {habit}")
    print("--------------------------")
    
    habit_name = input("Enter the name of the habit to delete: ").strip()
    if not habit_name:
        print("No habit name provided.")
        return habits
    
    # Check if habit exists before asking for confirmation
    if habit_name not in habits:
        print(f"Habit '{habit_name}' not found. Please check the spelling and try again.")
        return habits
    
    # Ask for confirmation only if habit exists
    confirm = input(f"Are you sure you want to delete '{habit_name}'? This cannot be undone. (y/n): ").strip().lower()
    if confirm == 'y':
        updated_habits, message = core_delete_habit(habits, habit_name)
        print(message)
        return updated_habits
    else:
        print("Deletion cancelled.")
        return habits

def main():
    """Main function to run the habit tracker application."""
    habits = load_data()
    while True:
        print("\nHabit Tracker Menu:")
        print("1. Add a new habit")
        print("2. Mark habits for today")
        print("3. Show progress")
        print("4. Delete a habit")
        print("5. Exit")
        print("\nYou can use numbers (1-5) or type the option name (e.g., 'add', 'mark', 'show', 'delete', 'exit')")
        choice = input("Choose an option: ").strip().lower()

        if choice in ["1", "add a new habit", "add"]:
            habits = ui_add_habit(habits)
            save_data(habits)
        elif choice in ["2", "mark habits for today", "mark"]:
            habits = ui_mark_habits(habits)
            save_data(habits)
        elif choice in ["3", "show progress", "show"]:
            ui_show_progress(habits)
        elif choice in ["4", "delete a habit", "delete"]:
            habits = ui_delete_habit(habits)
            save_data(habits)
        elif choice in ["5", "exit"]:
            save_data(habits)
            print("Goodbye! Keep up the good habits!")
            break
        else:
            print("Invalid choice. Please try again.")
            print("You can use: 1/add, 2/mark, 3/show, 4/delete, 5/exit")

if __name__ == "__main__":
    main()
