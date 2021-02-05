import database 

# add a record to the database
# database.add_one("Laura", "Smith", "laura@smith.com")

# delete the record with a specific id
# database.delete_one("6")

# Add many records
# many_customers = [
#                     ('Brenda','Smitherton','brenda@smitherton.com'),
#                     ('Joshua','Raintree','josh@raintree.com'),
#                ]
# database.add_many(many_customers)                

# show all the records
# database.show_all()

# lookup record by email address 
database.email_lookup('john@codemy.com')