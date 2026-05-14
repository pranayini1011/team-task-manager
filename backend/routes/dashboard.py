from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from datetime import datetime

from database import get_db

from models import (
    Task,
    StatusEnum,
    User
)

from auth import get_current_user

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/")
def get_dashboard(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    tasks = db.query(Task).all()

    total_tasks = len(tasks)

    todo = len([
        t for t in tasks
        if t.status == StatusEnum.todo
    ])

    in_progress = len([
        t for t in tasks
        if t.status == StatusEnum.inprogress
    ])

    done = len([
        t for t in tasks
        if t.status == StatusEnum.done
    ])

    overdue = len([
        t for t in tasks
        if t.due_date < datetime.utcnow()
        and t.status != StatusEnum.done
    ])

    tasks_per_user = {}

    users = db.query(User).all()

    for user in users:

        user_tasks = db.query(Task).filter(
            Task.assigned_to == user.id
        ).count()

        tasks_per_user[user.name] = user_tasks

    return {

        "total_tasks": total_tasks,

        "todo": todo,

        "in_progress": in_progress,

        "done": done,

        "overdue": overdue,

        "tasks_per_user": tasks_per_user
    }