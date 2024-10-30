import sqlite3

DATABASE = 'db.sqlite'
TABELA = 'leituras'

def get_all_leituras():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM {TABELA}")
    rows = cursor.fetchall()
    
    conn.close()
    return rows