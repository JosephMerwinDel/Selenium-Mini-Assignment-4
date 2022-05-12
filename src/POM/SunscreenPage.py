import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.POM.BaseClass import BaseClassPage
from src.Utilities.locators import MainPageLocators, SunscreenPageLocators
from src.Utilities.locators import MoisturizerPageLocators

class SunscreenPage(BaseClassPage):

    def __init__(self, driver):
        self.locator = SunscreenPageLocators
        super().__init__(driver)

    def add_to_cart(self):
        webelements = self.find_elements_by_xpath(self.locator.GET_ITEM_NAMES)
        #webelements = driver.find_elements(by=By.XPATH, value="//p[@class = 'font-weight-bold top-space-10']")
        print(webelements)
        aloeprice, almondprice = [0, ''], [0, '']
        for elements in webelements:
            print(elements)
            if "aloe" in elements.text.lower():
                add_item = self.locator.GET_ITEM_Price_1 + elements.text + self.locator.GET_ITEM_Price_2
                temp_price = self.find_element_by_xpath(add_item)
                print(temp_price)
                if (int(temp_price[-3:]) > aloeprice[0]):
                    aloeprice[0] = int(temp_price[-3:])
                    aloeprice[1] = add_item + self.locator.ADD_BUTTON
            elif "almond" in elements.text.lower():
                add_item = self.locator.GET_ITEM_Price_1 + elements.text + self.locator.GET_ITEM_Price_2
                temp_price = self.find_element_by_xpath(add_item)

                print(temp_price)
                if (int(temp_price[-3:]) > almondprice[0]):
                    almondprice[0] = int(temp_price[-3:])
                    almondprice[1] = add_item + self.locator.ADD_BUTTON
        print(almondprice, aloeprice)

        self.find_element_by_xpath(
                            almondprice[1]).click()
        self.find_element_by_xpath(
                            aloeprice[1]).click()
