import requests as rq
from bs4 import BeautifulSoup

#this is asimple func to fetch the webdata and store it in a specific file

def fetchandsavedata(url,path):
    r= rq.get(url)
    with open(path,"w") as f:
        f.write(r.text)

def fet(url,path):
    r= rq.get(url)
    soup = BeautifulSoup(r.text,"lxml")


#my quora profile page


url1 = "https://www.quora.com/profile/Isatyamks"

fet(url1,"web-data/quora.html")


