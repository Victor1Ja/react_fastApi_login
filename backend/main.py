from fastapi import FastAPI
from pydantic import BaseModel
import jwt
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

SECRET_KEY = "Trizibu Putybu"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 800

test_user = {
    "username": "test",
    "password":"pass"
}

app = FastAPI()

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
async def login(user: UserItem):
    data = jsonable_encoder(user)

    if data['username'] == test_user["username"] and data["password"] == test_user["password"]:
        encode_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
        return {"token": encode_jwt}
    else:
        return {"error": "Invalid username or password"}


