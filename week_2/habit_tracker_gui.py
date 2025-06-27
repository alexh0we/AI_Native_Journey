import tkinter as tk
from tkinter import messagebox, simpledialog
from habit_tracker import load_data, save_data, core_add_habit, core_delete_habit, core_mark_habit, core_reset_streak
from datetime import date

class HabitTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fun Habit Tracker")
        self.habits = load_data()
        self.create_widgets()
        self.refresh_habit_list()

    def create_widgets(self):
        self.frame = tk.Frame(self.root, padx=20, pady=20, bg="#ffe066", bd=0, highlightthickness=0, relief="flat")
        self.frame.pack(fill="both", expand=True)

        self.title = tk.Label(self.frame, text="🌈 Fun Habit Tracker", font=("Arial", 18, "bold"), bg="#ffe066", fg="#ffb3b3")
        self.title.pack(pady=(0, 10))

        self.habit_listbox = tk.Listbox(self.frame, width=40, height=10, font=("Arial", 12), bg="#b3d8f8")
        self.habit_listbox.pack(pady=10)

        self.button_frame = tk.Frame(self.frame, bg="#ffe066", bd=0, highlightthickness=0, relief="flat")
        self.button_frame.pack(pady=5)

        self.add_button = tk.Button(self.button_frame, text="Add Habit", bg="#b3e0ff", command=self.add_habit)
        self.add_button.pack(side="left", padx=5, pady=5)

        self.mark_button = tk.Button(self.button_frame, text="Mark as Done", bg="#b3e0ff", command=self.mark_habit)
        self.mark_button.pack(side="left", padx=5, pady=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Habit", bg="#ffb3b3", command=self.delete_habit)
        self.delete_button.pack(side="left", padx=5, pady=5)

        self.progress_button = tk.Button(self.button_frame, text="Show Progress", bg="#fff9c4", command=self.show_progress)
        self.progress_button.pack(side="left", padx=5, pady=5)

    def refresh_habit_list(self):
        self.habit_listbox.delete(0, tk.END)
        for habit in self.habits:
            self.habit_listbox.insert(tk.END, habit)

    def add_habit(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Habit")
        dialog.configure(bg="#ffe066")
        tk.Label(dialog, text="Enter a new habit to track:", bg="#ffe066").pack(padx=10, pady=10)
        entry = tk.Entry(dialog, bg="#b3d8f8", fg="#fffdfa", font=("Arial", 12))
        entry.pack(padx=10, pady=10)
        entry.focus_set()
        def on_ok():
            habit_name = entry.get()
            if habit_name:
                self.habits, message = core_add_habit(self.habits, habit_name.strip())
                save_data(self.habits)
                self.refresh_habit_list()
                messagebox.showinfo("Add Habit", message)
            dialog.destroy()
        ok_btn = tk.Button(dialog, text="Add", command=on_ok, bg="#b3e0ff")
        ok_btn.pack(pady=(0,10))
        dialog.transient(self.root)
        dialog.grab_set()
        self.root.wait_window(dialog)

    def mark_habit(self):
        selected = self.habit_listbox.curselection()
        if not selected:
            messagebox.showwarning("Mark Habit", "Please select a habit to mark as done.")
            return
        habit = self.habit_listbox.get(selected[0])
        today = date.today()
        updated_data, message = core_mark_habit(self.habits[habit], today)
        self.habits[habit] = updated_data
        save_data(self.habits)
        messagebox.showinfo("Mark Habit", f"For '{habit}': {message}")

    def delete_habit(self):
        selected = self.habit_listbox.curselection()
        if not selected:
            messagebox.showwarning("Delete Habit", "Please select a habit to delete.")
            return
        habit = self.habit_listbox.get(selected[0])
        confirm = messagebox.askyesno("Delete Habit", f"Are you sure you want to delete '{habit}'?")
        if confirm:
            self.habits, message = core_delete_habit(self.habits, habit)
            save_data(self.habits)
            self.refresh_habit_list()
            messagebox.showinfo("Delete Habit", message)

    def show_progress(self):
        if not self.habits:
            messagebox.showinfo("Progress", "You haven't added any habits yet. Add one to get started!")
            return
        progress = "\n".join(
            f"- {habit}: Total: {data['total']}, Streak: {data['streak']} days"
            for habit, data in self.habits.items()
        )
        messagebox.showinfo("Your Habit Progress", progress)

if __name__ == "__main__":
    root = tk.Tk()
    app = HabitTrackerApp(root)
    root.mainloop() 