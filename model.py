from sqlmodel import SQLModel, Field, create_engine
from typing import Optional


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    username: str
    email: str
    password: str

engine = create_engine("sqlite:///data.db", echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
