from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from database import Base
import enum

class PriorityEnum(str, enum.Enum):
    low = "Low"
    medium = "Medium"
    high = "High"

class StatusEnum(str, enum.Enum):
    todo = "To Do"
    inprogress = "In Progress"
    done = "Done"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password_hash = Column(String)

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    created_by = Column(Integer, ForeignKey("users.id"))

class ProjectMember(Base):
    __tablename__ = "project_members"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    role = Column(String, default="Member")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

    due_date = Column(DateTime)

    priority = Column(Enum(PriorityEnum))

    status = Column(
        Enum(StatusEnum),
        default=StatusEnum.todo
    )

    project_id = Column(
        Integer,
        ForeignKey("projects.id")
    )

    assigned_to = Column(
        Integer,
        ForeignKey("users.id")
    )