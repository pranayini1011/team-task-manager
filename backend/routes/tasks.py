from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from datetime import datetime

from database import get_db

from models import (
    Task,
    StatusEnum,
    ProjectMember,
    User
)

from auth import get_current_user

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.post("/")
def create_task(
    title: str,
    description: str,
    due_date: str,
    priority: str,
    project_id: int,
    assigned_to: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    admin = db.query(ProjectMember).filter(
        ProjectMember.project_id == project_id,
        ProjectMember.user_id == current_user.id,
        ProjectMember.role == "Admin"
    ).first()

    if not admin:

        raise HTTPException(
            status_code=403,
            detail="Only admins can create tasks"
        )

    task = Task(
        title=title,
        description=description,
        due_date=datetime.fromisoformat(due_date),
        priority=priority,
        project_id=project_id,
        assigned_to=assigned_to
    )

    db.add(task)

    db.commit()

    return {
        "message": "Task created successfully"
    }

@router.get("/")
def get_tasks(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    tasks = db.query(Task).filter(
        Task.assigned_to == current_user.id
    ).all()

    return tasks

@router.patch("/{task_id}/status")
def update_task_status(
    task_id: int,
    status: StatusEnum,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    if task.assigned_to != current_user.id:

        raise HTTPException(
            status_code=403,
            detail="You can only update your own tasks"
        )

    task.status = status

    db.commit()

    return {
        "message": "Task status updated"
    }

@router.get("/{task_id}")
def get_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    if task.assigned_to != current_user.id:

        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return task