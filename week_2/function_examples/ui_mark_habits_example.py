from datetime import date, timedelta

# Core logic functions required by the UI function below

def core_mark_habit(habit_data, today):
    """Logic to update a single habit's progress."""
    yesterday = str(today - timedelta(days=1))
    today_str = str(today)

    if habit_data["last_done"] == today_str:
        return habit_data, "Already marked for today."
    
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

# The UI function itself

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

# Example of how you might test this function:
if __name__ == "__main__":
    my_habits = {
        "drink water": {"total": 10, "streak": 3, "last_done": "2023-10-25"},
        "read a book": {"total": 5, "streak": 5, "last_done": str(date.today() - timedelta(days=1))}
    }
    print("Marking today's habits...")
    updated_habits = ui_mark_habits(my_habits)
    print("\nUpdated progress:")
    print(updated_habits) 