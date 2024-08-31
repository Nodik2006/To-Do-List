from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, 
                             QPushButton, QLabel, QMessageBox, QListWidgetItem, QFrame, QTextEdit, QDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QIcon, QPalette

class Task:
    def __init__(self, title, details="", completed=False):
        self.title = title
        self.details = details
        self.completed = completed

class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.tasks = []
        self.is_dark_mode = False
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Enhanced ToDo List")
        self.setGeometry(100, 100, 500, 600)

        self.task_list = QListWidget()
        self.task_list.setAlternatingRowColors(True)
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter a new task title...")
        self.task_details = QTextEdit()
        self.task_details.setPlaceholderText("Enter task details (optional)...")
        self.task_details.setMaximumHeight(100)
        self.add_button = QPushButton("Add Task")
        self.delete_button = QPushButton("Delete Task")
        self.complete_button = QPushButton("Mark as Complete")
        self.clear_all_button = QPushButton("Clear All")
        self.edit_button = QPushButton("Edit Task")
        self.details_button = QPushButton("Show Details")
        self.mode_toggle_button = QPushButton("Toggle Dark Mode")

        main_layout = QVBoxLayout()
        input_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        input_layout.addWidget(QLabel("Task Title:"))
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(QLabel("Task Details:"))
        input_layout.addWidget(self.task_details)
        input_layout.addWidget(self.add_button)

        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.complete_button)
        button_layout.addWidget(self.details_button)
        button_layout.addWidget(self.clear_all_button)

        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.task_list)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.mode_toggle_button)

        spacer = QFrame()
        spacer.setFrameShape(QFrame.HLine)
        spacer.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(spacer)

        self.setLayout(main_layout)

        self.add_button.clicked.connect(self.add_task)
        self.delete_button.clicked.connect(self.delete_task)
        self.complete_button.clicked.connect(self.mark_task_complete)
        self.clear_all_button.clicked.connect(self.clear_all_tasks)
        self.edit_button.clicked.connect(self.edit_task)
        self.details_button.clicked.connect(self.show_task_details)
        self.mode_toggle_button.clicked.connect(self.toggle_mode)

        self.load_tasks("tasks.txt")
        self.update_task_list()
        self.set_day_mode()

    def set_day_mode(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#E6E6FA"))  # Light lavender background
        palette.setColor(QPalette.WindowText, QColor("#000080"))  # Navy blue text
        palette.setColor(QPalette.Base, QColor("#FFFFFF"))  # White for input fields
        palette.setColor(QPalette.AlternateBase, QColor("#F0F0F0"))  # Light grey for alternating rows
        palette.setColor(QPalette.ToolTipBase, QColor("#FFFFFF"))
        palette.setColor(QPalette.ToolTipText, QColor("#000000"))
        palette.setColor(QPalette.Text, QColor("#000080"))  # Navy blue text for input fields
        palette.setColor(QPalette.Button, QColor("#4169E1"))  # Royal blue for buttons
        palette.setColor(QPalette.ButtonText, QColor("#FFFFFF"))
        palette.setColor(QPalette.Highlight, QColor("#6A5ACD"))  # Slate blue for selection
        palette.setColor(QPalette.HighlightedText, QColor("#FFFFFF"))
        self.setPalette(palette)
        self.is_dark_mode = False
        self.mode_toggle_button.setText("Toggle Dark Mode")
        self.update_task_list()

    def set_dark_mode(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#000000"))  # Black background
        palette.setColor(QPalette.WindowText, QColor("#FFFFFF"))  # White text
        palette.setColor(QPalette.Base, QColor("#1E1E1E"))  # Dark grey for input fields
        palette.setColor(QPalette.AlternateBase, QColor("#2A2A2A"))  # Slightly lighter grey for alternating rows
        palette.setColor(QPalette.ToolTipBase, QColor("#FFFFFF"))
        palette.setColor(QPalette.ToolTipText, QColor("#000000"))
        palette.setColor(QPalette.Text, QColor("#FFFFFF"))  # White text for input fields
        palette.setColor(QPalette.Button, QColor("#8B0000"))  # Dark red for buttons
        palette.setColor(QPalette.ButtonText, QColor("#FFFFFF"))
        palette.setColor(QPalette.Highlight, QColor("#B22222"))  # Lighter red for selection
        palette.setColor(QPalette.HighlightedText, QColor("#FFFFFF"))
        self.setPalette(palette)
        self.is_dark_mode = True
        self.mode_toggle_button.setText("Toggle Day Mode")
        self.update_task_list()

    def toggle_mode(self):
        if self.is_dark_mode:
            self.set_day_mode()
        else:
            self.set_dark_mode()

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    parts = line.strip().split('|')
                    if len(parts) >= 3:
                        title, details, completed = parts[0], parts[1], parts[2] == 'True'
                        self.tasks.append(Task(title, details, completed))
        except FileNotFoundError:
            pass

    def save_tasks(self, filename):
        with open(filename, 'w') as f:
            for task in self.tasks:
                f.write(f"{task.title}|{task.details}|{task.completed}\n")

    def add_task(self):
        title = self.task_input.text()
        if title:
            details = self.task_details.toPlainText()
            self.tasks.append(Task(title, details))
            self.update_task_list()
            self.task_input.clear()
            self.task_details.clear()
        else:
            QMessageBox.warning(self, "Warning", "Please enter a task title.")

    def update_task_list(self):
        self.task_list.clear()
        for i, task in enumerate(self.tasks):
            item = QListWidgetItem(f"{i+1}. {task.title}")
            if task.completed:
                item.setForeground(QColor("#808080"))  # Grey for completed tasks
                item.setFlags(item.flags() & ~Qt.ItemIsEnabled)
            else:
                item.setForeground(QColor("#000080") if not self.is_dark_mode else QColor("#FFFFFF"))
            self.task_list.addItem(item)

    def mark_task_complete(self):
        selected_items = self.task_list.selectedItems()
        if selected_items:
            for item in selected_items:
                task_index = self.task_list.row(item)
                self.tasks[task_index].completed = True
            self.update_task_list()
        else:
            QMessageBox.warning(self, "Warning", "Please select a task.")

    def delete_task(self):
        selected_items = self.task_list.selectedItems()
        if selected_items:
            for item in selected_items:
                task_index = self.task_list.row(item)
                del self.tasks[task_index]
            self.update_task_list()
        else:
            QMessageBox.warning(self, "Warning", "Please select a task.")

    def clear_all_tasks(self):
        confirm = QMessageBox.question(self, "Confirm Clear All", "Are you sure you want to delete all tasks?",
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.tasks.clear()
            self.update_task_list()

    def edit_task(self):
        selected_items = self.task_list.selectedItems()
        if selected_items:
            task_index = self.task_list.row(selected_items[0])
            task = self.tasks[task_index]
            
            dialog = QDialog(self)
            dialog.setWindowTitle("Edit Task")
            dialog_layout = QVBoxLayout()
            
            title_input = QLineEdit(task.title)
            details_input = QTextEdit(task.details)
            
            dialog_layout.addWidget(QLabel("Task Title:"))
            dialog_layout.addWidget(title_input)
            dialog_layout.addWidget(QLabel("Task Details:"))
            dialog_layout.addWidget(details_input)
            
            buttons = QHBoxLayout()
            save_button = QPushButton("Save")
            cancel_button = QPushButton("Cancel")
            buttons.addWidget(save_button)
            buttons.addWidget(cancel_button)
            dialog_layout.addLayout(buttons)
            
            dialog.setLayout(dialog_layout)
            
            save_button.clicked.connect(dialog.accept)
            cancel_button.clicked.connect(dialog.reject)
            
            result = dialog.exec_()
            if result == QDialog.Accepted:
                task.title = title_input.text()
                task.details = details_input.toPlainText()
                self.update_task_list()
        else:
            QMessageBox.warning(self, "Warning", "Please select a task to edit.")

    def show_task_details(self):
        selected_items = self.task_list.selectedItems()
        if selected_items:
            task_index = self.task_list.row(selected_items[0])
            task = self.tasks[task_index]
            QMessageBox.information(self, "Task Details", f"Title: {task.title}\n\nDetails: {task.details}")
        else:
            QMessageBox.warning(self, "Warning", "Please select a task to view details.")

    def closeEvent(self, event):
        self.save_tasks("tasks.txt")
        event.accept()

if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("Fusion")
    todo_app = TodoApp()
    todo_app.show()
    app.exec_()