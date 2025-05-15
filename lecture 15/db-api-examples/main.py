import sqlite3


conn = sqlite3.connect("db_api_bd_example.db")
print(type(conn))

cursor = conn.cursor()
print(type(cursor))

cursor.execute("""CREATE TABLE IF NOT EXISTS user (
u_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
u_name TEXT NOT NULL,
u_surname TEXT NOT NULL
);
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS task (
t_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
t_name TEXT NOT NULL,
t_priority INTEGER NOT NULL,
u_id_fk INTEGER NOT NULL,
FOREIGN KEY(u_id_fk) REFERENCES user(u_id)
);
""")
conn.commit()

##user_data1 = ("Петя","Петров")
##
##cursor.execute("""insert into user (u_name, u_surname) values (?,?);""",user_data1)
##
##cursor.execute("""insert into user (u_name, u_surname) values (?,?);""",("Вася","Петров"))
##
##cursor.execute("""insert into task (t_name, t_priority, u_id_fk) values (?, ?, ?);
##""", ("Бегаьт", 10, 1))
##
##cursor.execute("""insert into task (t_name, t_priority, u_id_fk) values (?, ?, ?);
##""", ("Спать", 5, 2))
##
##cursor.execute("""insert into task (t_name, t_priority, u_id_fk) values (?, ?, ?);
##""", ("Лежать", 7, 1))
##
##cursor.execute("""insert into task (t_name, t_priority, u_id_fk) values (?, ?, ?);
##""", ("Отдыхать", 100, 2))

conn.commit()


##for record in cursor.execute("""select * from user;"""):
##    print(record)
##    print(record[0], record[2])

##
##cursor.execute("""select * from task;""")
##
##results = cursor.fetchall()
##print(results)
##print()
##
##for i in results:
##    print(i)

##cursor.execute("""delete from task where t_id=?;""", (9,))
##cursor.execute("""delete from task where t_id=?;""", (8,))
##conn.commit()

tp = ("Мяу","ГАВ", 2)
cursor.execute("""update user set u_name = ?, u_surname=? where u_id = ?;""", tp)


conn.commit()
