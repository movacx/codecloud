from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controller.student_controller_api import router as student_router
from config.database import init_db

app = FastAPI(title="Student API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
init_db()

app.include_router(student_router)
