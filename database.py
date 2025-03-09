import sqlite3

# Ma'lumotlar bazasiga ulanish
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

# Foydalanuvchilar jadvalini yaratish
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY)''')
conn.commit()

# Foydalanuvchi qo'shish
def add_user(user_id):
    cursor.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    conn.commit()

# Barcha foydalanuvchilarni olish
def get_all_users():
    cursor.execute("SELECT user_id FROM users")
    return [row[0] for row in cursor.fetchall()]
