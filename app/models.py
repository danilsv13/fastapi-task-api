from sqlalchemy import Column, Integer, String, DateTime, Enum
from datetime import datetime
from app.database import Base
import enum

# Перечисление (enum) возможных статусов задач
class TaskStatus(str, enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"

# Модель SQLAlchemy: описывает таблицу "tasks"
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True) # Уникальный ID
    title = Column(String, nullable=False) # Заголовок
    description = Column(String, nullable=True) # Описание 
    status = Column(Enum(TaskStatus), default=TaskStatus.pending) # Статус
    created_at = Column(DateTime, default=datetime.utcnow) # Дата создания
