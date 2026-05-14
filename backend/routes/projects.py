from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from database import get_db

from models import (
    Project,
    ProjectMember,
    User
)

from auth import get_current_user

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

@router.post("/")
def create_project(
    name: str,
    description: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    project = Project(
        name=name,
        description=description,
        created_by=current_user.id
    )

    db.add(project)

    db.commit()

    db.refresh(project)

    admin_member = ProjectMember(
        project_id=project.id,
        user_id=current_user.id,
        role="Admin"
    )

    db.add(admin_member)

    db.commit()

    return {
        "message": "Project created successfully"
    }

@router.get("/")
def get_projects(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    projects = db.query(Project).join(
        ProjectMember,
        Project.id == ProjectMember.project_id
    ).filter(
        ProjectMember.user_id == current_user.id
    ).all()

    return projects

@router.post("/{project_id}/members")
def add_member(
    project_id: int,
    user_id: int,
    role: str,
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
            detail="Only admins can add members"
        )

    existing_member = db.query(ProjectMember).filter(
        ProjectMember.project_id == project_id,
        ProjectMember.user_id == user_id
    ).first()

    if existing_member:

        raise HTTPException(
            status_code=400,
            detail="User already exists in project"
        )

    member = ProjectMember(
        project_id=project_id,
        user_id=user_id,
        role=role
    )

    db.add(member)

    db.commit()

    return {
        "message": "Member added successfully"
    }
@router.delete("/{project_id}/members/{user_id}")
def remove_member(
    project_id: int,
    user_id: int,
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
            detail="Only admins can remove members"
        )

    member = db.query(ProjectMember).filter(
        ProjectMember.project_id == project_id,
        ProjectMember.user_id == user_id
    ).first()

    if not member:

        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    db.delete(member)

    db.commit()

    return {
        "message": "Member removed successfully"
    }