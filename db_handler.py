import sqlite3

def get_user_data(user_id):
    # New connection for every query - performance issue
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # SQL injection vulnerability
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

    result = cursor.fetchall()
    conn.close()
    return result

def update_user_status(user_id, status):
    # Another connection - resource intensive
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # No error handling or transaction management
    cursor.execute(f"UPDATE users SET status = '{status}' WHERE id = {user_id}")
    conn.commit()
    conn.close()
