import sqlite3

def connect():
    conn=sqlite3.connect("logi.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS logi (id INTEGER PRIMARY KEY, user_name text, password text, email text, mobile integer)")
    conn.commit()
    conn.close()

def insert(user_name,password,email,mobile):
    conn=sqlite3.connect("logi.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO logi VALUES (NULL,?,?,?,?)",(user_name,password,email,mobile))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("logi.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM logi")
    rows=cur.fetchall()
    conn.close()
    return rows
def search(user_name="",password=""):
    conn=sqlite3.connect("logi.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM logi WHERE user_name=? AND password=?", (user_name,password))
    rows=cur.fetchall()
    conn.close()
    return rows

connect()

print(view())
