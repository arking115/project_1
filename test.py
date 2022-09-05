from tokenize import Name
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd

profiles_url = [
    "https://wewave.com/collections/featured/products/david-hasselhoff",
    "https://wewave.com/collections/featured/products/huub-smit",
    #"https://wewave.com/collections/featured/products/tim-wiese",
    #"https://wewave.com/collections/featured/products/ralf-richter",
    #"https://wewave.com/collections/featured/products/carmen-goglin",
    #"https://wewave.com/collections/featured/products/roberto-blanco"
    ]

def get_profile(profile_link):
    profile_dict = {}
    driver = webdriver.Chrome(service=Service("/usr/local/bin/chromedriver"))
    driver.get(profile_link)
    name = driver.find_element(By.XPATH, "//h1[@class= 'product-single__title heading-pd']")
    price = driver.find_element(By.XPATH, "//span[@class = 'price-item price-item--regular']")
    product_description = driver.find_element(By.XPATH,"//div[@class = 'product-single__description rte']")
    profile_dict.update({"Name": name.text, "Price": price.text, "Description": product_description.text, "Product Link": profile_link})
    return profile_dict

dict_of_profiles = {}
lst_of_prof = []
lst_names = []
lst_price = []
lst_description = []
lst_link = []

for profile in profiles_url:
    lst_of_prof.append(get_profile(profile))

for profile in lst_of_prof:
    lst_names.append(profile["Name"])
    lst_price.append(profile["Price"])
    lst_description.append(profile["Description"])
    lst_link.append(profile["Product Link"])

dict_of_profiles.update({"Names": lst_names, "Prices": lst_price, "Descriptions": lst_description, "Links": lst_link})

print(pd.DataFrame.from_dict(dict_of_profiles))