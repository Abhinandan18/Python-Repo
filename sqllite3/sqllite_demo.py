import sqlite3
from SQLEmployee import Employee



""" using SQL DB operations
conn=sqlite3.connect('employee.db')
c=conn.cursor()

# c.execute(\"""CREATE Table Employees(first text,last text, pay integer)\""")
# c.execute("insert into employees values ('abhinandan','patil',60000)")
emp_1=Employee('Piyu','Patil',80000)
emp_2=Employee('Anvi','Patil',90000)
emp_3=Employee('Alwain','Schafer',40000)

# c.execute("insert into employees values ('{}','{}',{})".format(emp_1.firstname,emp_1.lastname,emp_1.pay))
# c.execute("insert into employees values (?,?,?)",(emp_2.firstname,emp_2.lastname,emp_2.pay))
# c.execute("insert into employees values (:first,:last,:pay)",{"first":emp_3.firstname,"last":emp_3.lastname,"pay":emp_3.pay})
c.execute("select * from employees where last=?",('Patil',))
print(c.fetchall())

c.execute("select * from employees where last=:last",{"last":'patil'})
print(c.fetchall())

conn.commit()
conn.close()
"""


"""using in memory operations"""

class SQlOperations:
    conn=sqlite3.connect(':memory:')
    c=conn.cursor()
    c.execute("""CREATE Table Employees(first text,last text, pay integer)""")

    def insert_emp(emp):
        with SQlOperations.conn:
            SQlOperations.c.execute("insert into employees values (:first,:last,:pay)",{"first":emp.firstname,"last":emp.lastname,"pay":emp.pay})

    def get_emp_by_lastname(last):
        SQlOperations.c.execute("select * from employees where last=:last",{"last":last})
        return SQlOperations.c.fetchall()

    def update_emp_pay(emp,pay):
        with SQlOperations.conn:
            SQlOperations.c.execute("""update employees set pay=:pay where first=:first and last=:last""",{"first":emp.firstname,"last":emp.lastname,"pay":pay})

    def remove_emp(emp):
        with SQlOperations.conn:
            SQlOperations.c.execute("delete from employees where first=:first and last=:last and pay=:pay",{"first":emp.firstname,"last":emp.lastname,"pay":emp.pay})

    def close_conn():
        SQlOperations.conn.close()