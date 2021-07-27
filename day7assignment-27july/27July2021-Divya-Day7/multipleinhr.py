class addition:
    def add(a,b):
        return a+b
class subtraction:
    def sub(a,b):
        return a-b
class multiple:
    def mul(a,b):
        return a*b

class calculator(addition,subtraction,multiple):
    pass

objcal = calculator
n = int(input("enter a number: "))
m = int(input("enter a number: "))
print("the addition of two num:",objcal.add(n,m))
print("the sub of two num:",objcal.sub(n,m))
print("the multiply of two num:",objcal.mul(n,m))

print(issubclass(calculator,multiple))
print(issubclass(subtraction,multiple))
print(issubclass(calculator,addition))
print(issubclass(addition,multiple))

