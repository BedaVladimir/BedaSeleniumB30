from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class TestSticker:
    def test_find_sticker_new(self, driver):
        ducks = driver.find_elements(By.XPATH, ".//ul[@class='listing-wrapper products']//li")
        all_ducks = len(ducks)
        all_sticker = 0
        for duck in ducks:
            sticker = duck.find_elements(By.XPATH, "//*[@class='product column shadow hover-light']//div/div")
            all_sticker = len(sticker)
        assert all_ducks == all_sticker, "Стикеры есть не у каждого товара/ " \
                                         "У одного товара стикеров больше чем один"