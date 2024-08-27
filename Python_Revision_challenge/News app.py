#NEWS APP (EXCERCISE 10)

#1 use the NEWSAPI and then requests module to fetch the 
# daily news related to different topics 

#2 Go to https://news.api.org/

#3 and explore the various options to build your app.

###########################################################
#SOLUTION - 

import requests
import json #read documentation

#query = input("which category of news would you like to see?:\n")
welcome = print("hello welcome to the daily news☺")
country = input("write first two letters of your country:\n")

url = (f"https://newsapi.org/v2/top-headlines?country={country}&apiKey=ac7eb036beaf48568b608d73286d2cc9")
r = requests.get(url) #to get source code of website
print(r.text) #it will give you as a text which will not be readable you have to parse it

news = json.loads(r.text) #it is in the dictionary format key-value pairs
#print(news, type(news))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-----------------------------------------------------------------------------------------------")