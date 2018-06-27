#  Create a database. Create the following tables:
# 1. Book
# 2. Titles
# 3. Publishers
# 4. Zipcodes
# 5. AuthorsTitles
# 6. Authors

import mysql.connector
# from mysql.connector import errorcode

db_name = 'acadview'

db = mysql.connector.connect(host='localhost', user='root', password='admin', database='acadview')

db.connect()

# query = """CREATE TABLE BOOK (title_id integer not null , location varchar(50), genre varchar(50) )"""

# db._execute_query(query)

db._execute_query("""CREATE TABLE TITLES (title_id integer not null , title varchar(50), isbn varchar(50) not null,
                  publisher_id varchar(60), publication_year integer    
                  )""")

db._execute_query("""CREATE TABLE PUBLISHERS (publisher_id varchar(60) not null , name char(50), street_address varchar(100),
                  serial_number varchar(50), zip_code integer    
                  )""")

db._execute_query("""CREATE TABLE ZIPCODES (zip_code_id integer not null , city char(50), state char(50),
                  zip_code integer    
                  )""")

db._execute_query("""CREATE TABLE AUTHOR_TITLES (author_title_id integer not null , author_id integer(50), title_id integer(50)
                  )""")

db._execute_query("""CREATE TABLE AUTHORS (author_id integer not null , firstname char(50), middlename char(50),
                  lastname char(50)
                  )""")
db.commit()

db.close()