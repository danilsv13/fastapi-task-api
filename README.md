# 🧩 FastAPI Task API

REST API на FastAPI для управления задачами

##  Стек технологий
- Python 3.11+
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite 

## 📌 Возможности
- Добавление задач (`POST /tasks/`)
- Получение списка задач (`GET /tasks/`)
- Обновление задач (`PUT /tasks/{id}`)
- Удаление задач (`DELETE /tasks/{id}`)

## 🚀 Как запустить
```bash
uvicorn app.main:app --reload
