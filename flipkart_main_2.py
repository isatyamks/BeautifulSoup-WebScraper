import pandas as pd

import requests 
from bs4 import BeautifulSoup



mobile_name =[]
prices = []
description =[]
reviews =[]
datasets=[]


url_loop = "https://www.flipkart.com/search?q=phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"

r =requests.get(url_loop)


soup =BeautifulSoup(r.text,"lxml")

namesofmob = soup.find_all("div",class_="KzDlHZ")
pricesofmob = soup.find_all("div",class_="Nx9bqj _4b5DiR")
# descriptionofmob = soup.find_all("div",class_="J+igdf")
reviewsofmob = soup.find_all("div",class_="XQDdHH")


#     with open("web-data/flipkart_mobile_link.txt", "a") as f:
#         f.write(mob_name + "\n")



for i in namesofmob:
    mob_name =i.text
    mobile_name.append(mob_name)
for i in namesofmob:
    mob_reviews =i.text
    reviews.append(mob_reviews)
for i in pricesofmob:
    mob_prices =i.text
    prices.append(mob_prices)



# print(reviews)
#print(description)
# print(len(reviews))
print(prices)
print(len(prices))
# # print(mobile_name)
# print(len(mobile_name))

    

#now using

df =pd.DataFrame({"Mobiles Name": mobile_name,"Prices": prices,"Reviews": reviews})


print(df)

df.to_csv("web-data/flipkart.csv")