from typing import Sequence

from fastapi import FastAPI
from sqlmodel import Session, select
from model import User, engine, create_db_and_tables
from bcrypt import hashpw, gensalt
from pydantic import BaseModel
import jwt
from fastapi.middleware.cors import CORSMiddleware

password = "um_secret_bem_secreto"

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

create_db_and_tables()


def get_session():
    with Session(engine) as session:
        yield session


@app.post("/register/")
def create_user(user: User) -> dict[str, str] | User:
    # check if user already exists
    with Session(engine) as session:
        if session.exec(select(User).where(User.username == user.username)).first():
            return {"error": "Username already exists"}

        if session.exec(select(User).where(User.email == user.email)).first():
            return {"error": "Email already exists"}

        user.password = hashpw(user.password.encode(), gensalt()).decode()

        session.add(user)
        session.commit()
        session.refresh(user)

        user.password = None
        return user


@app.get("/users/")
def read_users() -> Sequence[User]:
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        users = [User(id=user.id, name=user.name, username=user.username, email=user.email) for user in users]

        return users


class LoginDTO(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    token: str
    user: User

@app.post("/login/")
def login_user(user: LoginDTO) -> dict[str, str] | LoginResponse:
    with Session(engine) as session:
        db_user = session.exec(select(User).where(User.email == user.username)).first()

        if not db_user:
            return {"error": "User not found"}

        if not db_user.password == hashpw(user.password.encode(), db_user.password.encode()).decode():
            return {"error": "Incorrect password"}

        token = generate_token(db_user)
        user = {
            "id": db_user.id,
            "name": db_user.name,
            "username": db_user.username,
            "email": db_user.email
        }
        return LoginResponse(token=token, user=user)


def generate_token(user: User) -> str:
    return jwt.encode({"id": user.id, "username": user.username}, password, algorithm="HS256")


@app.get("/")
def read_root():
    return {"message": "a api ta rodando! :)"}
