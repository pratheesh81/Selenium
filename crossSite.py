from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import openpyxl
import time

wb = openpyxl.load_workbook("/Users/pratheeshs/Desktop/db.xlsx")
sheet = wb.active

BROWSER = "firefox"

if BROWSER == "chrome":
    driver = webdriver.Chrome(service=ChromeService("/Users/pratheeshs/Desktop/drivers/chromedriver"))
elif BROWSER == "firefox":
    driver = webdriver.Firefox(service=FirefoxService("/Users/pratheeshs/Desktop/drivers/geckodriver"))

driver.get("https://www.tutorialspoint.com/selenium/practice/login.php")
driver.maximize_window()

for row in sheet.iter_rows(min_row=2, values_only=True):
    username, password = row[0], row[1]


    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "email").send_keys(username)


    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)

    form = driver.find_element(By.XPATH, "//*[@id='signInForm']")
    form.click()

    time.sleep(2)
    driver.get("https://www.tutorialspoint.com/selenium/practice/login.php")

driver.quit()
