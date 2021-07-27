import requests,json
data=requests.get("https://reqres.in/api/users?page=2")
ExtractedData=data.json() 
data=ExtractedData["data"]
for i in data:
    print(i["first_name"])