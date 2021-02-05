import sqlite3

# connect to database
conn = sqlite3.connect('customer.db')

# create a cursor
crsr = conn.cursor()


# query the database
# crsr.execute(" SELECT * FROM customers")
# items = crsr.fetchall()
# print(items)
# for item in items:
#     print(item)
# print("NAME",  "\t\t\t" + "EMAIL")
# print("----",  "\t\t\t" + "-----")
# for item in items:
#     print(item[0], item[1] + "\t\t" + item[2]) 

# query the database
# crsr.execute(" SELECT rowid, * FROM customers")
# items = crsr.fetchall()
# for item in items:
#     print(item)   

# query the database
# crsr.execute(" SELECT rowid, * FROM customers WHERE last_name = 'elder'")
# crsr.execute(" SELECT * FROM customers WHERE last_name LIKE 'Br%'")
# crsr.execute(" SELECT * FROM customers WHERE email LIKE '%codemy.com'")
# items = crsr.fetchall()
# for item in items:
#     print(item)   


# update records
#----------------------------------
# crsr.execute(""" UPDATE customers SET first_name = 'Bob', 
#             last_name = 'Elder' 
#             WHERE last_name = 'elder'
#             """)
# # commit our command
# conn.commit()

# crsr.execute(" SELECT * FROM customers ")
# items = crsr.fetchall()
# for item in items:
#     print(item)  
#----------------------------------

# update records uniquely
#----------------------------------
# crsr.execute(""" UPDATE customers SET first_name = 'John', 
#             last_name = 'Elder' 
#             WHERE rowid = 1
#             """)
# # commit our command
# conn.commit()

# crsr.execute(" SELECT * FROM customers ")
# items = crsr.fetchall()
# for item in items:
#     print(item)     
#----------------------------------

# delete records uniquely
#----------------------------------
# crsr.execute(" DELETE from customers WHERE rowid = 6")
# # commit our command
# conn.commit()

# crsr.execute(" SELECT * FROM customers ")
# items = crsr.fetchall()
# for item in items:
#     print(item)     
#----------------------------------

# query the database - ORDER BY
# crsr.execute(" SELECT rowid, * FROM customers ORDER BY rowid DESC")
# crsr.execute(" SELECT rowid, * FROM customers ORDER BY last_name ASC")
# crsr.execute(""" SELECT rowid, * FROM customers 
#                 ORDER BY last_name ASC, first_name DESC
#             """)
# items = crsr.fetchall()
# for item in items:
#     print(item)  

# query the database - AND / OR
# crsr.execute(" SELECT * FROM customers WHERE last_name LIKE 'Br%' AND first_name LIKE 'Ma%'")
# crsr.execute(" SELECT * FROM customers WHERE last_name LIKE 'Br%' OR first_name LIKE 'Ma%'")
# items = crsr.fetchall()
# for item in items:
#     print(item) 

# query the database - LIMIT
# crsr.execute(" SELECT rowid, * FROM customers LIMIT 2")
crsr.execute(" SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 3")
items = crsr.fetchall()
for item in items:
    print(item) 

# delete table
# crsr.execute(" DROP TABLE customers ") 
# # commit our command
# conn.commit()


# close our connection
conn.close()