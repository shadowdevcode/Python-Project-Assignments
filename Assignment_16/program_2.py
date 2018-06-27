# Insert values in the tables

import mysql.connector

db_name = 'acadview'

db = mysql.connector.connect(host='localhost', user='root', password='admin', database=db_name)

db.connect()

db._execute_query("""INSERT INTO book(title_id,
         location, genre)
         VALUES (1213, 'College', 'JamesBond')""")

db._execute_query("""INSERT INTO titles(title_id,
         title, isbn, publisher_id, publication_year)
         VALUES (1213, 'Agent', 'abc123', 'abc1234', 2012)""")

db._execute_query("""INSERT INTO publishers(publisher_id,
         name, street_address, serial_number, zip_code)
         VALUES ('abc1234', 'Roosvelt', 'Cape Town, South Africa', 12345, 1350011)""")

db._execute_query("""INSERT INTO zipcodes(zip_code_id,
         city, state, zip_code)
         VALUES (121341, 'cape town', 'south africa', 1250011)""")

db._execute_query("""INSERT INTO author_titles(author_title_id,
         author_id, title_id)
         VALUES (1213412, 123421, 1213)""")

db._execute_query("""INSERT INTO authors(author_id,
         firstname, middlename, lastname)
         VALUES (123421, 'Test', 'User', 'Admin')""")

db.commit()

db.close()
