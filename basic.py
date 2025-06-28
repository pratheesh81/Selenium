from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

path = Service("/Users/pratheeshs/Desktop/drivers/chromedriver")
driver = webdriver.Chrome(service = path)
driver.get("http://google.com")
driver.maximize_window()
var = driver.find_element(By.XPATH, "//*[@id='APjFqb']")
var.send_keys("Python")
sleep(2)
var.submit()

curr = driver.title
exp = "Google"
assert exp in curr, f"Test Failed!  '{exp}' '{curr}'"
print("✅ Test Passed: Title contains 'Google'")

#if exp in curr:
   # print("Success!")
#else:
    #print("Failed!")

sleep(20)
driver.quit()