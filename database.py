import mysql.connector
print("Hello")
database = mysql.connector.connect(host="localhost", user="root", password="bryce2410")
cursorobj = database.cursor()
cursorobj.execute("drop database sys")
cursorobj.execute("create database sys")
cursorobj.execute("use sys")
cursorobj.execute("create table sys.Employee(Emp_id int(12),Emp_name varchar(100),Emp_Surname varchar(100),Email varchar(100),Town varchar(100),City varchar(100))")

cursorobj.execute('''insert into  Employee values("2","Bryce","Ferreira","ferreirabryce2410@gmail.com","Vasai","Mumbai");''')

cursorobj.execute('''insert into  Employee values("3","A","ABC","ABC@gmail.com","hadapsar","pune");''')

cursorobj.execute('''insert into  Employee values("4","Jay","XYZ","JayXYZ@gmail.com","Panjim","pune");''')

cursorobj.execute('''update Employee set Emp_name="X", City ="Goa" WHERE Emp_id=4;''')

cursorobj.execute('''delete from Employee where Emp_id = "4"''')

cursorobj.execute("select * from Employee")
database.commit
myresult = cursorobj.fetchall()
print(cursorobj.rowcount, "record(s) affected")
for i in myresult:
    print(i)
