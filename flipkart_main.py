import pandas as pd
import requests 
from bs4 import BeautifulSoup



#this is asimple func to fetch the webdata and store it in a specific file

def fetchandsavedata(url,path):
    r= requests.get(url)
    with open(path,"w") as f:
        f.write(r.text)





url ="https://www.flipkart.com"


#here i just searched "mobiles"  on the searchbar and get this url as i can see there are about 419 page of mobile data


url_mobiles = "https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

r = requests.get(url_mobiles)

# fetchandsavedata(url_mobiles,"web-data/flipkart_mobile.html")

soup = BeautifulSoup(r.text,"lxml")

#here i share the class name of next button to soup.find and it returns the link of the next button 

np = soup.find("a",class_ ="_9QVEpD").get("href")

# print(np)

# the ouput of this print is 

# >>> "/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=2"


# #as u see that it is incomplete because its not contain the main domain name -->

# >>> https://www.flipkart.com/np


complete_np = "https://www.flipkart.com"+np


# print(complete_np)



#now see the magic i can observe the pattern in the link of each page which is quite simple just look at the last of each link the number

#so i will use the loop


# while True:
#     np = soup.find("a",class_ ="_9QVEpD").get("href")
#     complete_np = "https://www.flipkart.com"+np

#     with open("web-data/flipkart_mobile_link.txt", "w") as f:
#             f.write(complete_np)
    
#     print(complete_np)

#     url=complete_np

#     r = requests.get(url)

#     soup =BeautifulSoup(r.text,"lxml")



#after so much try i got to know that while true will not work for flipkart pages for some reason (page is only runnin  between 1 and 2)



#so lets try with for loop


for i in range (2,10):

    url_loop = "https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

    r = requests.get(url_loop)
    soup = BeautifulSoup(r.text,"lxml")

    np_loop= soup.find("a",class_ ="_9QVEpD").get("href")

    complete_np_loop = "https://www/flipkart.com"+np_loop
    
    with open("web-data/flipkart_mobile_link.txt", "a") as f:
        f.write(complete_np_loop + "\n")



#now the next mission is to scrap the data from the each pages



#making the list of items which i want to scrap from the flipkart site


mobile_name =[]
prices = []
description =[]
reviews =[]


soup =BeautifulSoup (r.text,"lxml")





