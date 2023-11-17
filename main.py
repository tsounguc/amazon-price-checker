import os
from pprint import pprint
import lxml

import requests
from bs4 import BeautifulSoup

user_agent = os.environ.get("User-Agent", "User Agent value not found")
accepted_language = os.environ.get("Accepted-Language", "Accepted Language not found")
endpoint = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

headers = {
    "User-Agent": user_agent,
    "Accepted-Language": accepted_language
}

response = requests.get(url=endpoint, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

# pprint(soup.prettify())

price = float(f"{soup.find(name="div", 
                     id="corePriceDisplay_desktop_feature_div", 
                     class_="celwidget").find(name="span", class_="a-price-whole").getText()}{soup.find(name="div", 
                     id="corePriceDisplay_desktop_feature_div", 
                     class_="celwidget").find(name="span", class_="a-price-fraction").getText()}")

print(price)
