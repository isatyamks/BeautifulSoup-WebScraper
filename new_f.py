import pandas as pd
import requests
from bs4 import BeautifulSoup

mobile_name = []
prices = []
reviews = []

url = "https://www.flipkart.com/search?q=phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

# Update class names as per Flipkart's current structure
namesofmob = soup.find_all("div", class_="_4rR01T")  # Correct class for mobile names
pricesofmob = soup.find_all("div", class_="_30jeq3 _1_WHN1")  # Correct class for prices
reviewsofmob = soup.find_all("div", class_="_3LWZlK")  # Correct class for reviews

# Extract data
for i in namesofmob:
    mob_name = i.text
    mobile_name.append(mob_name)

for i in pricesofmob:
    mob_price = i.text
    prices.append(mob_price)

for i in reviewsofmob:
    mob_review = i.text
    reviews.append(mob_review)

# Ensure the lists have the same length before creating the DataFrame
min_length = min(len(mobile_name), len(prices), len(reviews))
mobile_name = mobile_name[:min_length]
prices = prices[:min_length]
reviews = reviews[:min_length]

# Create a DataFrame
df = pd.DataFrame({"Mobile Name": mobile_name, "Price": prices, "Reviews": reviews})

# Save to CSV
df.to_csv("web-data/flipkart.csv", index=False)

print(df)
