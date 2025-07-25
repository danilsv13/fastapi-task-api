from sqlalchemy.orm import Session
from app import models, schemas

# Создание задачи
def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Получение всех задач (с фильтром по статусу)
def get_tasks(db: Session, status: str = None):
    if status:
        return db.query(models.Task).filter(models.Task.status == status).all()
    return db.query(models.Task).all()


# Обновление задачи по ID
def update_task(db: Session, task_id: int, task: schemas.TaskUpdate):
    db_task = db.query(models.Task).get(task_id)
    if not db_task:
        return None
    for key, value in task.dict(exclude_unset=True).items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

# Удаление задачи
def delete_task(db: Session, task_id: int):
    db_task = db.query(models.Task).get(task_id)
    if not db_task:
        return None
    db.delete(db_task)
    db.commit()
    return db_task
