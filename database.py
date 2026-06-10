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
    type_options = ['full-time', 'part-time', 'internship']
    status_options = ['applied', 'rejected', 'offered', 'accepted']

    #Turn App Type Number Into Text    
    try: 
        app_type = type_options[app_type-1]
    except: 
        "Error: Invalid Type"

    #Turn App Status Number Into Text
    try:
        status = status_options[status-1]
    except:
        print("Error: Invalid Type")

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

def modify(id, title, type, status):
    slot = [] #tracks which values are subject to change
    values = [] #the values themselves

    if title: #if title has a value (has something entered to change)
        values.append(title)
        slot.append("title = ?")
    if type:
        values.append(type)
        slot.append("type = ?")
    if status:
        values.append(status)
        slot.append("status = ?")

    if len(slot) <= 0: #return if nothing ntered
        return

    values.append(id)
    query = f"UPDATE applications SET {', '.join(slot)} WHERE id = ?" #.join turns slot list into a single str
    cur.execute(query, values)
    con.commit()

def query(query):
    cur.execute(query)
    data = cur.fetchall()
    return data
