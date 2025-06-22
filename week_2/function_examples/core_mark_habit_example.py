from datetime import date, timedelta

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

# Example of how you might test this function:
if __name__ == "__main__":
    today = date.today()
    yesterday = date.today() - timedelta(days=1)
    
    # Test continuing a streak
    habit_with_streak = {"total": 5, "streak": 2, "last_done": str(yesterday)}
    updated_habit, message = core_mark_habit(habit_with_streak, today)
    print("Continuing streak:", message)
    print(updated_habit)

    # Test starting a new streak
    habit_without_streak = {"total": 5, "streak": 2, "last_done": "2023-01-01"}
    updated_habit, message = core_mark_habit(habit_without_streak, today)
    print("Starting new streak:", message)
    print(updated_habit) 