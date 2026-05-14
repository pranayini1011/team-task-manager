from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine

from routes.users import router as user_router
from routes.projects import router as project_router
from routes.tasks import router as task_router
from routes.dashboard import router as dashboard_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:3000",
        "https://team-task-manager-neon-six.vercel.app"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

@app.get("/")
def home():

    return {
        "message": "Team Task Manager API Running"
    }

app.include_router(user_router)

app.include_router(project_router)

app.include_router(task_router)

app.include_router(dashboard_router)from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine

from routes.users import router as user_router
from routes.projects import router as project_router
from routes.tasks import router as task_router
from routes.dashboard import router as dashboard_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:3000",
        "https://team-task-manager-neon-six.vercel.app"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

@app.get("/")
def home():

    return {
        "message": "Team Task Manager API Running"
    }

app.include_router(user_router)

app.include_router(project_router)

app.include_router(task_router)

app.include_router(dashboard_router)