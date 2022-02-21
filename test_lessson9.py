from selenium.webdriver.common.by import By
canada_list = []
america_list = []


class TestCountryZone:
    def test_geozone_canada(self, browser):
        browser.find_element(By.CSS_SELECTOR, "#box-apps-menu #app-:nth-child(6)").click()
        countries = browser.find_elements(By.XPATH, "//*[@class='row']/td[3]/a")
        countries[0].click()
        zones = browser.find_elements(By.XPATH, "//td[3]/select/option[@selected='selected']")
        for zone in zones:
            zone_text = zone.text
            canada_list.append(zone_text)

        assert canada_list == sorted(canada_list), "Геозоны отсортированы не по алфавиту"

    def test_geozone_america(self, browser):
        browser.find_element(By.CSS_SELECTOR, "#box-apps-menu #app-:nth-child(6)").click()
        countries = browser.find_elements(By.XPATH, "//*[@class='row']/td[3]/a")
        countries[1].click()
        zones = browser.find_elements(By.XPATH, "//td[3]/select/option[@selected='selected']")
        for zone in zones:
            zone_text = zone.text
            america_list.append(zone_text)

        assert america_list == sorted(america_list), "Геозоны отсортированы не по алфавиту"
