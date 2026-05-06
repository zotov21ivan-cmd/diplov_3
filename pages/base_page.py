import random

from asyncio.windows_events import NULL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.action = ActionChains(driver)

    def open(self, url):
        self.driver.get(url)

    def find_(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def find(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find(locator).click()

    def click_button(self, locator):
        self.click(locator)

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text
        
    def get_visibility(self, locator):
        return self.find(locator).is_displayed()
    
    def get_enabled(self, locator):
        return self.find(locator).is_enabled()
    
    def drag_n_drop(self, locator_source, locator_target):
        source = self.find(locator_source)
        target = self.find(locator_target)
        self.action.drag_and_drop(source, target).perform()
    