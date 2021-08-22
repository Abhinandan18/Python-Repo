from sqllite_demo import SQlOperations
from SQLEmployee import Employee

emp_1=Employee('Piyu','Patil',80000)
emp_2=Employee('Anvi','Patil',90000)
emp_3=Employee('Alwain','Schafer',40000)

SQlOperations.insert_emp(emp_1)
SQlOperations.insert_emp(emp_2)
SQlOperations.insert_emp(emp_3)

print(SQlOperations.get_emp_by_lastname('Patil'))

SQlOperations.update_emp_pay(emp_2,95000)
SQlOperations.remove_emp(emp_3)

print(SQlOperations.get_emp_by_lastname('Patil'))

SQlOperations.close_conn()

