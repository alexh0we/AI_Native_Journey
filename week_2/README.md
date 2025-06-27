# Habit Tracker

A simple and intuitive habit tracking application built in Python with both command-line interface (CLI) and graphical user interface (GUI) versions.

## About This Project

This habit tracker helps you build and maintain positive habits by tracking your daily progress, maintaining streaks, and providing visual feedback on your journey toward better habits. The application features a clean, user-friendly design with pastel colors and intuitive navigation.

### Features
- **Add new habits** to track
- **Mark habits as complete** for the current day
- **View progress** including total completions and current streaks
- **Delete habits** with confirmation prompts
- **Persistent data storage** using JSON files
- **Flexible input options** (numbers or text commands)
- **Two interface options**: CLI and GUI versions

## How It Works

### Core AI-Generated Logic

The application is built with a well-structured, modular architecture that separates concerns and promotes maintainability:

#### Data Persistence Layer
- **`load_data()`**: Safely loads habit data from JSON file, returns empty dictionary if file doesn't exist
- **`save_data(habits)`**: Persists habit data to JSON file with proper formatting

#### Core Logic Functions (No I/O)
- **`core_add_habit(habits, habit_name)`**: Validates and adds new habits, prevents duplicates
- **`core_mark_habit(habit_data, today)`**: Updates habit progress, calculates streaks, prevents double-marking
- **`core_reset_streak(habit_data, today)`**: Resets streak counter if habit wasn't completed today
- **`core_delete_habit(habits, habit_name)`**: Removes habits with final statistics feedback

#### User Interface Functions (Handles I/O)
- **`ui_add_habit(habits)`**: Manages user input/output for adding habits
- **`ui_mark_habits(habits)`**: Interactive marking of habits for the current day
- **`ui_show_progress(habits)`**: Displays formatted progress reports
- **`ui_delete_habit(habits)`**: Safe deletion with confirmation and error handling

#### Data Structure
Habits are stored as a dictionary with the following structure:
```python
{
    "habit_name": {
        "total": 0,        # Total completions
        "streak": 0,       # Current streak count
        "last_done": ""    # Date last completed
    }
}
```

#### Key Design Principles
- **Separation of Concerns**: Core logic separated from I/O operations
- **Error Handling**: Comprehensive validation and user feedback
- **Data Integrity**: Safe file operations with proper error handling
- **User Experience**: Flexible input options and clear feedback messages

## What I Learned Directing AI

This project was developed through collaboration with AI, providing valuable insights into effective AI-assisted programming and project development.

### Prompt Refinement Process

The development journey demonstrated the importance of **prompt refinement sequences** - systematically improving AI prompts to get better, more accurate results:

1. **Initial Prompts**: Started with basic requests like "help me build a habit tracker"
2. **Iterative Refinement**: Gradually added specificity about data structures, user experience, and functionality
3. **Context Provision**: Learned to provide clear context about requirements and constraints
4. **Output Formatting**: Specified desired response structures and code organization

### Key Insights from AI Collaboration

#### **Data Organization Matters**
- **Dictionary vs List**: Learned why dictionaries are superior for habit tracking (instant access, natural key-based operations)
- **User Value Connection**: Discovered how data structure choices directly impact user experience
- **Scalability**: Understood how good data organization enables future enhancements

#### **Error Handling is Critical**
- **Edge Cases**: AI helped identify and handle scenarios like non-existent habits, empty inputs, and data validation
- **User Feedback**: Learned to provide clear, helpful error messages that guide users
- **Graceful Degradation**: Implemented robust error handling that prevents crashes and data loss

#### **Separation of Concerns**
- **Core Logic vs UI**: Separated business logic from user interface code
- **Testability**: Created functions that can be tested independently
- **Maintainability**: Built modular code that's easier to understand and modify

#### **User Experience Design**
- **Flexible Input**: Implemented multiple ways to interact (numbers, text, case-insensitive)
- **Visual Design**: Created pleasant color schemes and intuitive layouts
- **Feedback Loops**: Ensured users always know what's happening and what they can do next

