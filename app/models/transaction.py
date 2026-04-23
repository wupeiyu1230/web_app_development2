from app.db import get_db

class Transaction:
    @staticmethod
    def create(user_id, category_id, type, amount, date, note=None):
        db = get_db()
        cursor = db.execute(
            'INSERT INTO transactions (user_id, category_id, type, amount, date, note) VALUES (?, ?, ?, ?, ?, ?)',
            (user_id, category_id, type, amount, date, note)
        )
        db.commit()
        return cursor.lastrowid

    @staticmethod
    def get_by_id(transaction_id):
        db = get_db()
        return db.execute('SELECT * FROM transactions WHERE id = ?', (transaction_id,)).fetchone()

    @staticmethod
    def get_all_by_user(user_id):
        db = get_db()
        return db.execute(
            '''SELECT t.*, c.name as category_name 
               FROM transactions t 
               JOIN categories c ON t.category_id = c.id 
               WHERE t.user_id = ? ORDER BY date DESC''',
            (user_id,)
        ).fetchall()

    @staticmethod
    def update(transaction_id, category_id, type, amount, date, note):
        db = get_db()
        db.execute(
            'UPDATE transactions SET category_id = ?, type = ?, amount = ?, date = ?, note = ? WHERE id = ?',
            (category_id, type, amount, date, note, transaction_id)
        )
        db.commit()

    @staticmethod
    def delete(transaction_id):
        db = get_db()
        db.execute('DELETE FROM transactions WHERE id = ?', (transaction_id,))
        db.commit()
