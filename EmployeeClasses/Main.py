from Employee import Employee


Employee.no_of_emp=10  #Class variable change
print(Employee.no_of_emp)   #Global variable access

emp1=Employee('Abhi','Patil','Tech',50000)  #class instance
emp2=Employee('Piyu','Patil','HR',60000)

emp1.apply_raise() 
print(emp1.pay)

# Employee.raise_amount=1.06

emp2.apply_raise()
print(emp2.pay)

print(Employee.no_of_emp)  #print class variable