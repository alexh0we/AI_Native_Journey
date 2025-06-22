def core_add_habit(habits, habit_name):
    """Logic to add a new habit."""
    if habit_name and habit_name not in habits:
        habits[habit_name] = {"total": 0, "streak": 0, "last_done": ""}
        return habits, f"Added habit: {habit_name}"
    return habits, "Habit already exists or is invalid."

# Example of how you might test this function:
if __name__ == "__main__":
    my_habits = {"read": {"total": 5, "streak": 2, "last_done": "2023-10-25"}}
    
    # Test adding a new habit
    updated_habits, message = core_add_habit(my_habits, "exercise")
    print(message)
    print("Updated habits:", updated_habits)
    
    # Test adding an existing habit
    updated_habits, message = core_add_habit(my_habits, "read")
    print(message)
    print("Updated habits:", updated_habits) 