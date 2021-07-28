import smtplib
even=[]
for i in range(10):
    n = int(input("enter a numnber: "))
    if n%2==0:
        even.append(n)
print(even)
int_str = [str(x) for x in even]
print(int_str)
y = ",".join(int_str)
connection = smtplib.SMTP ("smtp.gmail.com",587)
connection.starttls()
connection.login("chedivya1998@gmail.com","Welcome@2169")
connection.sendmail("chedviya1998@gmail.com","amarthiga@gmail.com",y)
print("email has sent successfully")
connection.quit()
