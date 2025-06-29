from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome WebDriver
options = Options()
options.add_argument("--start-maximized")
# options.add_argument("--headless")  # Uncomment for headless mode
service = Service("/Users/pratheeshs/Desktop/drivers/chromedriver")  # 🔁 Replace with your actual path
driver = webdriver.Chrome(service=service, options=options)

try:
    # Step 1: Open Amazon India
    driver.get("https://www.amazon.in")

    # Step 2: Search for a product
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.send_keys("wireless mouse")
    search_box.send_keys(Keys.RETURN)

    # Step 3: Click the first product using full XPath (as you provided)
    product_xpath = "/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/span/div/div/div/div[2]/div/div/div[1]/a/h2"
    product_element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, product_xpath))
    )
    product_title = product_element.text
    print("🛒 Selected Product:", product_title)

    # Click the product (using JavaScript for reliability)
    driver.execute_script("arguments[0].scrollIntoView(true);", product_element)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", product_element)

    # Step 4: Handle tab switch (if new tab opens)
    time.sleep(2)
    handles = driver.window_handles
    if len(handles) > 1:
        driver.switch_to.window(handles[1])
        print("✅ Switched to new tab.")
    else:
        print("⚠️ Product opened in the same tab.")

    # Step 5: Click Add to Cart using full XPath (as you provided)
    cart_xpath = "/html/body/div[2]/div/div/div[5]/div[1]/div[4]/div/div[1]/div/div/div/form/div/div/div/div/div[4]/div/div[38]/div[1]/span/span/span/input"
    add_to_cart_button = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, cart_xpath))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", add_to_cart_button)
    print("🛒 Clicked 'Add to Cart' button")

    # Step 6: Go to Cart
    time.sleep(3)
    driver.get("https://www.amazon.in/gp/cart/view.html")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.a-truncate-cut"))
    )

    # Step 7: Check if product is in the cart
    cart_items = driver.find_elements(By.CSS_SELECTOR, "span.a-truncate-cut")
    found = any(product_title.split()[0].lower() in item.text.lower() for item in cart_items)

    if found:
        print("✅ SUCCESS: Product is in the cart.")
    else:
        print("❌ FAILURE: Product not found in the cart.")

finally:
    driver.quit()
