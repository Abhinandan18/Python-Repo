class Employee:
    raise_amount=1+(4/100)  #class variable
    no_of_emp =0

    def __init__(self,firstname,lastname,department,pay): #parameter variables are instance variable
        self.firstname=firstname
        self.lastname=lastname
        self.department=department
        self.pay=pay
        Employee.no_of_emp+=1

    def Empfullname(self):
        return '{} {}'.format(self.firstname,self.lastname)

    def apply_raise(self):
        self.pay=int(self.pay * Employee.raise_amount)  #modufyig the instance variable only
        print(Employee.raise_amount) #print class variable value

    @classmethod  #update class variable using class instance 
    def set_raise_amt(cls,amount):
        cls.raise_amount=amount

    @classmethod  #this will work like another constructor
    def from_string(cls,inputStr):
        firstname,lastname,dept,pay=inputStr.split('-')
        return cls(firstname,lastname,dept,pay)
        
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

emp1=Employee('Abhi','Patil','Tech',50000)  #class instance
emp2=Employee('Piyu','Patil','Tech',70000)  #class instance
# print(Employee.raise_amount)
# emp1.set_raise_amt(1.08)  #this will update the class variable which update the value in all the instances
# print(emp1.raise_amount)
# emp1.apply_raise()
# print(emp1.pay)

# print(emp2.pay)
# emp2.apply_raise()
# print(emp2.pay)

employee_str='A-P-Team-100'



emp3=Employee.from_string(employee_str)
print(emp3.department)

import datetime
my_date=datetime.date(2021,8,8)

print(Employee.is_workday(my_date))
