from app.db import get_db

class Category:
    @staticmethod
    def create(user_id, name, type, is_default=False):
        db = get_db()
        cursor = db.execute(
            'INSERT INTO categories (user_id, name, type, is_default) VALUES (?, ?, ?, ?)',
            (user_id, name, type, is_default)
        )
        db.commit()
        return cursor.lastrowid

    @staticmethod
    def get_by_id(category_id):
        db = get_db()
        return db.execute('SELECT * FROM categories WHERE id = ?', (category_id,)).fetchone()

    @staticmethod
    def get_all_by_user(user_id):
        db = get_db()
        return db.execute(
            'SELECT * FROM categories WHERE user_id = ? OR is_default = 1 ORDER BY type, id',
            (user_id,)
        ).fetchall()

    @staticmethod
    def update(category_id, name, type):
        db = get_db()
        db.execute(
            'UPDATE categories SET name = ?, type = ? WHERE id = ?',
            (name, type, category_id)
        )
        db.commit()

    @staticmethod
    def delete(category_id):
        db = get_db()
        db.execute('DELETE FROM categories WHERE id = ?', (category_id,))
        db.commit()
