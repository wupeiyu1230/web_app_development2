import sqlite3
from flask import g, current_app
import os

def get_db():
    if 'db' not in g:
        db_path = os.path.join(current_app.root_path, '..', 'instance', 'database.db')
        g.db = sqlite3.connect(
            db_path,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
