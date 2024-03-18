from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import csv


driver = webdriver.Chrome(options=chrome_options)

# links of competetors are stored in 'links' list
driver.get("https://www.zomato.com/mumbai/ettarra-1-juhu")
time.sleep(1)
links = []

# link_elements = driver.find_elements(By.CLASS_NAME, '//*[@id="root"]/div/main/div/section[4]/section/section/article[1]/section[2]/section/div/section/section/section/section/section[1]/div/a[1]')
# links = {link_element.get_attribute("href") for link_element in link_elements}
for i in range(1,4):
    xpath = f'//*[@id="root"]/div/main/div/section[4]/section/section/article[1]/section[2]/section/div/section/section/section/section/section[{i}]/div/a[1]'
    link_element = driver.find_element(By.XPATH, xpath)
    links.append(link_element.get_attribute("href"))

print(links)
driver.quit()

