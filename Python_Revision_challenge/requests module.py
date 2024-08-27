#Request Module in Python - 

'''The requests module in python is a HTTP library that enables you to send HTTP requests using 
python code and makes it possible to interact with web service'''

# it uses 'requests' module

#1 GET REQUESTS - IT WILL GIVE SOURCE CODE IN RESPONSE

import requests
import bs4 #bs4 (Beautiful Soup 4) is used for parsing HTML/XML documents, navigating the parse tree,
#searching for elements, modifying the document, and handling malformed markup.

#response = requests.get("https://www.codewithharry.com/") #it gets all the source code of the website
#print(response.text)


#2 Post Requests - It will post the requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title":"foo",
    "body":"bar",
    "user_id":1}
headers = {"content-type":"application/json;charset=UTF-8"}

response = requests.post(url,headers = headers,json =data)


#########################################################################################

# Beautifulsoup

'''A data structure representing a parsed HTML or XML document.

Most of the methods you'll call on a BeautifulSoup object are inherited from PageElement or Tag.'''

url = "https://www.codewithharry.com/"
r = requests.get(url)

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text,'html.parser')
#print(soup.prettif()) #print page elements as string.

for heading in soup.find_all("h2"): #print all the page elements in the h2 tag.
    print(heading.text)
