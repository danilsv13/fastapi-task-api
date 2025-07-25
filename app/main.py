from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import tasks

models.Base.metadata.create_all(bind=engine) # Создаёт таблицы в базе, если их нет
app = FastAPI(title="Task API") # Экземпляр FastAPI
app.include_router(tasks.router) # Подключает маршруты из tasks.py

@app.get("/")
def root():
    return {"message": "Task API is working. Go to /docs"}
