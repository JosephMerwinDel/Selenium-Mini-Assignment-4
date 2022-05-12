import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver


class BaseClassPage(object):
    def __init__(self, driver, base_url='https://weathershopper.pythonanywhere.com/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_element_by_xpath(self, *value):
        return self.driver.find_element(By.XPATH, value=value)

    def find_elements_by_xpath(self, *locator):
        print(locator)
        webel = self.driver.find_elements(by=By.XPATH, value="//p[@class = 'font-weight-bold top-space-10']")
        print(webel)
        return self.driver.find_elements(*locator)

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(*locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()

    def element_clickable(self, *locator):
        try:
            return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(*locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()
