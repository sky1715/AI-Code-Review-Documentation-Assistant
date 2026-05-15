import sqlite3

def connect_db(db_path: str):
    """Connect to a SQLite database and return the connection."""
    conn = sqlite3.connect(db_path)
    return conn

def run_query(conn, query: str):
    """Run a SQL query and return results."""
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def close_db(conn):
    """Close the database connection."""
    conn.close()