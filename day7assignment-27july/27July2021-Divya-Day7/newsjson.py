import json
import  requests
data = requests.get ("https://newsapi.org/v2/top-headlines?country=in&apiKey=5b00428da5f24a4dae3f2558212dd2d8")
Extractdata = data.json()
l = Extractdata["status"]
articles = Extractdata["articles"]
print(len(articles))
vowels = "aeiou"
count = 0
for ar in articles:
        title = ar['title']
        print(title)

        for i in title.lower():
            if i in vowels:
                count+=1
        print(count)


            