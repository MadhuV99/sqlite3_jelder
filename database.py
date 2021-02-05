import sqlite3

# query the database
def show_all():
    # connect to database & create a cursor
    conn = sqlite3.connect('customer.db')
    crsr = conn.cursor()

    # query the database
    crsr.execute(" SELECT rowid, * FROM customers")
    items = crsr.fetchall()
    for item in items:
        print(item) 

    # close the connection
    conn.close()

# query for email with WHERE clause
def email_lookup(email):
    # connect to database & create a cursor
    conn = sqlite3.connect('customer.db')
    crsr = conn.cursor()

    # query the database
    crsr.execute(" SELECT rowid, * FROM customers WHERE email = (?)", (email,))
    items = crsr.fetchall()
    for item in items:
        print(item) 

    # close the connection
    conn.close()

def add_one(first, last, email):
    # connect to database & create a cursor
    conn = sqlite3.connect('customer.db')
    crsr = conn.cursor()

    # insert one record into table
    crsr.execute(" INSERT INTO customers VALUES (?,?,?) ", (first, last, email))

    # close the connection after commit
    conn.commit()
    conn.close()    

def add_many(many_customers):
    # connect to database & create a cursor
    conn = sqlite3.connect('customer.db')
    crsr = conn.cursor()

    # insert many records into table
    crsr.executemany(" INSERT INTO customers VALUES(?,?,?) ", (many_customers))

    # close the connection after commit
    conn.commit()
    conn.close()    

def delete_one(id):
    # connect to database & create a cursor
    conn = sqlite3.connect('customer.db')
    crsr = conn.cursor()

    # insert record into table
    crsr.execute(" DELETE from customers WHERE rowid = (?) ",id)

    # close the connection after commit
    conn.commit()
    conn.close()    
