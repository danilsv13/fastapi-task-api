from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, models
from app.database import SessionLocal


# Создаём маршруты с префиксом /tasks
router = APIRouter(prefix="/tasks", tags=["Tasks"])

# Зависимость: получение сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST /tasks/ — создать задачу
@router.post("/", response_model=schemas.TaskOut)
def create(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)


# GET /tasks/ — получить список задач (с фильтром по статусу)
@router.get("/", response_model=list[schemas.TaskOut])
def read(status: str = None, db: Session = Depends(get_db)):
    return crud.get_tasks(db, status)

# PUT /tasks/{task_id} — обновить задачу по ID
@router.put("/{task_id}", response_model=schemas.TaskOut)
def update(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    db_task = crud.update_task(db, task_id, task)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


# DELETE /tasks/{task_id} — удалить задачу по ID
@router.delete("/{task_id}")
def delete(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.delete_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
