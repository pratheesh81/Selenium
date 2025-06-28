from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome driver
driver = webdriver.Chrome(service=ChromeService("/Users/pratheeshs/Desktop/drivers/chromedriver"))

# Open the Cleartrip Flights page
driver.get("https://www.cleartrip.com/flights")
driver.maximize_window()

wait = WebDriverWait(driver, 20)

# Wait for and enter the From location
from_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'From')]")))
from_input.click()
from_input.send_keys("Chennai")
time.sleep(1)
from_input.send_keys(Keys.ENTER)

# Wait for and enter the To location
to_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'To')]")))
to_input.click()
to_input.send_keys("Delhi")
time.sleep(1)
to_input.send_keys(Keys.ENTER)

# Select Departure Date (e.g. 15 July 2025)
date_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Departure')]")))
date_button.click()
time.sleep(1)
driver.find_element(By.XPATH, "//div[@aria-label='15 July 2025']").click()

# Click the Search Flights button
search_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Search flights')]")))
search_btn.click()

# Wait and close browser
time.sleep(10)
driver.quit()
