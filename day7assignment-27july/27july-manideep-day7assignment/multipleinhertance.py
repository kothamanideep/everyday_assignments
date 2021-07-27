class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived:  
    def Divide(self,a,b):  
        return a/b; 

class calculator(Calculation1,Calculation2,Derived): 
    pass


d = calculator()  
# n1=int(input("enter a number:"))
# n2=int(input("enter second number:"))
# print(d.Summation(n1,n2))  
# print(d.Multiplication(n1,n2))  
# print(d.Divide(n1,n2))  
print(issubclass(Calculation1,Calculation2))  #to check to ascess
print(issubclass(Derived,calculator))