from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=Fn0ZDmalU6o")
wait = WebDriverWait(driver, 10)
time.sleep(10)
for _ in range(3):
    driver.execute_script("scrollBy(0, 300)")
    time.sleep(5)
user_data = driver.find_elements(By.XPATH, '//*[@id="content-text"]')
print([i.text for i in user_data])