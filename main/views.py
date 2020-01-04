from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
 
def index(request):
    return  HttpResponse(getWrappedHTML())

def getWrappedHTML():
    r = requests.get("https://www.indiatoday.in/india")
    soup = BeautifulSoup(r.content)
   
    imageTag = soup.find("img",{"class":"header__logo-image"})
    imageTag["src"] = "https://lh3.googleusercontent.com/-5UBDpppxMQg/Wq9xTSrvqMI/AAAAAAAAAIY/jDdUeiQEFeQIEccbMMbX_yPY9ygQ_6iCwCEwYBhgL/w140-h140-p/Untitled-1.png"
    imageTag["height"] = "50%"
    imageTag["width"] = "50%"

    newsTabs = soup.findAll("div", {"class": "catagory-listing"})

    for news in newsTabs:
        heading = news.find("h2")
        heading.a.string = "Crypters Forged You"

    return str(soup)