### AI-Assisted Development Benefits

#### **Rapid Prototyping**
- Quickly generated working code from high-level requirements
- Explored multiple approaches (CLI, GUI, web) efficiently
- Iterated through design improvements rapidly

#### **Learning Through Collaboration**
- **Code Review**: AI provided explanations for design decisions
- **Best Practices**: Learned about proper error handling, data validation, and user experience
- **Problem Solving**: Collaborated on debugging and feature implementation

#### **Quality Assurance**
- **Testing Strategies**: Developed comprehensive test cases for edge scenarios
- **Documentation**: Created detailed README and code comments
- **Code Organization**: Maintained clean, readable, and maintainable code

### Lessons for Future AI Collaboration

1. **Be Specific**: Clear, detailed prompts produce better results
2. **Provide Context**: Give AI enough background to understand your goals
3. **Iterate Gradually**: Make small, focused improvements rather than major changes
4. **Test Thoroughly**: Always verify AI-generated code works as expected
5. **Understand the Code**: Don't just copy-paste; understand what the code does and why

### The Result

This project demonstrates how effective AI collaboration can produce:
- **Professional-quality code** with proper architecture
- **User-friendly applications** with thoughtful design
- **Comprehensive documentation** that explains both what and why
- **Maintainable solutions** that can grow with future needs

The habit tracker serves as a practical example of how AI can accelerate development while teaching important programming concepts and best practices.

## How to Run It

### Prerequisites
- Python 3.x installed on your system
- No additional dependencies required (uses only standard library)

### Command-Line Interface (CLI)

1. Navigate to the project directory:
   ```bash
   cd week_2
   ```

2. Run the CLI version:
   ```bash
   python3 habit_tracker.py
   ```

3. Use the menu options:
   - Type `1` or `add` to add a new habit
   - Type `2` or `mark` to mark habits as complete
   - Type `3` or `show` to view progress
   - Type `4` or `delete` to remove a habit
   - Type `5` or `exit` to quit

### Graphical User Interface (GUI)

1. Navigate to the project directory:
   ```bash
   cd week_2
   ```

2. Run the GUI version:
   ```bash
   python3 habit_tracker_gui.py
   ```

3. Use the graphical interface:
   - Click "Add Habit" to create new habits
   - Select a habit and click "Mark as Done" to record completion
   - Click "Show Progress" to view statistics
   - Select a habit and click "Delete Habit" to remove it

### Data Storage

Both versions use the same data file (`habits.json`) located in the `week_2` directory. Your habits and progress are automatically saved and will persist between sessions.

### Features in Both Versions

- **Flexible Input**: Accept numbers or text commands (CLI)
- **Error Handling**: Clear feedback for invalid inputs
- **Data Persistence**: Automatic saving of all changes
- **Streak Tracking**: Automatic calculation of consecutive days
- **Safe Deletion**: Confirmation prompts before removing habits

### Color Scheme (GUI Version)

The GUI features a pleasant pastel color scheme:
- **Background**: Deep butter yellow (`#ffe066`)
- **Text Entry**: Muted baby blue (`#b3d8f8`)
- **Text Color**: Creamy white (`#fffdfa`)
- **Buttons**: Various pastel shades for different actions

## File Structure

```
week_2/
├── README.md              # This file
├── habit_tracker.py       # CLI version
├── habit_tracker_gui.py   # GUI version
└── habits.json           # Data storage (created automatically)
```

## Tips for Success

- **Start Small**: Begin with 2-3 habits to build momentum
- **Be Consistent**: Mark your habits daily for accurate streak tracking
- **Review Progress**: Regularly check your progress to stay motivated
- **Use Both Versions**: CLI for quick updates, GUI for detailed review

---

*Built with Python and Tkinter. Designed for simplicity and effectiveness in building lasting habits.* 