import os
from pprint import pprint
import lxml
import smtplib

import requests
from bs4 import BeautifulSoup

user_agent = os.environ.get("User-Agent", "User Agent value not found")
accepted_language = os.environ.get("Accepted-Language", "Accepted Language not found")
my_email = "tsounguc@mail.gvsu.edu"
password = os.environ.get("email_password", "Password not found")
endpoint = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
target_price = 100

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

if price < target_price:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # Secure connection with Transport Layer Security
        connection.starttls()
        # Login to account
        connection.login(user=my_email, password=password)
        # Send email
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Instant Pot Price Alert\n\n"
                                                                       f"The product price is now ${round(price, 2)}, "
                                                                       f"below your ${target_price} target price")
