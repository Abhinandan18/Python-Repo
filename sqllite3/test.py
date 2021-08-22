import sqlite3
from SQLEmployee import Employee


conn=sqlite3.connect(':memory:')

c=conn.cursor()

c.execute("""CREATE Table Employees(first text,last text, pay integer)""")
#c.execute("insert into Employees values (:first,:last,:pay)",{'first':emp_5.firstname,'last':emp_5.lastname,'pay':emp_5.pay})
# conn.commit()
# c.execute("select * from Employees where last=:last",{"last":'Patil'})
# print(c.fetchall())

def insert_emp(emp):
    with conn:
        c.execute("insert into Employees values (:first,:last,:pay)",{'first':emp.firstname,'last':emp.lastname,'pay':emp.pay})

def get_emp_by_lastname(last):
    c.execute("select * from Employees where last=:last",{"last":last})
    return c.fetchall()

def update_emp_pay(emp,pay):
    with conn:
        c.execute("""update Employees set pay=:pay where first=:first,last=:last""",{"first":emp.firstname,"last":emp.lastname,"pay":emp.pay})

def remove_emp(emp):
    with conn:
        c.execute("delete from employee where first=:first and last=:last and pay=:pay",{"first":emp.firstname,"last":emp.lastname,"pay":emp.pay})

emp_1=Employee('Piyu','Patil',80000)
emp_2=Employee('Anvi','Patil',90000)
emp_3=Employee('Alwain','Schafer',40000)

insert_emp(emp_1)
insert_emp(emp_2)
insert_emp(emp_3)

print(get_emp_by_lastname('Patil'))
conn.close()