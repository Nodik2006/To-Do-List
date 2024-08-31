# Enhanced ToDo Application

## Overview

This Enhanced ToDo Application is a feature-rich task management tool built with Python and PyQt5. It offers a user-friendly interface for managing daily tasks, with support for both light and dark modes to suit user preferences.

## Features

- Add, edit, and delete tasks
- Mark tasks as complete
- View detailed task information
- Clear all tasks with confirmation
- Day and Dark mode toggle
- Persistent storage of tasks between sessions
- Responsive and intuitive GUI

## Requirements

- Python 3.6+
- PyQt5

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Nodik2006/To-Do-List.git
   cd To-Do-List
   ```

2. Install the required dependencies:
   ```
   pip install PyQt5
   ```

## Usage

Run the application using Python:

```
python todo_app.py
```

### Adding a Task
1. Enter the task title in the "Task Title" field.
2. (Optional) Enter additional details in the "Task Details" field.
3. Click the "Add Task" button.

### Editing a Task
1. Select a task from the list.
2. Click the "Edit Task" button.
3. Modify the title or details in the pop-up dialog.
4. Click "Save" to confirm changes.

### Completing a Task
1. Select a task from the list.
2. Click the "Mark as Complete" button.

### Deleting a Task
1. Select a task from the list.
2. Click the "Delete Task" button.

### Viewing Task Details
1. Select a task from the list.
2. Click the "Show Details" button.

### Clearing All Tasks
1. Click the "Clear All" button.
2. Confirm the action in the pop-up dialog.

### Toggling Between Day and Dark Mode
- Click the "Toggle Dark Mode" or "Toggle Day Mode" button at the bottom of the window to switch between color schemes.

## File Storage

Tasks are automatically saved to a file named `tasks.txt` in the same directory as the script. This ensures that your tasks persist between application sessions.

## Contributing

Contributions to improve the Enhanced ToDo Application are welcome. Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

This project is open source and available under the [MIT License](LICENSE).
