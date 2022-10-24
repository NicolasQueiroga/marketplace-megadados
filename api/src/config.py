import os
from .main import app
from fastapi.middleware.cors import CORSMiddleware


DEBUG = bool(int(os.environ.get("DEBUG", 0)))

origins = [
    "http://localhost",
    "http://localhost:8008",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)