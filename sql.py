#!/usr/bin/env python3
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mypassword",
  database = "mydatabase"

)

mycursor = mydb.cursor()



# --------------------------------------- database -------------------------------------

mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
 print(x)


# --------------------------------------- creating TABLE --------------------------------------

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


mycursor.execute("DROP TABLE IF EXISTS customers")

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")


mycursor.execute("SHOW TABLES")


for x in mycursor:
 print(x)


#--------------------------------------- Inserting one value to custmors table --------------------------------------


sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)


mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


#--------------------------------------- Inserting to table --------------------------------------


sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

print(mycursor.rowcount, "record inserted.")

val = [
 ('Peter', 'Lowstreet 4'),
 ('Amy', 'Apple st 652'),
 ('Hannah', 'Mountain 21'),
 ('Michael', 'Valley 345'),
 ('Sandy', 'Ocean blvd 2'),
 ('Betty', 'Green Grass 1'),
 ('Richard', 'Sky st 331'),
 ('Susan', 'One way 98'),
 ('Vicky', 'Yellow Garden 2'),
 ('Ben', 'Park Lane 38'),
 ('William', 'Central st 954'),
 ('Chuck', 'Main Road 989'),
 ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")







#--------------The fetchone() -------------- return the first row of the result

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)



#--------------------------------------- SELECT from Customers table --------------------------------------



# sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)



#--------------------------------------- another SELECT ends with way from Customers table --------------------------------------

# sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)




# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )

# mycursor.execute(sql, adr)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)




#---------------------------------------  SELECT and ORDER from Customers table --------------------------------------
# sql = "SELECT * FROM customers ORDER BY name"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


#---------------------------------------  SELECT and DESC from Customers table --------------------------------------

# sql = "SELECT * FROM customers ORDER BY name DESC"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


#---------------------------------------  DELETE from Customers table --------------------------------------

# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")





# sql = "DELETE FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )

# mycursor.execute(sql, adr)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")



#---------------------------------------  DROP  Customers table --------------------------------------

# sql = "DROP TABLE customers"

# mycursor.execute(sql)





# sql = "DROP TABLE IF EXISTS customers"

# mycursor.execute(sql)




#---------------------------------------  UPDATE from Customers table --------------------------------------

# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) affected")




# sql = "UPDATE customers SET address = %s WHERE address = %s"
# val = ("Valley 345", "Canyon 123")

# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record(s) affected")




#---------------------------------------  SHOWING 5 records --------------------------------------

# mycursor.execute("SELECT * FROM customers LIMIT 5")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)





#---------------------------------------  SHOWING 5 records from row 2 --------------------------------------

# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)







#---------------------------------------  creating % inserting users Table --------------------------------------


# mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav INT)")



# sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"


# val = [
#  ('John', 154),
#  ('Peter', 154),
#  ('Amy', 155),
#  ('Hannah', 155),
#  ('Michael', 156)
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")


# mycursor.execute("CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")


#---------------------------------------  creating & inserting products Table --------------------------------------



# sql = "INSERT INTO products (id, name) VALUES (%s, %s)"

# val = [
#  (154, 'Chocolate Heaven'),
#  (155, 'Tasty Lemons'),
#  (156,'Vanilla Dreams')
# ]





# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")



#---------------------------------------  Join examples --------------------------------------

# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   INNER JOIN products ON users.fav = products.id"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   LEFT JOIN products ON users.fav = products.id"
