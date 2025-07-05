from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel

# Defining Schemas
class CreateTask(BaseModel):
    title: str | None = None
    description: str | None = None
    is_completed: bool = False

class UpdateTask(BaseModel):
    is_completed: bool = True
    title: None | str = None
    description: None | str = None

#creating instances
app = FastAPI()
con = sqlite3.connect("tasks_data.db")
cur = con.cursor()

# if table not exits create one
cur.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT, 
    is_completed TEXT
)
""")

# endpoint to create a task in database
@app.post("/tasks")
async def create_task(task: CreateTask):
    cur.execute("""
        INSERT INTO tasks (title, description, is_completed)
        VALUES (?, ?, ?)
    """, (task.title, task.description, str(task.is_completed).lower()))
    con.commit() 
    return {"message": "task created successfully"}

# endpoint to get all tasks from database
@app.get("/tasks")
async def send_all(is_completed: bool | None = None):
    # checking for query parameters
    if is_completed is not None:
        value = "true" if is_completed else "false"
        cur.execute("SELECT * FROM tasks WHERE is_completed = ?", (value,))
    else:
        cur.execute("SELECT * FROM tasks")
    
    rows = cur.fetchall()
    tasks = [
        {
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "is_completed": row[3] == "true"
        }
        for row in rows
    ]
    return {"tasks": tasks}

# endpoint to get info of particular task based on task id
@app.get("/tasks/{task_id}")
async def send(task_id: int):
    # Checking if task exists
    cur.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    row = cur.fetchone()
    if row is None:
        return {"ERROR": "404 task not found"}
    task = [
        {
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "is_completed": row[3] == "true"
        }
    ]
    return {"tasks": task}

# endpoint to update particular task 
@app.put("/tasks/{task_id}")
async def update(task_id: int, task: UpdateTask):
    # checking if task exists
    cur.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    row = cur.fetchone()
    if row is None:
        return {"ERROR": "404 task not found"}
    
    # checking for updated parameters
    title = task.title if (task.title and task.title !="string") else row[1]
    description = task.description if (task.description and task.description != "string") else row[2]
    is_completed = str(task.is_completed) if task.is_completed else row[3]

    cur.execute("""
        UPDATE tasks
        SET title = ?, description = ?, is_completed = ?
        WHERE id = ?
    """, (title, description, str(is_completed).lower(), task_id))
    con.commit()
    
    return {"message": "Task updated", "task": task}

# endpoint to delete particular task
@app.delete("/tasks/{task_id}")
async def delete(task_id: int):
    # checking if task exists
    cur.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    row = cur.fetchone()
    if row is None:
        return {"ERROR": "404 task not found"}

    cur.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    con.commit()

    return {"message": "task deleted successfully"}