import sqlite3
'''
step:

1.import library
2.create connection using connect() function
3.create cursour using courser() function
4.write sql query

'''

#step1:: create connection

conn = sqlite3.connect('test.db')
print(conn)
#step2:create cursor

cur = conn.cursor()
print(cur)
def create():
    sql = "CREATE TABLE user(id INTEGER PRIMARY KEY AUTOINCREMENT,\
    first_name TEXT NOT NULL,last_name TEXT)"
    print(sql)
    print(cur.execute(sql))

create()