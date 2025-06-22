from datetime import date

def core_reset_streak(habit_data, today):
    """Logic to reset a habit's streak if not done."""
    if habit_data["last_done"] != str(today):
        habit_data["streak"] = 0
    return habit_data

# Example of how you might test this function:
if __name__ == "__main__":
    today = date.today()
    
    # Habit that needs its streak reset
    habit_to_reset = {"total": 5, "streak": 3, "last_done": "2023-01-01"}
    updated_habit = core_reset_streak(habit_to_reset, today)
    print("Habit after reset check:", updated_habit)

    # Habit that was done today, streak should not reset
    habit_done_today = {"total": 6, "streak": 4, "last_done": str(today)}
    updated_habit_no_reset = core_reset_streak(habit_done_today, today)
    print("Habit done today:", updated_habit_no_reset) 