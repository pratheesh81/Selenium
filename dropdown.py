from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Firefox()

browser.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
browser.maximize_window()
time.sleep(2)

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

dropdown = Select(browser.find_element(By.ID, "state"))

dropdown.select_by_visible_text("NCR")

dropdown2 = Select(browser.find_element(By.ID, "city"))

dropdown2.select_by_visible_text("Agra")
time.sleep(3)

browser.quit()
