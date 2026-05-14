from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine
import models

from routes import users
from routes import projects
from routes import tasks
from routes import dashboard

models.Base.metadata.create_all(bind=engine)

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

app.include_router(users.router)
app.include_router(projects.router)
app.include_router(tasks.router)
app.include_router(dashboard.router)

@app.get("/")
def home():
    return {
        "message": "API running successfully"
    }