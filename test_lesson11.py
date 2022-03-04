from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

login_from = "testbeda765@email.com"


class TestRegistrationNewCustomers:

    def test_click_link_login(self, driver):
        driver.find_element(By.CSS_SELECTOR, "#navigation td a").click()

    def test_registration_customer_required_fields(self, driver):
        fname = driver.find_element(By.CSS_SELECTOR, "input[name='firstname']")
        fname.send_keys("Ivan")
        lname = driver.find_element(By.CSS_SELECTOR, "input[name='lastname']")
        lname.send_keys("Denisov")
        address = driver.find_element(By.CSS_SELECTOR, "input[name='address1']")
        address.send_keys("Moskovskya street")
        postcode = driver.find_element(By.CSS_SELECTOR, "input[name='postcode']")
        postcode.send_keys("12345")
        city = driver.find_element(By.CSS_SELECTOR, "input[name='city']")
        city.send_keys("Montgomery")
        select = driver.find_element(By.CSS_SELECTOR, "span.select2-selection__arrow")
        ActionChains(driver).move_to_element(select).click().send_keys("United States" + Keys.ENTER).perform()
        email = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        email.send_keys(login_from)
        phone = driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
        phone.send_keys(Keys.ARROW_LEFT + "123 554 77 99")
        password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password.send_keys("BedaUS")
        confirm_password = driver.find_element(By.CSS_SELECTOR, "input[name='confirmed_password']")
        confirm_password.send_keys("BedaUS")
        button = driver.find_element(By.CSS_SELECTOR, "button[name='create_account']")
        button.click()
        time.sleep(10)

    def test_logout_account(self, driver):
        driver.find_element(By.CSS_SELECTOR, "#box-account li:last-child a").click()

    def test_login_account(self, driver):
        login = driver.find_element(By.CSS_SELECTOR, "#box-account-login [name='email']")
        login.send_keys(login_from)
        password = driver.find_element(By.CSS_SELECTOR, "#box-account-login [name='password']")
        password.send_keys("BedaUS")
        button = driver.find_element(By.CSS_SELECTOR, "button[name='login']")
        button.click()

    def test_logout_account2(self, driver):
        driver.find_element(By.CSS_SELECTOR, "#box-account li:last-child a").click()
