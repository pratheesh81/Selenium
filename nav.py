from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = Service("/Users/pratheeshs/Desktop/drivers/geckodriver")
driver = webdriver.Firefox(service=path)

driver.get("http://google.com")
driver.maximize_window()
driver.execute_script()
wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='APjFqb']")))
search_box.send_keys("Python")
search_box.submit()

wait.until(EC.title_contains("Google"))

curr = driver.title
exp = "Google"
assert exp in curr, f"Test Failed! '{exp}' not in '{curr}'"
print(" Test Passed: Title contains 'Google'")

sleep(2)
print(" Going back...")
driver.back()

sleep(2)
print(" Going forward...")
driver.forward()

sleep(2)
print("Refreshing the page...")
driver.refresh()

sleep(5)
print(" Quitting browser...")
driver.quit()
