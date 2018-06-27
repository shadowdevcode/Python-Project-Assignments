# Update any values in any of the tables. Print the original and updated values

import mysql.connector

db_name = 'acadview'

db = mysql.connector.connect(host='localhost', user='root', password='admin', database=db_name)

db.connect()

cur = db.cursor()
query = """SELECT * FROM book;"""
cur.execute(query)

for i in cur.fetchall():
    print(i)

print("Updation process begins for table Book ---->")

query_update_1 = """UPDATE book SET location = "Bangalore"
                           WHERE title_id = 1213;"""

cur.execute(query_update_1)

print("After updation in table book value becomes following ---->")

query_after_updation = """SELECT * FROM book;"""

cur.execute(query_after_updation)

for i in cur.fetchall():
    print(i)

print("Original values of the table Authors --->")

query_authors_original = """SELECT * FROM authors;"""

cur.execute(query_authors_original)

for i in cur.fetchall():
    print(i)

print("updation of table authors begins --->")

query_update_2 = """UPDATE authors SET firstname = "Robin"
                           WHERE author_id = 123421;"""

cur.execute(query_update_2)

print(" After updation of table author value becomes ---->")

query_authors_updation = """SELECT * FROM authors;"""

cur.execute(query_authors_updation)

for i in cur.fetchall():
    print(i)

print("Values are updated!")

db.commit()

db.close()
