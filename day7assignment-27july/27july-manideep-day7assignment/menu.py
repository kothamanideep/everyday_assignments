while(True):
    print("select an option from menu:\n")
    print("1.addition")
    print("2.subtraction")
    print("3.exit")
    choice=int(input("enter your choice:"))

    if choice==1:
        print("addition selected")
    
    if choice==2:
        print("subtraction selected")

    if choice==3:
        break

    else:
        print("wrong choice")
