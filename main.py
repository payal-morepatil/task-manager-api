from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from database import engine, sessionLocal
from models import TaskDB
from schemas import Task
from auth import create_token, verify_jwt

app = FastAPI()

# create the database tables
TaskDB.metadata.create_all(bind=engine)

security = HTTPBearer()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


# tasks = []
def verify_token(credentials: HTTPAuthorizationCredentials =
                 Depends(security)):
    token = credentials.credentials
    payload = verify_jwt(token)
    if payload is None:
        raise HTTPException(status_code=401, detail='Invalid token')

    return payload

@app.post('/login')  # create a route for login
def login(username: str, password: str):
    if username != 'admin' and password != 'password':
        raise HTTPException(status_code=401, detail='Invalid credentials')
    token = create_token({'user': username})
    return {'access_token': token}


@app.get('/')  # create a route for the home page
def home():
    return {'messsage': 'welcome to Task Manager API'}


@app.post('/tasks')  # create a route for creating a task
def create_task(task: Task, db: Session = Depends(get_db),
                user :dict = Depends(verify_token)):
    new_task = TaskDB(**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@app.get('/tasks')  # create a route for getting all tasks
def get_tasks(db: Session = Depends(get_db),user :dict = Depends(verify_token)):
    return db.query(TaskDB).all()


@app.put('/tasks/{id}')  # create a route for getting a task by id
def update_task(id: int, task: Task, db: Session = Depends(get_db),user :dict = Depends(verify_token)):
    existing_task = db.query(TaskDB).filter(TaskDB.id == id).first()
    if not existing_task:
        raise HTTPException(status_code=404, detail='Task not found')
    existing_task.title = task.title
    existing_task.description = task.description
    existing_task.status = task.status
    db.commit()

    return {'message': 'Task updated successfully'}


@app.delete('/tasks/{id}')  # create a route for deleting a task by id
def delete_task(id: int, db: Session = Depends(get_db),user :dict = Depends(verify_token)):
    existing_task = db.query(TaskDB).filter(TaskDB.id == id).first()
    if not existing_task:
        raise HTTPException(status_code=404, detail='Task not found')
    db.delete(existing_task)
    db.commit()
    return {'message': 'Task deleted successfully'}
