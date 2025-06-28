from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


from selenium.webdriver.common.by import By

path = Service("/Users/pratheeshs/Desktop/drivers/chromedriver")
driver = webdriver.Chrome(service = path)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
v1 = driver.find_element(By.NAME,"user-name")
v1.send_keys("standard_user")
v1.submit()
v2 = driver.find_element(By.NAME,"password")
v2.send_keys("secret_sauce")
v2.submit()
a = driver.current_url
b = "inventory.html"
assert a in b, f"Test Failed!  '{a}' '{b}'"
print("Success: From, To, and Date selected.")
time.sleep(3)
driver.quit()

#assert
sleep(30)
driver.close()
