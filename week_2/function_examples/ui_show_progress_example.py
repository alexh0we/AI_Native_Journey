def ui_show_progress(habits):
    """Handles the output for displaying habit progress."""
    print("\n--- Your Habit Progress ---")
    if not habits:
        print("You haven't added any habits yet. Add one to get started!")
    for habit, data in habits.items():
        print(f"- {habit}: Total Completions: {data['total']}, Current Streak: {data['streak']} days")
    print("--------------------------")

# Example of how you might test this function:
if __name__ == "__main__":
    my_habits = {
        "drink water": {"total": 10, "streak": 3, "last_done": "2023-10-25"},
        "read a book": {"total": 5, "streak": 5, "last_done": "2023-10-26"}
    }
    
    print("Showing progress for sample data:")
    ui_show_progress(my_habits)

    print("\nShowing progress for empty data:")
    ui_show_progress({}) 