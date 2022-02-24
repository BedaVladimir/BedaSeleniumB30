from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os


class TestAddNewProduct:
    def test_click_add_product(self, browser):
        browser.find_element(By.CSS_SELECTOR, "#box-apps-menu li:nth-child(2) a").click()
        browser.find_element(By.CSS_SELECTOR, "#content a:last-child.button").click()

    def test_add_general(self, browser):
        checkbox_status = browser.find_element(By.XPATH, "//*[@id='tab-general']//label//input[@value='1']")
        checkbox_status.click()
        name_field = browser.find_element(By.CSS_SELECTOR, "input[name='name[en]']").send_keys("King Duck")
        code = browser.find_element(By.CSS_SELECTOR, "input[name='code']").send_keys("1713161")
        categories = browser.find_element(By.XPATH, "//*[@id='tab-general']//tr[4]//tr[2]//input").click()
        default_category = Select(browser.find_element(By.CSS_SELECTOR,
                                                       "#tab-general select[name='default_category_id']"))
        default_category.select_by_value("1")
        gender_checkbox = browser.find_element(By.XPATH, "//*[@id='tab-general']//tr[7]//tr[4]//input").click()
        quantity = browser.find_element(By.CSS_SELECTOR, "input[name='quantity']")
        quantity.send_keys(Keys.CONTROL,'a' + Keys.BACK_SPACE)
        quantity.send_keys("10")
        soldout = Select(browser.find_element(By.CSS_SELECTOR, "select[name='sold_out_status_id']"))
        soldout.select_by_value("2")
        directory = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(directory, "royalduck.jpg")
        add_file = browser.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(file_path)
        date_from = browser.find_element(By.CSS_SELECTOR, "input[name='date_valid_from']")
        date_from.send_keys(Keys.HOME + "24.02.2022")
        date_to = browser.find_element(By.CSS_SELECTOR, " input[name='date_valid_to']")
        date_to.send_keys(Keys.HOME + "28.02.2022")

    def test_add_information(self, browser):
        browser.find_element(By.CSS_SELECTOR, ".index li:nth-child(2) a").click()
        manufacturer = Select(browser.find_element(By.CSS_SELECTOR, "select[name='manufacturer_id']"))
        manufacturer.select_by_value("1")
        keywords = browser.find_element(By.CSS_SELECTOR, "input[name='keywords']").send_keys("Rubber duck")
        short_desc = browser.find_element(By.CSS_SELECTOR, "input[name='short_description[en]']")
        short_desc.send_keys("Product description")
        desc = browser.find_element(By.CSS_SELECTOR, "[contenteditable='true']").send_keys("Long description")
        head_title = browser.find_element(By.CSS_SELECTOR, "input[name='head_title[en]']").send_keys("Royal Duck")
        meta = browser.find_element(By.CSS_SELECTOR, "input[name='meta_description[en]']").send_keys("Rubber")
        #time.sleep(10)

    def test_add_price(self, browser):
        browser.find_element(By.CSS_SELECTOR, ".index li:nth-child(4) a").click()
        price = browser.find_element(By.CSS_SELECTOR, "input[name='purchase_price']")
        price.send_keys(Keys.CONTROL,'a' + Keys.BACKSPACE)
        price.send_keys("5")
        currency = Select(browser.find_element(By.CSS_SELECTOR, "select[name='purchase_price_currency_code']"))
        currency.select_by_value("USD")
        price_usd = browser.find_element(By.CSS_SELECTOR, "input[name='prices[USD]']").send_keys("5")
        price_eur = browser.find_element(By.CSS_SELECTOR, "input[name='prices[EUR]']").send_keys("5")
        save_button = browser.find_element(By.CSS_SELECTOR, "button[name='save']").click()

    def test_check_new_product(self, browser):
        catalog = browser.find_element(By.CSS_SELECTOR, "table.dataTable")
        product = catalog.find_element(By.LINK_TEXT, "King Duck").click()
        time.sleep(5)