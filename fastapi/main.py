from schemas import UserPublic, UserCreate

app = FastAPI()


@app.post(
    "/users",
    response_model=UserPublic,
    status_code=status.HTTP_201_CREATED
) 
async def create_user(user: UserCreate) -> UserPublic:
    fake_db_record = {
        "id": 1,
        "name": user.name,
        "email": user.email,
        "hashed_password": user.password  # Assuming password is hashed before storage
    }
    return UserPublic(**fake_db_record)