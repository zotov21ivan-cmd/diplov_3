from selenium.webdriver.common.by import By

class OrderFeedPageLocators:

# Локаторы Ленты Заказов
# Найди текст "Лента Заказов"   
    ORDERS_PAGE_TEXT = (By.XPATH, ".//h1[text()='Лента заказов']")
# Счетчик заказов Выполнено за все время
    ORDERS_COUNT_ALL = (By.CSS_SELECTOR, "div[class='undefined mb-15'] p[class='OrderFeed_number__2MbrQ text text_type_digits-large']")
# Счетчик заказов Выполнено за сегодня
    ORDERS_COUNT_DAY = (By.CSS_SELECTOR, "div:nth-child(3) p:nth-child(2)")
# Счетчик заказов В работе
    ORDER_ID_WORK = (By.CSS_SELECTOR, "ul[class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi'] li[class='text text_type_digits-default mb-2']")