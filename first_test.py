from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    browser = webdriver.Chrome()
    browser.get("https://www.google.ru/")
    button = browser.find_element(By.CSS_SELECTOR, ".FPdoLc.lJ9FBc .RNmpXc").click()
finally:
    browser.quit()