from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class InstaBot():

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")

    def enter_link(self, link):
        self.driver.get(link)
    
    def get_photos_links(self):
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        
        all_links = list()
        for current_link in links:
            href = current_link.get_attribute('href')
            if(href.startswith("https://www.instagram.com/p/")):
                all_links.append(href)

        return all_links

    def give_like(self):
        like = self.driver.find_elements(by=By.CLASS_NAME, value='_abl-')
        like[1].click()

    def comment(self):
        pass

bot = InstaBot()
bot.enter_link("https://www.instagram.com/")
time.sleep(20)
bot.enter_link("#Instagram User")
time.sleep(3)
links_photos = bot.get_photos_links()

for link in links_photos:
    bot.enter_link(link)
    time.sleep(1)
    bot.give_like()
    time.sleep(2)
