from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from curl import BASE_URL


class MainPage(BasePage):

    def open_main_page(self):
        self.open(BASE_URL)

    def get_status_section(self, locator):
        return self.get_text(locator)
    
    def get_visibility_section(self, locator):
        return self.get_visibility(locator)

    def get_status_login(self):
        return self.get_text(MainPageLocators.MAKE_ORDER_BUTTON)