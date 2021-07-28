class Employee:
    def __init__(self):
        self.name='AADRIKA '
        self.salary=30000
    def __str__(self):
        return 'name= '+self.name+' salary= RS'+str(self.salary)
e1=Employee()
print(e1)