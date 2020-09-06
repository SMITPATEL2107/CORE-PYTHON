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
    sql = "create table if not exists user(id INTEGER PRIMARY KEY AUTOINCREMENT,\
    first_name TEXT NOT NULL,last_name TEXT)"
    print(sql)
    print(cur.execute(sql))

#create()

"""def insert():
    sql="INSERT INTO user(first_name,last_name)values('patel','shashank ')"
    cur.execute(sql)
    conn.commit()"""
#insert()

def read():
    sql="select * from user"
    cur.execute(sql)
    data=cur.fetchall()
    print(data)

#read()

def update():
    sql= "UPDATE user SET first_name='newfname',last_name='newlname' WHERE id=2"
    cur.execute(sql)
    conn.commit()  #save all data in table

#update()
read()

def delete():
    sql="DELETE FROM user WHERE id=1"
    cur.execute(sql)
    conn.commit()

#delete()
read()

def insert(a,b):
    sql="INSERT INTO user (first_name,last_name) values (?,?);"
    cur.execute(sql,(a,b))
    conn.commit()

insert('asdkjsk','sdjjks')
insert('asddsdjs','sdjdsdsdsjks')
insert('asssdk','sdjjkdsdsdsddfs')

read()

