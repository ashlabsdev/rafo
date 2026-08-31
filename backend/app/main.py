from fastapi import FastAPI
from app.api.routes import formulas

app = FastAPI(
    title="Rafo API",
    description="Engineering Calculation Platform API",
    version="0.1.0"
)

app.include_router(formulas.router)

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