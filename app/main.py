from fastapi import FastAPI
from app.routers import equipment
from app.database import init_db

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    init_db()

app.include_router(equipment.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Smart Fleet Maintenance API"}