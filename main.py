'''from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com")

driver.find_element(by=By.XPATH, value="//input[@class = 'gLFyf gsfi']").send_keys("outlook")
driver.implicitly_wait(0.8)
driver.find_element(by=By.XPATH, value="//div[@class = 'mkHrUc' ]//span[text() = 'outlook']//b[text()=' 365']").click()'''


