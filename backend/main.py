from fastapi import FastAPI, Depends, HTTPException

from typing import List
from sqlalchemy.orm import Session

import crud, models, schemas

from database import SessionLocal, engine

from pydantic import BaseModel
import jwt
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

SECRET_KEY = "Trizibu Putybu"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 800

# test_user = {
#     "username": "test",
#     "password":"pass"
# }

app = FastAPI()

#  Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


origins = {
    "http://localhost",
    "http://localhost:3000",
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#  Classes are the tables in the database
# They should have they own file


class UserItem(BaseModel):
    username: str
    password: str

    @app.get("/")
    def read_root():
        return {"Hello": "World"}


@app.post("/login")
async def login(user: schemas.UserCreate, db: Session = Depends(get_db)):


    data = jsonable_encoder(user)
    db_user = crud.get_user_by_email(db, data["email"])

    if not db_user:
        return {"error": "Invalid username or password"}
    
    encode_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return {"token": encode_jwt}

    # if data['username'] == test_user["username"] and data["password"] == test_user["password"]:
    #     encode_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    #     return {"token": encode_jwt}
    # else:
    #     return {"error": "Invalid username or password"}


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return crud.create_user(db, user)


@app.get("/users/", response_model=List[schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)

@app.get("/users/{user_id}", response_model = schemas.User)
def get_user( user_id:int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code = 404, detail= "user Not Found")
    return db_user

@app.post("/users/{user_id}/items", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_user = crud.create_item(db, item, user_id)

    return db_user

@app.get("/items/", response_model=List[schemas.Item])
def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_items(db, skip=skip, limit=limit)


