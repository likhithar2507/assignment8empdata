import sqlite3 as sql
from prettytable import PrettyTable

connection=sql.connect("EmployeesData.db")
employeeList=connection.execute("select name from sqlite_master where type='table' and name='Employee'").fetchall()
if employeeList!=[]:
    print("Table already created")
else:
    connection.execute('''create table Employee(
                                id integer primary key autoincrement,
                                empcode integer,
                                empname text,
                                emp_salary integer,
                                designation text
                                );''')
    print("Table created Successfully")

while True:
    print("1. Add Employee ")
    print("2. View Employee ")
    print("3. EXIT ")

    choice=int(input("Enter Your choice from the above manu :"))
    if choice==1:
        getempcode=input("Employee Code :")
        getempname=input("Name :")
        getsalary=input("Salary :")
        getdesig=input("Designation :")

        connection.execute("insert into Employee(empcode,empname,emp_salary,designation)\
                           values("+getempcode+",'"+getempname+"',"+getsalary+",'"+getdesig+"')")
        print("Data interted successfully")
        connection.commit()

    if choice==2:
        result = connection.execute("select * from Employee")
        table=PrettyTable(["ID","empcode","empname","emp_salary","designation"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4]])
        print(table)

    if choice==3:
        break

    else:
        print("You have choosed an Invalid option....try again by choosing valid choice..!")