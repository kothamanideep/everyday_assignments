while(True):
    print("select an option from menu")
    print("\n")
    print("1.Add")
    print("2.Sub")
    print("3.Exit")
    choice = int(input("enter your choice: "))
    if choice == 1:
        add = 4+5
        print("addition",add)
    if choice == 2:
        print("subtraction")
    if choice == 3:
        break
    else:
        print("wrong choice")