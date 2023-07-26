import sqlalchemy as db
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
import os

from citySchemas import Base

url_object = URL.create(
    "postgresql+psycopg2",
    username=os.environ.get("USERNAME"),
    password=os.environ.get("PASSWORD"),  # plain (unescaped) text
    host=os.environ.get("HOST"),
    database=os.environ.get("DATABASE_NAME"),
)

#Setup connection to database
def connection():
    engine = db.create_engine(url_object)
    return engine

#Create session
Session = sessionmaker(bind=connection())

#Create the table schema
def table_setup():
    engine = db.create_engine(url_object)
    Base.metadata.create_all(engine)
    return engine
    
# For Testing
# brew install postgresql
# createuser -s postgres
# brew services restart postgresql

def main():
    table_setup()

if __name__ == '__main__':
    main()