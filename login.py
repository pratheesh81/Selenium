from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
path = Service("/Users/pratheeshs/Desktop/drivers/chromedriver")
driver = webdriver.Chrome(service=path)
username = "standard_user"
password = "secret_sauce"
login_url = "https://www.saucedemo.com/"
driver.get(login_url)
username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
username_field.send_keys(username)
password_field.send_keys(password)
login_button = driver.find_element(By.ID, "login-button")
assert not login_button.get_attribute("disabled")
login_button.click()
sleep(20)
driver.quit()