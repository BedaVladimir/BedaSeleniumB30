from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class TestSticker:
    def test_find_sticker_new(self, browser):
        browser.find_element(By.CSS_SELECTOR, "a .fa.fa-chevron-circle-left").click()
        ducks = browser.find_elements(By.CSS_SELECTOR, "li a.link")
        for ducks in ducks:
            try:
                sticker_new = browser.find_element(By.CLASS_NAME, "sticker new")
                return True
            except NoSuchElementException:
                return False

    def test_find_sticker_sale(self, browser):
        browser.find_element(By.CSS_SELECTOR, "a .fa.fa-chevron-circle-left").click()
        ducks = browser.find_elements(By.CSS_SELECTOR, "li a.link")
        for ducks in ducks:
            try:
                sticker_sale = browser.find_element(By.CLASS_NAME, "sticker sale")
                return True
            except NoSuchElementException:
                return False