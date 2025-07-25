from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models import TaskStatus

# Схема для создания новой задачи
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus

# Схема для частичного обновления задачи
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None

# Схема, которая возвращается клиенту
class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: TaskStatus
    created_at: datetime

    class Config:
        orm_mode = True
