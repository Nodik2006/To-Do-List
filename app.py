import eel
import json

class Task:
    def __init__(self, title, details="", completed=False):
        self.title = title
        self.details = details
        self.completed = completed

tasks = []
filename = "tasks.json"

@eel.expose
def add_task(title, details=""):
    if title:
        tasks.append(Task(title, details))
        save_tasks()
        return True
    return False

@eel.expose
def get_tasks():
    return [{"title": task.title, "details": task.details, "completed": task.completed} for task in tasks]

@eel.expose
def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks()
        return True
    return False

@eel.expose
def mark_task_complete(index):
    if 0 <= index < len(tasks):
        tasks[index].completed = True
        save_tasks()
        return True
    return False

@eel.expose
def edit_task(index, title, details):
    if 0 <= index < len(tasks):
        tasks[index].title = title
        tasks[index].details = details
        save_tasks()
        return True
    return False

@eel.expose
def show_task_details(index):
    if 0 <= index < len(tasks):
        return {"title": tasks[index].title, "details": tasks[index].details}
    return ""

@eel.expose
def toggle_mode(is_dark_mode):
    return is_dark_mode

def save_tasks():
    with open(filename, 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

def load_tasks():
    global tasks
    try:
        with open(filename, 'r') as f:
            tasks_data = json.load(f)
            tasks = [Task(**data) for data in tasks_data]
    except FileNotFoundError:
        tasks = []

# Инициализация и запуск приложения
eel.init('web')
load_tasks()
# Удаляем параметр options
eel.start('index.html', size=(600, 800))
