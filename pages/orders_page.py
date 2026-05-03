from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from curl import ORDERS_URL


class OrdersPage(BasePage):

    def open_orders_page(self):
        self.open(ORDERS_URL)

    def get_status_orders(self):
        return self.get_text(OrderFeedPageLocators.ORDERS_PAGE_TEXT)