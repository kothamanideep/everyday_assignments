import json
import  requests
data = requests.get ("https://reqres.in/api/users?page=2")
Extractdata = data.json()
da = Extractdata["data"]
#ar = Extractdata["articles"]
print(len(da))
for i in da:
    First_name = i["first_name"]
    print(First_name)


            