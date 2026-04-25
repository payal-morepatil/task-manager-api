from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from database import engine, sessionLocal
from models import TaskDB
from schemas import Task
app = FastAPI()

# create the database tables
TaskDB.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

#tasks = []

@app.get('/') # create a route for the home page
def home():
    return {'messsage': 'welcome to Task Manager API'}

@app.post('/tasks') # create a route for creating a task
def create_task(task:Task, db: Session = Depends(get_db)):
    new_task = TaskDB(**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return  new_task

@app.get('/tasks') # create a route for getting all tasks
def get_tasks(db: Session = Depends(get_db)):
    return  db.query(TaskDB).all()