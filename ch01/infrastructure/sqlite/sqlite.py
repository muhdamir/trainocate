import sqlite3


def get_db():
    try:
        conn = sqlite3.connect(
            "./ch01/infrastructure/sqlite/inventory.db", check_same_thread=False
        )
        yield conn.cursor()
    except Exception as e:
        print(e)
    finally:
        conn.close()
