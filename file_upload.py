from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import Service
import time

path = Service("/Users/pratheeshs/Desktop/drivers/geckodriver")
driver = webdriver.Firefox(service=path)
driver.get("https://the-internet.herokuapp.com/upload")
driver.maximize_window()

driver.find_element(By.ID, "file-upload").send_keys("/Users/pratheeshs/Desktop/a.pdf")
driver.find_element(By.ID, "file-submit").click()
driver.back()
driver.refresh()
#driver.forward()
driver.find_element(By.ID, "file-upload").send_keys("/Users/pratheeshs/Desktop/a.pdf")
driver.find_element(By.ID, "file-submit").click()



time.sleep(2)
assert "File Uploaded!" in driver.find_element(By.TAG_NAME, "h3")
print(" File uploaded successfully!")
time.sleep(10)
driver.close()

