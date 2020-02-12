#base datos
#http://docs.peewee-orm.com/en/latest/peewee/installation.html
#pip install peewee
# o bien git clone https://github.com/coleifer/peewee.git
# cd peewee
# python setup.py install
#python runtests.py
#sudo pip3 install PyMySQL
import pymysql
import pymysql.cursors

con = pymysql.connect('192.168.0.7', 'victor','vvgvvg', 'zurbaies')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Alumnos")

    rows = cur.fetchall()

    for row in rows:
        print("{0} {1} {2}".format(row[0], row[1], row[2]))

    cur.execute("SELECT * FROM Alumnos")

    rows = cur.fetchall()

    for row in rows:
        #print(row["Nombre"], row["DniAlumno"], row("Domicilio"))
        print("{0}".format(row[0]))

con.close()

## Connecting to the database

## importing 'mysql.connector' as mysql for convenient
#pip3 install mysql.connector
import mysql.connector as mysql

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "192.168.0.7",
    user = "victor",
    passwd = "vvgvvg"
)

## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = db.cursor()

## creating a databse called 'datacamp'
## 'execute()' method is used to compile a 'SQL' statement
## below statement is used to create tha 'datacamp' database
try:
    cursor.execute("CREATE DATABASE datacamp")
except mysql.Error as err:
    print("Dabase ya creada", err)
except :
    print("Error desconocido")

## executing the statement using 'execute()' method
cursor.execute("SHOW DATABASES")

## 'fetchall()' method fetches all the rows from the last executed statement
databases = cursor.fetchall() ## it returns a list of all databases present

## printing the list of databases
print(databases)

## showing one by one database
for database in databases:
    print(database)

db.close()

import mysql.connector as mysql

db = mysql.connect(
    host = "192.168.0.7",
    user = "victor",
    passwd = "vvgvvg",
    database = "datacamp"
)

cursor = db.cursor()

## creating a table called 'users' in the 'datacamp' database
#cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")
## creating the 'users' table again with the 'PRIMARY KEY'
#cursor.execute("DROP TABLE users")
try:
    cursor.execute("CREATE TABLE users (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), user_name VARCHAR(255))")
except mysql.Error as err:
    print("tabla ya creada", err)
## 'DESC table_name' is used to get all columns information
cursor.execute("DESC users")

## it will print all the columns as 'tuples' in a list
print(cursor.fetchall())

cursor = db.cursor()

## defining the Query
query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
## storing values in a variable
values = [
    ("Peter", "peter"),
    ("Amy", "amy"),
    ("Michael", "michael"),
    ("Hennah", "hennah")
]

## executing the query with values
cursor.executemany(query, values)

## to make final output we have to run the 'commit()' method of the database object
db.commit()

print(cursor.rowcount, "records inserted")

## defining the Query
query = "SELECT * FROM users"

## getting records from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

## Showing the data
for record in records:
    print(record)

## defining the Query
query = "DELETE FROM users WHERE id = 5"

## executing the query
cursor.execute(query)

## final step to tell the database that we have changed the table data
db.commit()

## defining the Query
query = "UPDATE users SET name = 'Kareem' WHERE id = 1"

## executing the query
cursor.execute(query)

## final step to tell the database that we have changed the table data
db.commit()

db.close()


from decimal import Decimal
from datetime import datetime, date, timedelta

import mysql.connector

# Connect with the MySQL Server
#cnx = mysql.connector.connect('192.168.0.7', 'victor','vvgvvg', 'zurbaies')

cnx = mysql.connector.connect(user='victor', password='vvgvvg', database='employees',host='192.168.0.7',port='3306')

#con = pymysql.connect('192.168.0.7', 'victor','vvgvvg', 'zurbaies')
# Get two buffered cursors
curA = cnx.cursor(buffered=True)
curB = cnx.cursor(buffered=True)

#try:
curA.execute("CREATE TABLE IF NOT EXISTS employees (emp_no INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),hire_date DATE)")
curA.execute("CREATE TABLE IF NOT EXISTS salaries (emp_no INT(11) , salary INT, from_date DATE, to_date DATE)")
query = "INSERT INTO employees (name,hire_date) VALUES ('victor',DATE('1000-01-01'))"
curA.execute(query)
cnx.commit()

query = "SELECT  emp_no FROM employees as a WHERE a.name='victor' AND a.hire_date=DATE('1000-01-01')"
curB.execute(query)
#rows = curB.fetchall()
#row=rows[0]
#print("rows:", rows, "row", row, "row0", rows[0])
query = "INSERT INTO salaries (salary,from_date,to_date) VALUES (1000,DATE('1000-01-01'),DATE('9999-01-01'))"
curA.execute(query,row[0])


query = "INSERT INTO salaries (emp_no,salary,from_date,to_date) VALUES (%i,1000,DATE('1000-01-01'),DATE('9999-01-01'))"
#curA.execute(query,row[0])
cnx.commit()
#except mysql.Error as err:
#    print("tabla ya creada", err)

# Query to get employees who joined in a period defined by two dates
query = (
  "SELECT s.emp_no, salary, from_date, to_date FROM employees AS e "
  "LEFT JOIN salaries AS s USING (emp_no) "
  "WHERE to_date = DATE('9999-01-01')"
  "AND e.hire_date BETWEEN DATE(%s) AND DATE(%s)")

# UPDATE and INSERT statements for the old and new salary
update_old_salary = (
  "UPDATE salaries SET to_date = %s "
  "WHERE emp_no = %s AND from_date = %s")
insert_new_salary = (
  "INSERT INTO salaries (emp_no, from_date, to_date, salary) "
  "VALUES (%s, %s, %s, %s)")

# Select the employees getting a raise
curA.execute(query, (date(2000, 1, 1), date(2000, 12, 31)))

# Iterate through the result of curA
for (emp_no, salary, from_date, to_date) in curA:

  # Update the old and insert the new salary
  new_salary = int(round(salary * Decimal('1.15')))
  curB.execute(update_old_salary, (tomorrow, emp_no, from_date))
  curB.execute(insert_new_salary,
               (emp_no, tomorrow, date(9999, 1, 1,), new_salary))

  # Commit the changes
  cnx.commit()

cnx.close()

#import peewee as pw
from peewee import *

myDB = MySQLDatabase("datacamp", host="192.168.0.7", port=3306, user="victor", passwd="vvgvvg")


class MySQLModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = myDB

class Users(MySQLModel):
    id = IntegerField(unique=True)
    name = CharField()
    user_name = CharField()

    class Meta:
        database = myDB

def create_table():
    with myDB:
        myDB.create_tables([Users])

# when you're ready to start querying, remember to connect
myDB.connect()

#myDB.create_tables()
try:
    with myDB.atomic():
        user = Users.create(name="Victor",user_name="usuario")
        print("Registro insertado")
except IntegrityError:
    #flash('That username is already taken')
    print("Registro existente")

#list records
for user in user.select():
    print(user.name," ",user.user_name)

for user in user.select().where(user.name == "Victor"):
    print(user.name)

myDB.close()