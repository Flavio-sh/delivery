from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI


def start_app():
    app = FastAPI()

    origins = [
        "http://localhost:3001",
        "http://localhost:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
