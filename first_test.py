from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    browser = webdriver.Chrome()
    browser.get("https://en.wikipedia.org/wiki/Main_Page")
    search = browser.find_element(By.CLASS_NAME, "vector-search-box-input").send_keys("Selenium")
    button = browser.find_element(By.CSS_SELECTOR, "#searchButton").click()
finally:
    browser.quit()