import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_pdf(website_url, report_name):
    try:
        response = requests.get(website_url)
      
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        pdf_links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.lower().endswith('.pdf') and report_name.lower() in href.lower():
                pdf_links.append(urljoin(website_url, href))

        if not pdf_links:
            print(f"No PDF reports matching '{report_name}' found on {website_url}.")
            return
        
        pdf_url = pdf_links[0]
   
        pdf_response = requests.get(pdf_url)

        pdf_name = pdf_url.split("/")[-1]
        with open(pdf_name, 'wb') as pdf_file:
            pdf_file.write(pdf_response.content)
        
      
      
        print(f"Succesfully downloaded: {pdf_name}")

    except requests.RequestException as e:
        print(f"Error accessing {website_url}: {e}")

if __name__ == "__main__":
   
    website_url = input("Enter the website URL: ").strip()
   
    report_name = input("Enter the report name or keyword: ").strip()
   
    download_pdf(website_url, report_name)
