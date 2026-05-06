# CLI App For Tracking Applications

#to navigate DB in commandline- sqlite3 appliations.db

#Import bulit in sqlite3 module
import sqlite3 

con = sqlite3.connect("applications.db") #open if exists or create db file
cur = con.cursor() #Database cursor allows to execute queries
cur.execute("CREATE TABLE IF NOT EXISTS applications(id INTEGER PRIMARY KEY, title, type, status, date)")


def getAppCount():
    cur.execute("SELECT COUNT(*) FROM applications")
    return cur.fetchone()[0]

def add_entry(title, app_type, status):
    query = """
    INSERT INTO applications (title, type, status, date)
    VALUES (:title, :type, :status, date());

    """
    cur.execute(query, {"title": title, "type": app_type, "status": status})
    con.commit() #actually commit to database

def remove_entry(id):
    query = """
    DELETE FROM applications
    WHERE id = ?;

    """
    cur.execute(query, (id,)) #trailing commar to distuiguish tuple
    con.commit()

def get_all():
    cur.execute("select * from applications;")
    data = cur.fetchall()
    return data
