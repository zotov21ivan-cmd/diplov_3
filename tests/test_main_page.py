import pytest
import allure
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.orders_page import OrdersPage
from locators.main_page_locators import MainPageLocators
from locators.account_page_locators import AccountPageLocators
from data_pak import *

@allure.feature('Основной функционал')
@allure.story('Тесты навигации и взаимодействия с элементами')
class TestMainPage:
    # Тест успешного перехода по клику на Конструктор
    @allure.title('Успешный переход из личного кабинета в Конструктор')
    @allure.description('Проверяет, что пользователь может перейти в Конструктор из личного кабинета через кнопку или логотип')
    @pytest.mark.parametrize('buttons',[AccountPageLocators.CONSTRUCTOR_BUTTON,AccountPageLocators.STELLAR_LOGO_BUTTON])
    def test_success_transfer_from_personal_account_to_constructor(self, driver, buttons):
        with allure.step('Открытие главной страницы'):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step('Переход в Личный кабинет и авторизация'):
            main_page.click_button(MainPageLocators.LOGIN_BUTTON_MAIN)
            account_page = AccountPage(driver)
            account_page.open_login_page()
            account_page.login(right_login, right_pass)

        with allure.step('Переход в Конструктор через кнопку/логотип'):
            account_page.click_button(buttons)

        with allure.step('Проверка наличия кнопки "Оформить заказ"'):
            message = main_page.get_status_login()
            assert 'Оформить заказ' in message

    # Тест успешного перехода на раздел «Лента заказов» для незарегистрированного пользователя
    @allure.title('Переход на "Лента заказов" для незарегистрированного пользователя')
    @allure.description('Проверяет, что незарегистрированный пользователь может перейти на страницу "Лента заказов"')
    def test_success_transfer_from_main_page_to_orders_feed(self, driver):
        with allure.step('Открытие главной страницы'):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step('Переход на раздел "Лента заказов"'):
            main_page.click_button(MainPageLocators.ORDERS_LIST_BUTTON)

        with allure.step('Проверка заголовка "Лента заказов"'):
            order_page = OrdersPage(driver)
            message = order_page.get_status_orders()
            assert 'Лента заказов' in message

    # Тест успешного перехода на раздел «Лента заказов» для зарегистрированного пользователя
    @allure.title('Переход на "Лента заказов" для зарегистрированного пользователя')
    @allure.description('Проверяет, что авторизованный пользователь может перейти на страницу "Лента заказов"')
    def test_success_transfer_login_user_to_orders_feed(self, driver):
        with allure.step('Открытие главной страницы'):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step('Переход в Личный кабинет и авторизация'):
            main_page.click_button(MainPageLocators.LOGIN_BUTTON_MAIN)
            account_page = AccountPage(driver)
            account_page.login(right_login, right_pass)

        with allure.step('Переход на раздел "Лента заказов"'):
            main_page.click_button(MainPageLocators.ORDERS_LIST_BUTTON)

        with allure.step('Проверка заголовка "Лента заказов"'):
            order_page = OrdersPage(driver)
            message = order_page.get_status_orders()
            assert 'Лента заказов' in message

    # Тест успешного перехода из Личного кабинета на раздел «Лента заказов»
    @allure.title('Переход из Личного кабинета на "Лента заказов"')
    @allure.description('Проверяет возможность перехода на страницу "Лента заказов" непосредственно из личного кабинета')
    def test_success_transfer_from_account_page_to_orders_feed(self, driver):
        with allure.step('Открытие страницы авторизации'):
            account_page = AccountPage(driver)
            account_page.open_login_page()

        with allure.step('Переход на раздел "Лента заказов" из личного кабинета'):
            account_page.click_button(AccountPageLocators.ORDERS_LIST_BUTTON)

        with allure.step('Проверка заголовка "Лента заказов"'):
            order_page = OrdersPage(driver)
            message = order_page.get_status_orders()
            assert 'Лента заказов' in message

    # Тест успешного просмотра Всплывающего окна с деталями ингредиента
    @allure.title('Просмотр деталей ингредиента во всплывающем окне')
    @allure.description('Проверяет открытие всплывающего окна с информацией об ингредиенте')
    def test_success_select_ingredient_open(self, driver):
        with allure.step('Авторизация пользователя'):
            main_page = MainPage(driver)
            account_page = AccountPage(driver)
            account_page.open_login_page()
            account_page.login(right_login, right_pass)

        with allure.step('Клик по ингредиенту для открытия всплывающего окна'):
            main_page.click_button(MainPageLocators.INGREDIENT_ITEMS)

        with allure.step('Проверка видимости заголовка во всплывающем окне'):
            main_page.get_visibility(MainPageLocators.WINDOW_TEXT_INGREDIENT)
            present = main_page.get_enabled(MainPageLocators.MAIN_BURGER_SECTION)
            assert present

    @allure.description('Проверяет закрытие всплывающего окна с информацией об ингредиенте')
    def test_success_select_ingredient_close(self, driver):
        with allure.step('Авторизация пользователя'):
            main_page = MainPage(driver)
            account_page = AccountPage(driver)
            account_page.open_login_page()
            account_page.login(right_login, right_pass)

        with allure.step('Клик по ингредиенту для открытия всплывающего окна'):
            main_page.click_button(MainPageLocators.INGREDIENT_ITEMS)

        with allure.step('Ожидание видимости заголовка во всплывающем окне'):
            main_page.get_visibility(MainPageLocators.WINDOW_TEXT_INGREDIENT)

        with allure.step('Закрытие всплывающего окна кликом по крестику'):
            main_page.click_button(MainPageLocators.WINDOW_CROSS_INGREDIENT)

        with allure.step('Проверка доступности секции "Соберите бургер"'):
            present = main_page.get_enabled(MainPageLocators.MAIN_BURGER_SECTION)
            assert present

    @allure.title('Добавление ингредиента и проверка счётчика')
    @allure.description('Проверяет увеличение счётчика ингредиентов при добавлении нового ингредиента в заказ')
    def test_success_add_ingredient_count(self, driver):
        with allure.step('Авторизация пользователя'):
            main_page = MainPage(driver)
            account_page = AccountPage(driver)
            account_page.open_login_page()
            account_page.login(right_login, right_pass)

        with allure.step('Перетаскивание ингредиента в область заказа'):
            main_page.drag_n_drop(MainPageLocators.INGREDIENT_ITEMS, MainPageLocators.TOP_ORDER_POS)

        with allure.step('Проверка значения счётчика ингредиентов'):
            count = main_page.get_text(MainPageLocators.COUNTER_BRED)
            assert '2' == count