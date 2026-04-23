CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    is_default BOOLEAN DEFAULT 0,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    type TEXT NOT NULL,
    amount REAL NOT NULL,
    date DATE NOT NULL,
    note TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(category_id) REFERENCES categories(id)
);

CREATE TABLE IF NOT EXISTS budgets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    category_id INTEGER,
    amount REAL NOT NULL,
    month TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(category_id) REFERENCES categories(id)
);

-- Insert some default categories
INSERT INTO categories (name, type, is_default) VALUES ('薪水', 'income', 1);
INSERT INTO categories (name, type, is_default) VALUES ('獎金', 'income', 1);
INSERT INTO categories (name, type, is_default) VALUES ('投資', 'income', 1);
INSERT INTO categories (name, type, is_default) VALUES ('餐飲', 'expense', 1);
INSERT INTO categories (name, type, is_default) VALUES ('交通', 'expense', 1);
INSERT INTO categories (name, type, is_default) VALUES ('娛樂', 'expense', 1);
INSERT INTO categories (name, type, is_default) VALUES ('購物', 'expense', 1);
INSERT INTO categories (name, type, is_default) VALUES ('居住', 'expense', 1);
