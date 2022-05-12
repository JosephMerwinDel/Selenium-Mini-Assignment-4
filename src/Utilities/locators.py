from selenium.webdriver.common.by import By


class MainPageLocators(object):
    TEMPERATURE = (By.ID, 'temperature')
    BUY_MOISTURIZERS_BUTTON = (By.XPATH, "//button[text() = 'Buy moisturizers']")
    BUY_SUNSCREEN_BUTTON = (By.XPATH, "//button[text() = 'Buy sunscreens']")


class MoisturizerPageLocators(object):
    GET_ITEM_NAMES = (By.XPATH, "//p[@class = 'font-weight-bold top-space-10']")
    GET_ITEM_Price_1 = "//p[text() = '"
    GET_ITEM_Price_2 = "']//following-sibling::p[contains(text(), 'Price:')]"
    ADD_BUTTON = "//following-sibling::button[text() = 'Add']"

class SunscreenPageLocators(object):
    pass