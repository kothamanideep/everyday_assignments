import json
import  requests
data = requests.get ("https://newsapi.org/v2/top-headlines?country=in&apiKey=5b00428da5f24a4dae3f2558212dd2d8")
Extractdata = data.json()
l = Extractdata["status"]
articles = Extractdata["articles"]
print(len(articles))
vowels = "aeiou"
for i in articles:
    title = i["title"]
    count = {}.fromkeys(vowels,0)
    print(title)

    for x in title.lower():
        if x in count:
            count[x] = count[x] + 1
    print(count)


            