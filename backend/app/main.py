from fastapi import FastAPI
from app.api.routes import calculations, formulas
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Rafo API",
    description="Engineering Calculation Platform API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
    ],
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