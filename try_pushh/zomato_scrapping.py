from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.zomato.com/mumbai/ettarra-1-juhu/reviews")
wait = WebDriverWait(driver, 10)
user_data = driver.find_elements(By.XPATH, '//*[@id="root"]/div/main/div/section[4]/div/div/section/div[2]')
print(user_data[0].text)

# //*[@id="root"]/div/main/div/section[3]/section/section/div/div/div/section/div[1]/div[1]/div/div/div[2]
# //*[@id="tablink_clsvufnp5002c3578k5ridb24__2"]/a
# //*[@id="root"]/div/main/div/section[3]/section/section/div/div/div/section/div[3]/div[1]/div/div/div[1]
#//*[@id="root"]/div/main/div/section[4]/div/div/section/div[1]/div[1]/div/div/div/div/span/p
#//*[@id="root"]/div/main/div/section[4]/div/div/section
#//*[@id="root"]/div/main/div/section[4]/div/div/section/div[1]/div[1]
#//*[@id="root"]/div/main/div/section[4]/div/div/section
#//*[@id="root"]/div/main/div/section[4]/div/div/section/div[1]
#//*[@id="root"]/div/main/div/section[4]/div/div/section/div[2]