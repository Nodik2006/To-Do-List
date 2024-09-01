let isDarkMode = false;

// Переключение на интерфейс просмотра задач
function switchToViewTasks() {
  document.getElementById("addTaskInterface").style.display = "none";
  document.getElementById("viewTaskInterface").style.display = "flex";
  loadTasks();
}

// Переключение на интерфейс добавления задач
function switchToAddTask() {
  document.getElementById("addTaskInterface").style.display = "flex";
  document.getElementById("viewTaskInterface").style.display = "none";
}

// Функция для рендеринга задач в списке
function renderTasks(tasks) {
  const taskList = document.getElementById("taskList");
  taskList.innerHTML = "";
  tasks.forEach((task, index) => {
    const taskItem = document.createElement("li");
    taskItem.className = task.completed ? "completed" : "";
    taskItem.innerHTML = `
              ${task.title}
              <div>
                  <button onclick="showDetails(${index})">
                    <img src="img/details.png" alt="Details Icon">
                  </button>
                  <button onclick="editTask(${index})">
                    <img src="img/edit.png" alt="Edit Icon">
                  </button>
                  <button onclick="deleteTask(${index})">
                    <img src="img/delete.png" alt="Delete Icon">
                  </button>
                  <button onclick="markComplete(${index})">
                    <img src="img/complete.png" alt="Complete Icon">
                  </button>
              </div>
          `;
    taskList.appendChild(taskItem);
  });
}

// Функция загрузки всех задач
async function loadTasks() {
  const tasks = await eel.get_tasks()();
  renderTasks(tasks);
}

// Функция добавления новой задачи
async function addTask() {
  const title = document.getElementById("taskTitle").value;
  const details = document.getElementById("taskDetails").value;
  if (await eel.add_task(title, details)()) {
    document.getElementById("taskTitle").value = "";
    document.getElementById("taskDetails").value = "";
  } else {
    alert("Please enter a task title.");
  }
}

// Функция удаления задачи
async function deleteTask(index) {
  if (await eel.delete_task(index)()) {
    loadTasks();
  }
}

// Функция отметки задачи как выполненной
async function markComplete(index) {
  if (await eel.mark_task_complete(index)()) {
    loadTasks();
  }
}

// Функция редактирования задачи
async function editTask(index) {
  const title = prompt("Edit Task Title:", "");
  const details = prompt("Edit Task Details:", "");
  if (title && (await eel.edit_task(index, title, details)())) {
    loadTasks();
  }
}

// Функция отображения деталей задачи
async function showDetails(index) {
  const details = await eel.show_task_details(index)();

  // Вместо alert, заполняем модальное окно и показываем его
  document.getElementById("modalTaskTitle").textContent = details.title;
  document.getElementById("modalTaskDetails").textContent = details.details;
  document.getElementById("taskDetailsModal").style.display = "block";
}

// Закрываем модальное окно при клике на крестик или вне области контента
const modal = document.getElementById("taskDetailsModal");
const span = document.getElementsByClassName("close")[0];
span.onclick = function () {
  modal.style.display = "none";
};
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

// Функция переключения темного режима
function toggleMode() {
  isDarkMode = !isDarkMode;
  const body = document.body;

  if (isDarkMode) {
    body.classList.add("dark-theme");
    body.classList.remove("red-theme");
  } else {
    body.classList.remove("dark-theme");
    body.classList.add("red-theme");
  }
}

// Блокировка изменения размера окна
window.onload = function () {
  window.resizeTo(600, 800);
  window.addEventListener("resize", function (event) {
    window.resizeTo(600, 800);
  });
};

// Инициализация задачи при загрузке страницы
loadTasks();
