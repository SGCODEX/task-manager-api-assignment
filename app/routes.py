from fastapi import APIRouter
from app.models import Task
from app.service import create_task_service

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Task Manager API running"}

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/tasks")
def create_task(task: Task):
    task_id = create_task_service(task)
    return {"task_id": task_id}

from app.service import get_tasks_service

# @router.get("/tasks")
# def get_tasks():
#     return get_tasks_service()

@router.get("/tasks")
def get_tasks(page: int = 1, limit: int = 5):
    return get_tasks_service(page, limit)

from app.service import get_task_service

@router.get("/tasks/{task_id}")
def get_task(task_id: str):
    return get_task_service(task_id)

from app.service import update_task_service

@router.put("/tasks/{task_id}")
def update_task(task_id: str, task: Task):
    updated = update_task_service(task_id, task)

    if updated:
        return {"message": "Task updated"}
    
    return {"message": "Task not found"}

from app.service import delete_task_service

@router.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    deleted = delete_task_service(task_id)

    if deleted:
        return {"message": "Task deleted"}
    
    return {"message": "Task not found"}

from app.service import complete_task_service

@router.post("/tasks/{task_id}/complete")
def complete_task(task_id: str):
    completed = complete_task_service(task_id)

    if completed:
        return {"message": "Task marked as completed"}

    return {"message": "Task not found"}