# 📌 Task Manager API (FastAPI + SQLite)

This is a simple REST API for managing tasks, built using **FastAPI** and **SQLite**. It allows you to:

- Create tasks
- View all tasks (with optional filter)
- View individual task
- Update a task
- Delete a task

---

## 🚀 How to Run This API Locally

### ✅ Prerequisites

Make sure you have:

- Python 3.10 or above installed
- `pip` (Python package manager)

---

### 📁 Project Structure

```
.
├── main.py             # Main FastAPI app
├── tasks_data.db       # SQLite database (auto-created)
├── requirements.txt    # Dependencies
└── README.md
```

---

### 📦 1. Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note:** If `pip` gives an error with `fastapi[standard]`, try upgrading pip:
> ```bash
> python -m pip install --upgrade pip
> ```

---

### ▶️ 2. Run the API Server

Use **uvicorn** to run the server:

```bash
uvicorn main:app --reload
```

- `main` = filename without `.py` (`main.py`)
- `app` = FastAPI app instance inside `main.py`
- `--reload` = auto-restarts server on code changes

---

### 🌐 3. Test the API

After running, open your browser and visit:

**Interactive Docs:**  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

**Alternative Docs:**  
[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 Sample Endpoints

| Method   | Endpoint                 | Description               |
|----------|--------------------------|---------------------------|
| `POST`   | `/tasks`                 | Create a new task         |
| `GET`    | `/tasks`                 | Get all tasks             |
| `GET`    | `/tasks?is_completed=true` | Filter completed tasks |
| `GET`    | `/tasks/{task_id}`       | Get task by ID            |
| `PUT`    | `/tasks/{task_id}`       | Update task by ID         |
| `DELETE` | `/tasks/{task_id}`       | Delete task by ID         |

---

## 🗃️ Data Model

```json
// CreateTask
{
  "title": "My Task",
  "description": "Do something important",
  "is_completed": false
}

// UpdateTask
{
  "title": "Updated Title",
  "description": "Updated Description",
  "is_completed": true
}
```

---

## 🛠 Tips

- The database `tasks_data.db` will be created automatically in the same folder.
- Use tools like **Postman**, **curl**, or the **Swagger UI** (`/docs`) to test endpoints.

---
