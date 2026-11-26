from pydantic import BaseModel, Field, ConfigDict, EmailStr

class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=20, examples=["John Doe"])
    email: EmailStr = Field(examples=["johndoe@gmail.com"])
    password: str = Field(min_length=8, max_length=100)

class UserPublic(BaseModel):
    id: int
    name: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)