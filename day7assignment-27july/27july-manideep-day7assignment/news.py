import requests
import json
data=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=5b00428da5f24a4dae3f2558212dd2d8")
ExtractedData=data.json()
#print(ExtractedData)
articles=ExtractedData["articles"]
# print(len(articles))
for i in articles:
    print(i["title"])

    def vowel_count(i):
      count = 0
      vowel = set("aeiouAEIOU")
      for alphabet in i:
    
         if alphabet in vowel:
            count = count + 1
      
      print("No. of vowels :", count) 
    i = i["title"]
    vowel_count(i)

