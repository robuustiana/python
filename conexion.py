import sqlite3
def getConexion():
    conn = sqlite3.connect("canciones.db")
    conn.row_factory = sqlite3.Row

    try:
        yield conn
    finally:
        conn.close()