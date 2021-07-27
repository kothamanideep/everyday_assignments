import json
import requests
data=requests.get("https://reqres.in/api/users?page=2")
ExtractedData=data.json()
articles=ExtractedData["data"]
print(articles)
li=[]
for i in articles:
    li.append(i["first_name"])
print(li)