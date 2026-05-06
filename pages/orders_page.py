from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from curl import ORDERS_URL


class OrdersPage(BasePage):

    def open_orders_page(self):
        self.open(ORDERS_URL)

    def get_status_orders(self):
        return self.get_text(OrderFeedPageLocators.ORDERS_PAGE_TEXT)
    def is_order_displayed_in_work(self, order_id):
        """Ожидает появления номера заказа в разделе 'В работе'"""
        expected_id = str(order_id)
        # Он должен вернуть True, если текст совпал, или False по таймауту
        return self.wait_for_text_in_element(
            OrderFeedPageLocators.ORDER_ID_WORK, 
            expected_id
        )