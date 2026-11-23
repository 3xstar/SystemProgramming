import aiosqlite

"""
users
id  name  age   status
1   Ivan  54   active
"""
async def add_user(name: str, age: int):
    async with aiosqlite.connect("test.db") as db:
        await db.execute(
            "INSERT INTO users (name, age) VALUES (?, ?)",
            (name, age)
        )
        db.commit()


async def get_all_users() -> list:
    async with aiosqlite.connect("test.db") as db:
        result = await db.execute("SELECT * FROM users")
        rows = await result.fetchall() # [(1, Ivan, 54, active), (2, Name, 33, Inactive), ...]
        return [
            {"id": row[0], "name": row[1], "age": row[2]}
            for row in rows
        ]
