from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestClickLink:
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
            WebDriverWait(browser, 10).until(EC.new_window_is_opened(old_window))
            new_window = browser.window_handles
            new_window = list(set(new_window).difference(old_window))
            browser.switch_to.window(new_window[0])
            browser.close()
            browser.switch_to.window(main_window)
            time.sleep(5)

