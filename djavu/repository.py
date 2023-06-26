from djavu.db import get_db
from werkzeug.security import generate_password_hash

class userRepository:
    async def list_users(self):
        db = await get_db()
        users = db.execute(
            'SELECT * FROM user'
        ).fetchall()
        return users


    def insert_user(self, username, fullname, email, password):
        db = get_db()
        try:
            db.execute(
                "INSERT INTO user (username, fullname, email, password) VALUES (?, ?, ?, ?)",
                (username, fullname,
                 email, generate_password_hash(password)),
            )
            db.commit()
        except db.IntegrityError:
            error = f"User {username} is already registered."
