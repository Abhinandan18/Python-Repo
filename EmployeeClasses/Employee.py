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
        #print(Employee.raise_amount) #print class variable value

class Developer(Employee):
    raise_amount=1.10
    

    def __init__(self, firstname, lastname, department, pay,prog_lang):
        super().__init__(firstname, lastname, department, pay)
        self.prog_lang=prog_lang
        

class Manager(Employee):
    

    def __init__(self, firstname, lastname, department, pay, employees=None):
        super().__init__(firstname, lastname, department, pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def list_emp(self):
        for emp1 in self.employees:
            print('-->',emp1.Empfullname())
            


dev1=Developer('Abhinandan','Patil','Tech',100000,'Python')
dev2=Developer('Piyu','Patil','HR',100000,'Non-Tech')

mgr1=Manager('Anvi','Patil','Tech',90000,[dev1])
# print(mgr1.pay)
mgr1.add_emp(dev2)
mgr1.remove_emp(dev1)
mgr1.list_emp()

print(isinstance(mgr1,Employee))
print(issubclass(Developer,Employee))

