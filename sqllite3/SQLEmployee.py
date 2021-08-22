class Employee:
   


    def __init__(self,firstname,lastname,pay): #parameter variables are instance variable
        self.firstname=firstname
        self.lastname=lastname
        self.pay=pay
       

    def Empfullname(self):
        return '{} {}'.format(self.firstname,self.lastname)


