from selenium.webdriver.common.by import By


class TestCampaignsDuck:
    def test_title(self, browser):
        browser.find_element(By.CSS_SELECTOR, "a .fa.fa-chevron-circle-left").click()
        name = browser.find_element(By.CSS_SELECTOR, "#box-campaigns .name").text
        browser.find_element(By.CSS_SELECTOR, "#box-campaigns a.link").click()
        name1 = browser.find_element(By.CSS_SELECTOR, "h1.title").text
        assert name == name1, "Названия на страницах не совпадают"

    def test_regular_price(self, browser):
        browser.find_element(By.CSS_SELECTOR, "a .fa.fa-chevron-circle-left").click()
        regular_price = browser.find_element(By.CSS_SELECTOR, "#box-campaigns .regular-price").text
        browser.find_element(By.CSS_SELECTOR, "#box-campaigns a.link").click()
        regular_price1 = browser.find_element(By.CSS_SELECTOR, "s.regular-price").text
        assert regular_price == regular_price1, "Цены без скидки на страницах не совпадают"

    def test_campaign_price(self, browser):
        browser.find_element(By.CSS_SELECTOR, "a .fa.fa-chevron-circle-left").click()
        sale_price = browser.find_element(By.CSS_SELECTOR, "#box-campaigns .campaign-price").text
        browser.find_element(By.CSS_SELECTOR, "#box-campaigns a.link").click()
        sale_price1 = browser.find_element(By.CSS_SELECTOR, "strong.campaign-price").text
        assert sale_price == sale_price1, "Цена со скидкой на страницах не совпадает"

    def test_regular_price_grey(self, browser):
        browser.find_element(By.CSS_SELECTOR, "a .fa.fa-chevron-circle-left").click()
        regular_price = browser.find_element(By.CSS_SELECTOR, "#box-campaigns .regular-price")
        regular_price_attr = regular_price.get_attribute("tagName")
        regular_price_color = regular_price.value_of_css_property("color")
        if regular_price_color.count("119") == 3:
            print("цвет цены на странице магазина - серый")
        else:
            print("цвет другой")
        # здесь переходим на страницу товара
        browser.find_element(By.CSS_SELECTOR, "#box-campaigns a.link").click()

        regular_price1 = browser.find_element(By.CSS_SELECTOR, "s.regular-price")
        regular_price_attr1 = regular_price1.get_attribute("tagName")
        regular_price_color1 = regular_price1.value_of_css_property("color")
        if regular_price_color1.count("102") == 3:
            print("цвет цены на странице товара - серый")
        else:
            print("цвет другой")
        assert regular_price_attr == regular_price_attr1, "Текст цены не перечеркнут"

    def test_sale_price_red_and_fat(self, browser):
        browser.find_element(By.CSS_SELECTOR, "a .fa.fa-chevron-circle-left").click()
        sale_price = browser.find_element(By.CSS_SELECTOR, "#box-campaigns .campaign-price")
        sale_price_attr_fat = sale_price.get_attribute("tagName")
        sale_price_color = sale_price.value_of_css_property("color")
        if sale_price_color.count("0") == 2:
            print("цвет цены на странице магазина красный")
        else:
            print("цвет другой")
        # здесь переходим на страницу товара
        browser.find_element(By.CSS_SELECTOR, "#box-campaigns a.link").click()

        sale_price1 = browser.find_element(By.CSS_SELECTOR, "strong.campaign-price")
        sale_price_attr_fat1 = sale_price1.get_attribute("tagName")
        sale_price_color1 = sale_price1.value_of_css_property("color")
        if sale_price_color1.count("0") == 2:
            print("цвет цены на странице товара - красный")
        else:
            print("цвет другой")
        assert sale_price_attr_fat == sale_price_attr_fat1, "Текст цены жирный"

    def test_sale_price_large(self, browser):
        browser.find_element(By.CSS_SELECTOR, "a .fa.fa-chevron-circle-left").click()
        regular_price = browser.find_element(By.CSS_SELECTOR, "#box-campaigns .regular-price")
        regular_price_size = regular_price.value_of_css_property("font-size").replace("px", "")
        regular_price_size_int = float(regular_price_size)
        sale_price = browser.find_element(By.CSS_SELECTOR, "#box-campaigns .campaign-price")
        sale_price_size = sale_price.value_of_css_property("font-size").replace("px", "")
        sale_price_size_int = float(sale_price_size)
        assert regular_price_size_int < sale_price_size_int, "Текст скидки не больше обычного текста цены"

        browser.find_element(By.CSS_SELECTOR, "#box-campaigns a.link").click()

        regular_price1 = browser.find_element(By.CSS_SELECTOR, "s.regular-price")
        regular_price_size1 = regular_price1.value_of_css_property("font-size").replace("px", "")
        regular_price_size_int1 = float(regular_price_size1)
        sale_price1 = browser.find_element(By.CSS_SELECTOR, "strong.campaign-price")
        sale_price_size1 = sale_price1.value_of_css_property("font-size").replace("px", "")
        sale_price_size_int1 = float(sale_price_size1)
        assert regular_price_size_int1 < sale_price_size_int1, "Текст скидки не больше обычного текста цены"
