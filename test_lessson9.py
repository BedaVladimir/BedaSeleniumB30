from selenium.webdriver.common.by import By


class TestCountryZone:
    def test_cycle_zone(self, browser):
        browser.find_element(By.CSS_SELECTOR, "#box-apps-menu #app-:nth-child(6)").click()
        string = len(browser.find_elements(By.XPATH, "//*[@class='row']"))
        for i in range(string):
            countries = browser.find_elements(By.XPATH, "//*[@class='row']/td[3]/a")[i]
            countries.click()
            zones = browser.find_elements(By.XPATH, "//td[3]/select/option[@selected='selected']")
            for zone in zones:
                country_list = []
                zone_text = zone.text
                country_list.append(zone_text)
                assert country_list == sorted(country_list), "Геозоны отсортированы не по алфавиту"
            cancel = browser.find_element(By.CSS_SELECTOR, "button[name='cancel']")
            cancel.click()








