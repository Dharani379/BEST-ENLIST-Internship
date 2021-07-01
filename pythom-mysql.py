#1q
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="Dharani@379")
print(mydb)
import sys
cur = mydb.cursor()
cur.execute("SELECT VERSION()")
data=cur.fetchone()
print("MYDB version :",str(data))
#2.Create a multiple tables&insert data in tables
dbse = mydb.cursor()
dbse.execute("CREATE DATABASE mydatabase")
dbse = mydb.cursor()
dbse.execute("SHOW DATABASES")
for entry in dbse:
    print(entry)
mydb = mysql.connector.connect(host="localhost",user="root",password="Dharani@379")
dbse = mydb.cursor()
dbse.execute("CREATE TABLE customers(Employee_name Varchar(255),Employee_dep Varchar(255),Employee_id Varchar(255))")
dbse = mydb.cursor()
dbse.execute("SHOW TABLES")
for value in dbse:
    print(value)
dbse = mydb.cursor()
dbse.execute("CREATE TABLE Office(emp_name Varchar(255),EMP_ADRESS Varchar(255),emp_id int(5))")
dbse = mydb.cursor()
dbse.execute("CREATE TABLE student(rollno int(5),stud_name varchar(255),Mark int(3))")
dbse = mydb.cursor()
dbse.execute("SHOW TABLES")
for value in dbse:
    print(value)


#3q
mydb = mysql.connector.connect(host="localhost",user="root",password="Dharani@379",database="mydatabase")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE EMPLOYEE1(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),adress varchar(255))")
mydb = mysql.connector.connect(host="localhost",user="root",password="Dharani@379",database = "my database")
mycursor = mydb.cursor()
sql = "INSERT INTO EMPLOYEE1 (id,name,adress)VALUES(%s, %s, %s)"
val = ("124","Renu","TNagar")
mycursor.execute(sql,val)

mydb.commit()
print(mycursor.rowcount,"record inserted")

mycursor = mydb.cursor()
sql = "INSERT INTO EMPLOYEE1 (id,name,adress)VALUES(%s, %s, %s)"
val = ("231","Reani","Bhagya Nagar")
mycursor.execute(sql,val)

mydb.commit()
print(mycursor.rowcount,"record inserted")

mycursor = mydb.cursor()
sql = "INSERT INTO EMPLOYEE1 (id,name,adress)VALUES(%s, %s, %s)"
val = [
    ('1','peter','low street4'),
    ('2','Anu','humpy'),
    ('3','mahi','palli'),
    ('4','uma','panipat')
    ('5','megha','jaipur')
    ('6','dharani','china')]
mycursor.executemany(sql,val)

mydb.commit()
print(mycursor.rowcount,"was inserted.")
mycursor= mydb.cursor()
mycursor.execute("SELECT *FROM Employee1")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
mycursor=mydb.cursor()
mycursor.execute("SELECT name FROM Employee1")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)



                  
                  





                  
                  





                  
                  

