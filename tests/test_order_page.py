import pytest
import allure
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.orders_page import OrdersPage
from locators.account_page_locators import AccountPageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators

from data_pak import *

@allure.feature('Раздел «Лента заказов»')
@allure.story('Тесты счётчиков и отображения заказов')
class TestOrderPageCountAlls:
    # проверка при создании нового заказа увеличения счётчика «Выполнено за всё время»
    @allure.title('Увеличение счётчика "Выполнено за всё время" при создании заказа')
    @allure.description('Проверяет, что счётчик "Выполнено за всё время" увеличивается после создания нового заказа')
    def test_success_count_all_day_up(self, driver):
        with allure.step('Авторизация пользователя'):
            account_page = AccountPage(driver)
            main_page = MainPage(driver)
            order_page = OrdersPage(driver)
            account_page.open_login_page()
            account_page.login(right_login, right_pass)

        with allure.step('Ожидание доступности секции "Соберите бургер"'):
            main_page.get_enabled(MainPageLocators.MAIN_BURGER_SECTION)

        with allure.step('Чтение начального значения счётчика "Выполнено за всё время"'):
            order_page.open_orders_page()
            count_all = order_page.get_text(OrderFeedPageLocators.ORDERS_COUNT_ALL)

        with allure.step('Создание нового заказа'):
            main_page.open_main_page()
            main_page.drag_n_drop(MainPageLocators.INGREDIENT_ITEMS, MainPageLocators.TOP_ORDER_POS)
            main_page.click_button(MainPageLocators.ORDER_MAKE_BUTTON)

        with allure.step('Ожидание и проверка увеличения счётчика "Выполнено за всё время"'):
            order_page.open_orders_page()
            count_all_new = order_page.get_text(OrderFeedPageLocators.ORDERS_COUNT_ALL)
            while int(count_all_new) <= int(count_all):
                count_all_new = order_page.get_text(OrderFeedPageLocators.ORDERS_COUNT_ALL)

        with allure.step('Подтверждение увеличения счётчика'):
            assert int(count_all_new) > int(count_all)

    # проверка при создании нового заказа увеличения счётчика «Выполнено за сегодня»
    @allure.title('Увеличение счётчика "Выполнено за сегодня" при создании заказа')
    @allure.description('Проверяет, что счётчик "Выполнено за сегодня" увеличивается после создания нового заказа')
    def test_success_count_day_up(self, driver):
        with allure.step('Авторизация пользователя'):
            account_page = AccountPage(driver)
            main_page = MainPage(driver)
            order_page = OrdersPage(driver)
            account_page.open_login_page()
            account_page.login(right_login, right_pass)

        with allure.step('Ожидание доступности секции "Соберите бургер"'):
            main_page.get_enabled(MainPageLocators.MAIN_BURGER_SECTION)

        with allure.step('Чтение начального значения счётчика "Выполнено за сегодня"'):
            order_page.open_orders_page()
            count_day = order_page.get_text(OrderFeedPageLocators.ORDERS_COUNT_DAY)

        with allure.step('Создание нового заказа'):
            main_page.open_main_page()
            main_page.drag_n_drop(MainPageLocators.INGREDIENT_ITEMS, MainPageLocators.TOP_ORDER_POS)
            main_page.click_button(MainPageLocators.ORDER_MAKE_BUTTON)

        with allure.step('Ожидание и проверка увеличения счётчика "Выполнено за сегодня"'):
            order_page.open_orders_page()
            count_day_new = order_page.get_text(OrderFeedPageLocators.ORDERS_COUNT_DAY)
            while int(count_day_new) <= int(count_day):
                count_day_new = order_page.get_text(OrderFeedPageLocators.ORDERS_COUNT_DAY)

        with allure.step('Подтверждение увеличения счётчика'):
            assert int(count_day_new) > int(count_day)

    @allure.title('Отображение нового заказа в разделе "В работе"')
    @allure.description('Проверяет, что новый заказ отображается в разделе "В работе" на странице ленты заказов')
    def test_success_count_work(self, driver):
        with allure.step('Авторизация пользователя'):
            account_page = AccountPage(driver)
            main_page = MainPage(driver)
            order_page = OrdersPage(driver)
            account_page.open_login_page()
            account_page.login(right_login, right_pass)

        with allure.step('Ожидание доступности секции "Соберите бургер"'):
            main_page.get_enabled(MainPageLocators.MAIN_BURGER_SECTION)

        with allure.step('Создание нового заказа'):
            main_page.open_main_page()
            main_page.drag_n_drop(MainPageLocators.INGREDIENT_ITEMS, MainPageLocators.TOP_ORDER_POS)
            main_page.click_button(MainPageLocators.ORDER_MAKE_BUTTON)

        with allure.step('Получение номера нового заказа из всплывающего окна'):
            order_id = main_page.get_text(MainPageLocators.ORDER_ID_TEXT)
            while order_id == '9999':
                order_id = main_page.get_text(MainPageLocators.ORDER_ID_TEXT)

        with allure.step('Закрытие всплывающего окна щелчком вне его области'):
            main_page.click_button(MainPageLocators.OUT_WINDOW_BODY)

        with allure.step('Ожидание отображения заказа в разделе "В работе"'):
            order_page.open_orders_page()
            order_id_work = order_page.get_text(OrderFeedPageLocators.ORDER_ID_WORK)
            while True:
                order_id_work = order_page.get_text(OrderFeedPageLocators.ORDER_ID_WORK)
                if int(order_id) == int(order_id_work):
                    break

        with allure.step('Подтверждение отображения заказа в разделе "В работе"'):
            assert int(order_id_work) == int(order_id)