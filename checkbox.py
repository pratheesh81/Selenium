from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.service import Service

path = Service("/Users/pratheeshs/Desktop/drivers/geckodriver")
browser = webdriver.Firefox(service=path)

browser.get("https://www.tutorialspoint.com/selenium/practice/check-box.php")

browser.maximize_window()

time.sleep(2)

checkbox = browser.find_element(By.ID, "c_bs_1")  # correct ID
checkbox.click()
sleep(5)
checkbox.click()

time.sleep(3)

browser.quit()
