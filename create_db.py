import sqlite3

# connect to database
conn = sqlite3.connect('customer.db')

# create a cursor
crsr = conn.cursor()

#create a table (only ONCE)
crsr.execute(""" CREATE TABLE customers (
                first_name text,
                last_name text,
                email text
                )
    """)

# valid datatypes: null, integer, real, text, blob 

# insert record into table
crsr.execute(" INSERT INTO customers VALUES('john', 'elder', 'john@codemy.com')")
crsr.execute(" INSERT INTO customers VALUES('Tim',  'Smith', 'tim@codemy.com' )")
crsr.execute(" INSERT INTO customers VALUES('Mary', 'Brown', 'mary@codemy.com')")

# insert multiple records at once
many_customers = [
                    ('Wes','Brown','wes@brown.com'),
                    ('Steph','Kuewa','steph@kuewa.com'),
                    ('Dan','Pas','dan@pas.com'),
                ]
crsr.executemany(" INSERT INTO customers VALUES(?,?,?) ", many_customers)

# commit our command
conn.commit()

print('DDL/DML Command(s) executed successfully...')

# query the database
crsr.execute(" SELECT * FROM customers")
# crsr.fetchone()
# crsr.fetchmany(3)
print(crsr.fetchall())

# close our connection
conn.close()