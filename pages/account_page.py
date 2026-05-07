from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from curl import LOGIN_URL, REGISTER_URL


class AccountPage(BasePage):

    def open_login_page(self):
        self.open(LOGIN_URL)

    def open_register_page(self):
        self.open(REGISTER_URL)

    def login(self, username, password):
        self.type(AccountPageLocators.LOG_USERNAME_INPUT, username)
        self.type(AccountPageLocators.LOG_PASSWORD_INPUT, password)
        self.click(AccountPageLocators.LOGIN_BUTTON)

    def register(self, name, username, password):
        self.type(AccountPageLocators.REG_NAME_INPUT, name)
        self.type(AccountPageLocators.REG_USERNAME_INPUT, username)
        self.type(AccountPageLocators.REG_PASSWORD_INPUT, password)
        self.click(AccountPageLocators.REG_REGISTRATION_BUTTON)

    def get_status_logout(self):
        return self.get_text(AccountPageLocators.LOGIN_PAGE_TEXT)
    
    def get_status_account(self):
        return self.get_text(AccountPageLocators.PROFILE_MENU_TEXT)
    
    def get_status_error(self):
        return self.get_text(AccountPageLocators.ERROR_INVALID_PASSWORD)
    
    def logout(self):
        self.click(AccountPageLocators.PERSONAL_ACCAUNT_BUTTON)
        self.click(AccountPageLocators.LOGOUT_BUTTON)