#http://127.0.0.1:8000/docs
@app.post("/webhook/weather")
async def weather_webhook(payload: dict):
    required_fields: list = [
        "city",
        "temperature",
        "description",
        "wind_speed"
    ]

    for field in required_fields:
        if field not in payload:
            raise HTTPException(
                status_code=400,
                detail="В данных нет нужных полей"
            )

    await save_weather_to_db(
        payload["city"],
        payload["temperature"],
        payload["description"],
        payload["wind_speed"],
    )

    return {
        "status": 200,
        "city": payload["city"]
    }

user_data = {"login": "Vladimir", "password": "123654"}


@app.post("/login")
async def user_login(payload: dict):
    username = payload["username"]
    password = payload["password"]

    if not username or not password:
        raise HTTPException(
            status_code=400,
            detail="В данных нет нужных полей"
        )

    if users_db.get(username) != password:
        query = select(Users).where(username=username)
        db.execute(query).fetchone()

        async with aiosqlite.connect(DB_NAME) as db:
            cursor = await db.execute(
                "SELECT password FROM users WHERE username=?",
                (username,)
            )
            result = await cursor.fetchone()
        