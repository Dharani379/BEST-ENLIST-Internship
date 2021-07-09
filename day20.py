#1q
import mysql.connector
mydb=mymydb=mysql.connector.connect(host="localhost",user="root",password="Dharani@379",database="employee_management")
mycursor=mydb.cursor()
print(mydb)
dbse=mydb.cursor()
dbse.execute("CREATE DATABASE Employee_Management")
dbse=mydb.cursor()
dbse.execute("SHOW DATABASES")
for entry in dbse:
    print(entry)

mydb=mysql.connector.connect(host="localhost",user="root",password="Dharani@379",database="Employe_management")
dbse=mydb.cursor()
dbse.execute("CREATE TABLE Employee(emp_id int(10),Emp_name varchar(355),emp_salary Double)")
dbse=mydb.cursor()
dbse.excute("SHOW COLUMNS FROM Employee")
for value in dbse:
    print(value)

dbse = mydb.cursor
sql = "INSERT INTO Employee(emp_id,Emp_name,emp_salary)VALUES(%s,%s,%s,%s)"
val=[('1','sana','10000'),('2','Mani','20000'),('3','Harish','30000'),('4','Dharani','90000'),('5','Shankar','15000'),('4','honey','40000'),('5','Harika','35000'),('6','Shannu','46000'),('7','Shareen','56000'),('7','Chinnu','67000'),('8','Divya','87560'),('9','Farukh','29000'),('10','Rana','67000')]
dbse.executemany(sql,val)
mydb.commit()
print(dbse.rowcount,"was inserted.")
#1.a q
mycursor = mydb.cursor()
mycursor.execute("SELECT Emp_name,Emp_salary FROM Employee WHERE Emp_salary = (select max(Emp_salary) FROM Employee)")
myresult = mycursor.feetchall()
for x in myresult:
    print(x)

mycursor = mydb.cursor()
mycursor.execute("SELECT Emp_Name,Emp_salary FROM Employee WHERE Emp_salary = (select min(Emp_salary) from Employee)")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


#1.b q
mycursor = mydb.cursor()
mycursor.execute("SELECT COUNT(*) from Employee")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


#1.c q
mycursor = mydb.cursor()
mycursor.execute("SELECT * from Employee WHERE Emp_Name LIKE('Harika%')")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
    


    
