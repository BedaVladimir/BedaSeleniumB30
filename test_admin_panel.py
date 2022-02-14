import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class TestClass:
    def test_login_admin(self):
        browser = webdriver.Firefox()
        # browser = webdriver.Chrome()
        # browser = webdriver.Edge('C:\\msedgedriver\\msedgedriver.exe')

        browser.get("http://localhost/litecart/admin/")
        browser.find_element(By.CSS_SELECTOR, ".input-wrapper>[name='username']").send_keys("admin")
        browser.find_element(By.CSS_SELECTOR, ".input-wrapper>[name='password']").send_keys("admin")
        browser.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        browser.quit()
