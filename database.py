from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker, declarative_base

# tells python where database
DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/task_db'

# create a database connection
engine = create_engine(DATABASE_URL)

#use for db operations
sessionLocal = sessionmaker(bind=engine)

# create to table
Base = declarative_base()