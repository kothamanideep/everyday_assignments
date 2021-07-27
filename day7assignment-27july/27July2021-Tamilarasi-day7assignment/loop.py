class Cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b

a=int(input("Enter 1st num:"))
b=int(input("Enter 2nd num:"))
obj=Cal(a,b)
choice=1
while choice!=0:
    print("select an option from menu")
    print("\n")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("Addition selected: ",obj.add())
    elif choice==2:
        print("Subtraction Selected: ",obj.sub())
    elif choice==3:
        break
    else:
        print("Wrong choice")