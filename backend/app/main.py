import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import calculations, formulas


app = FastAPI(
    title="Rafo API",
    description="Engineering Calculation Platform API",
    version="0.1.0",
)


allowed_origins = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:4200",
).split(",")


app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(formulas.router)
app.include_router(calculations.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Rafo API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }