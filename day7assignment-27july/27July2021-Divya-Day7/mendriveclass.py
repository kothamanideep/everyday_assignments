class choiceMaking:
    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b

choice = int(input("enter your choice: "))
n = int(input("enter a number: "))
m = int(input("enter a number: "))
cm = choiceMaking()
while(True):
    print("select option from menu")
    print("1.addition")
    print("2.subtraction")
    print("3.Exit")  
    
    
    if choice == 1:
        #print("addition")
        print("The sum of two number : ",cm.addition(n,m))
        break
    elif choice == 2:
        #print("subtraction")
        print("The sub of two number : ",cm.subtraction(n,m))
        break
    elif choice == 3:
        print("Exit key pressed")
        break
    else:
        print("wrong choice")

