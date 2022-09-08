from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd

class WeWave:
    def __init__(self, profiles_url_f):
        self.driver = webdriver.Chrome(service=Service("/usr/local/bin/chromedriver"))
        self.profiles_url = profiles_url_f

    def get_profile(self, profile_link):
        profile_dict = {}
        self.driver.get(profile_link)
        try:
            name = self.driver.find_element(By.XPATH, "//h1[@class= 'product-single__title heading-pd']").text
        except:
            exit()
        try:
            price = self.driver.find_element(By.XPATH, "//span[@class = 'price-item price-item--regular']").text
        except:
            exit()
        try:
            product_description = self.driver.find_element(By.XPATH,"//div[@class = 'product-single__description rte']").text
        except:
            exit()
        profile_dict.update({"Name": name, "Price": price, "Description": product_description, "Product Link": profile_link})
        return profile_dict

    def extract_profiles(self):
        self.dict_of_profiles = {}
        lst_of_prof = []
        lst_names = []
        lst_price = []
        lst_description = []
        lst_link = []

        for profile in self.profiles_url:
            lst_of_prof.append(self.get_profile(profile))
        self.driver.close()

        for profile in lst_of_prof:
            lst_names.append(profile["Name"])
            lst_price.append(profile["Price"])
            lst_description.append(profile["Description"])
            lst_link.append(profile["Product Link"])

        self.dict_of_profiles.update({"Names": lst_names, "Prices": lst_price, "Descriptions": lst_description, "Links": lst_link})

    def process_output(self):
        df = pd.DataFrame.from_dict(self.dict_of_profiles)
        df.to_excel('output.xlsx', index = False) #Index is used for showing row, in both cases :p
        df.to_csv('output.csv', index = False)

    def run(self):
        self.extract_profiles()
        self.process_output()



profiles_url = [
    "https://wewave.com/collections/featured/products/david-hasselhoff",
    "https://wewave.com/collections/featured/products/huub-smit",
    "https://wewave.com/collections/featured/products/tim-wiese",
    "https://wewave.com/collections/featured/products/ralf-richter",
    "https://wewave.com/collections/featured/products/carmen-goglin",
    "https://wewave.com/collections/featured/products/roberto-blanco"
    ]

class_element = WeWave(profiles_url)
class_element.run()