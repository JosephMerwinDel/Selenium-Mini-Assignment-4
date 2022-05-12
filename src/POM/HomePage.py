import time

from selenium.webdriver.common.keys import Keys
from src.POM.BaseClass import BaseClassPage
'''from pages.login_page import LoginPage
from pages.signup_page import SignUpBasePage'''
from src.Utilities.locators import *

class HomePage(BaseClassPage):

    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)

    def check_page_loaded(self):
        print(self.find_element(*self.get_title()))
        return True if (self.find_element(*self.get_title())) == '' else False

    def select_options_based_on_temperature(self):
        temperature = self.find_element(*self.locator.TEMPERATURE).text
        numbers = ''
        for word in temperature.split():
            if word.isdigit():
                numbers += word

        if int(numbers) >= 34:
            ele = self.element_clickable(self.locator.BUY_SUNSCREEN_BUTTON)
            ele.click()
        elif int(numbers) <= 19:
            ele = self.element_clickable(self.locator.BUY_MOISTURIZERS_BUTTON)
            ele.click()
