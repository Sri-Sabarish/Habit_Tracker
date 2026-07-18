import sqlite3
# we need to connect to the database 
def connect_db():  
    conn=sqlite3.connect("habits.db")
    return conn
#nest create tables
def create_tables():
    conn=connect_db()
    cursor=conn.cursor() #cursor() act like sql executor
    cursor.execute("""CREATE TABLE IF NOT EXISTS habits(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS logs(id INTEGER PRIMARY KEY AUTOINCREMENT, habit_id INTEGER, date TEXT NOT NULL, status TEXT NOT NULL, FOREIGN KEY(habit_id) REFERENCES habits(id))""")
    conn.commit()
    conn.close()
def add_habit(name):
    conn=connect_db()
    cursor=conn.cursor()
    cursor.execute("""INSERT INTO habits(name) VALUES(?)""",(name,))
    conn.commit()
    conn.close()
def get_all_habits():
    conn=connect_db()
    cursor=conn.cursor()
    cursor.execute("""SELECT id,name from habits""")
    result=cursor.fetchall()
    conn.close()
    return result
def log_status(habit_id,date_str,status): #Daily updates - from user side
    conn=connect_db()
    cursor=conn.cursor()
    cursor.execute("""INSERT INTO logs(habit_id,date,status) VALUES(?,?,?)""",(habit_id,date_str,status))
    conn.commit()
    conn.close()
def get_logs(habit_id): #Data related to particular Hobby
    conn=connect_db()
    cursor=conn.cursor()
    cursor.execute("""SELECT date,status FROM logs WHERE habit_id=? ORDER BY date""",(habit_id,))
    result=cursor.fetchall()
    conn.close()
    return result
def reset_all_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM logs")
    cursor.execute("DELETE FROM habits")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='habits'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='logs'")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Tables created successfully!")
 
