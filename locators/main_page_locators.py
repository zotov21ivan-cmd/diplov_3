from selenium.webdriver.common.by import By

class MainPageLocators:

# Найди кнопку "Войти в аккаунт"
    LOGIN_BUTTON_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")
# Найди кнопку "Оформить заказ"
    MAKE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
#  Локаторы переходов
#     
# Найди выбор меню "Профиль"
    PROFILE_MENU_TEXT = (By.XPATH, ".//a[text()='Профиль']")
# Найди кнопку "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
# Найди кнопку "Stellar-Burger"
    STELLAR_LOGO_BUTTON = (By.XPATH, ".//div/header/nav/div/a")
# Найди кнопку "Лента Заказов"
    ORDERS_LIST_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")

# Локаторы конструктора

# кнопка и текст раздела "Булки"
    SECTION_TEXT_BREAD = (By.XPATH, ".//div[2]/h2[1]") 
# кнопка и текст раздела "Соусы"
    SECTION_TEXT_SAUCE = (By.XPATH, ".//div[2]/h2[2]")
# кнопка и текст раздела "Начинки"
    SECTION_TEXT_TOPPING = (By.XPATH, ".//div[2]/h2[3]")
# изображение Булки
    INGREDIENT_IMG_BREAD = (By.CSS_SELECTOR, "div.BurgerIngredients_ingredients__menuContainer__Xu3Mo.ul:nth-child(2).a:nth-child(1)") 
# изображение Соуса
    INGREDIENT_IMG_SAUCE = (By.XPATH, ".//div[2]/ul[2]/a[1]")
# изображение Начинки
    INGREDIENT_IMG_TOPPING = (By.XPATH, ".//div[2]/ul[3]/a[1]")
# текст заголовка окна Детали ингредиента
    WINDOW_TEXT_INGREDIENT = (By.XPATH, ".//h2[text()='Детали ингредиента']")
# крестик в окне Детали ингредиента
    WINDOW_CROSS_INGREDIENT = (By.XPATH, "(//button[@type='button'])[1]")
# Локатор раздела для проверки успешного входа
    MAIN_BURGER_SECTION = (By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2")
# Локатор для элементов ингредиентов
    INGREDIENT_ITEMS = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
# Локатор верхней полки заказа
    TOP_ORDER_POS = (By.XPATH, "//div[@class='constructor-element constructor-element_pos_top']")
# Счетчик булки
    COUNTER_BRED = (By.CLASS_NAME, "counter_counter__num__3nue1")
# Кнопка Оформить заказ
    ORDER_MAKE_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
# Залоговок окна Идентификатор заказа    
    ORDER_ID_TEXT = (By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
# крестик в окне Идентификатор заказа
    WINDOW_CROSS_ORDER_ID = (By.XPATH, "//button[@type='button']//*[name()='svg']")
# Вне модального окна
    OUT_WINDOW_BODY = (By.TAG_NAME, "body")
# текст в модальном окне
    ORDER_SUCCESS_MESSAGE = (By.XPATH, "//p[@class='undefined text text_type_main-medium mb-15']")    
# Локаторы Ленты Заказов
# Найди текст "Лента Заказов"   
    ORDERS_PAGE_TEXT = (By.XPATH, ".//h1[text()='Лента заказов']")