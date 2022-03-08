from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestClickLink:
    def test_go_to_country(self, browser):
        browser.find_element(By.CSS_SELECTOR, "#box-apps-menu li:nth-child(3) a").click()
        browser.find_element(By.CSS_SELECTOR, "#content .row td:nth-child(5) a").click()

    def test_code_window(self, browser):
        link = browser.find_element(By.XPATH, "//form//tr[2]//a").click()
        window = browser.window_handles
        wait = WebDriverWait(browser, 10)
        wait.until(EC.new_window_is_opened(browser.window_handles[1]))
        browser.switch_to.window(browser.window_handles[1])
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
        time.sleep(10)

    def test_click_all_link(self, browser):
        browser.find_element(By.CSS_SELECTOR, "#box-apps-menu li:nth-child(3) a").click()
        browser.find_element(By.CSS_SELECTOR, "#content .row td:nth-child(5) a").click()

        all_link = browser.find_elements(By.XPATH, ".//*[@id='content']/form/table[1]//a[@target='_blank']")

        main_window = browser.current_window_handle
        print("main_window = ", main_window)
        old_window = browser.window_handles
        print("old_window = ", old_window)

        for i in range(len(all_link)):
            all_link[i].click()
            time.sleep(5)
            new_window = browser.window_handles
        #    print("new_window = ", new_window)
            new_window = list(set(new_window).difference(old_window))
        #    print("new_window = ", new_window)
            browser.switch_to.window(new_window[0])
            browser.close()
            browser.switch_to.window(main_window)
            time.sleep(5)

