from app.db import get_db

class Budget:
    @staticmethod
    def create(user_id, amount, month, category_id=None):
        db = get_db()
        cursor = db.execute(
            'INSERT INTO budgets (user_id, category_id, amount, month) VALUES (?, ?, ?, ?)',
            (user_id, category_id, amount, month)
        )
        db.commit()
        return cursor.lastrowid

    @staticmethod
    def get_by_id(budget_id):
        db = get_db()
        return db.execute('SELECT * FROM budgets WHERE id = ?', (budget_id,)).fetchone()

    @staticmethod
    def get_all_by_user_month(user_id, month):
        db = get_db()
        return db.execute(
            'SELECT * FROM budgets WHERE user_id = ? AND month = ?',
            (user_id, month)
        ).fetchall()

    @staticmethod
    def update(budget_id, amount):
        db = get_db()
        db.execute(
            'UPDATE budgets SET amount = ? WHERE id = ?',
            (amount, budget_id)
        )
        db.commit()

    @staticmethod
    def delete(budget_id):
        db = get_db()
        db.execute('DELETE FROM budgets WHERE id = ?', (budget_id,))
        db.commit()
