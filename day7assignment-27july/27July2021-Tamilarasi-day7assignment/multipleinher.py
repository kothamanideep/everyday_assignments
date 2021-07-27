class AddOperation:
    def AddTwoNo(self,a,b):
        return a+b
    
class SubOperation:
    def SubTwoNo(self,a,b):
        return a-b

class MulOperation:
    def MulTwoNo(self,a,b):
        return a*b

class Calculator(AddOperation,SubOperation,MulOperation):
    pass

objcalc=Calculator()
# n1=int(input("Enter the 1st num:"))
# n2=int(input("Enter the 2nd num:"))
# print(objcalc.MulTwoNo(n1,n2))
# print(objcalc.AddTwoNo(n1,n2))
# print(objcalc.SubTwoNo(n1,n2))
print(issubclass(SubOperation,Calculator))
print(issubclass(SubOperation,AddOperation))