# This is an example of a UI function that handles user I/O
# and calls a core logic function to perform the main task.

def core_add_habit(habits, habit_name):
    """Logic to add a new habit."""
    if habit_name and habit_name not in habits:
        habits[habit_name] = {"total": 0, "streak": 0, "last_done": ""}
        return habits, f"Added habit: {habit_name}"
    return habits, "Habit already exists or is invalid."

def ui_add_habit(habits):
    """Handles the user input and output for adding a habit."""
    habit_name = input("Enter a new habit to track: ").strip()
    updated_habits, message = core_add_habit(habits, habit_name)
    print(message)
    return updated_habits

# Example of how you might test this function:
if __name__ == "__main__":
    my_habits = {}
    print("Let's add a habit.")
    my_habits = ui_add_habit(my_habits)
    print("Current habits:", my_habits)
    
    print("\nLet's add another one.")
    my_habits = ui_add_habit(my_habits)
    print("Current habits:", my_habits) 