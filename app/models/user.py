from app.db import get_db

class User:
    @staticmethod
    def create(username, password_hash):
        db = get_db()
        cursor = db.execute(
            'INSERT INTO users (username, password_hash) VALUES (?, ?)',
            (username, password_hash)
        )
        db.commit()
        return cursor.lastrowid

    @staticmethod
    def get_by_id(user_id):
        db = get_db()
        return db.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()

    @staticmethod
    def get_by_username(username):
        db = get_db()
        return db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

    @staticmethod
    def update(user_id, password_hash):
        db = get_db()
        db.execute(
            'UPDATE users SET password_hash = ? WHERE id = ?',
            (password_hash, user_id)
        )
        db.commit()

    @staticmethod
    def delete(user_id):
        db = get_db()
        db.execute('DELETE FROM users WHERE id = ?', (user_id,))
        db.commit()
