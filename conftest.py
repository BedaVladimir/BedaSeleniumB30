from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(scope='session')
def browser():
    browser = webdriver.Chrome()
    # browser = webdriver.Firefox()
    # browser = webdriver.Edge('C:\\msedgedriver\\msedgedriver.exe')
    browser.maximize_window()
    browser.get("http://localhost/litecart/admin/")
    browser.find_element(By.CSS_SELECTOR, ".input-wrapper>[name='username']").send_keys("admin")
    browser.find_element(By.CSS_SELECTOR, ".input-wrapper>[name='password']").send_keys("admin")
    browser.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    yield browser
    browser.quit()


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    # driver = webdriver.Edge('C:\\msedgedriver\\msedgedriver.exe')
    driver.maximize_window()
    driver.get("http://localhost/litecart/en/")
    yield driver
    driver.quit()