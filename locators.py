from selenium.webdriver.common.by import By

class AccountPageLocators:

    ORDER_HISTORY_BUTTON = (By.XPATH, ".//a[@href = '/account/order-history']")  # Кнопка "История заказов"
    PREVIOUS_ORDERS = (By.XPATH, ".//div[contains(@class, 'OrderHistory_orderHistory')]")  # История заказов
    SIGN_OUT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']")  # Кнопка "Выход"

class FeedPageLocators:

    FIRST_ORDER = (By.CSS_SELECTOR, ".OrderHistory_listItem__2x95r:nth-of-type(1)") # Первый заказ в ленте
    ORDERS_LIST = (By.XPATH, ".//p[@class='text text_type_digits-default']") # Список заказов
    POPUP_WINDOW = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]")  # Всплывающее окно
    TOTAL_ORDERS_COUNTER = (By.XPATH, "(.//p[@class= 'OrderFeed_number__2MbrQ text text_type_digits-large'])[1]") # Счётчик заказов за всё время
    TODAY_ORDERS_COUNTER = (By.XPATH, "(.//p[@class= 'OrderFeed_number__2MbrQ text text_type_digits-large'])[2]") # Счётчик заказов за сегодня
    ORDERS_IN_PROGRESS = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]") # Список заказов в работе
    ALL_ORDERS_READY = (By.XPATH, ".//li[contains(@class, 'text text_type_main-small')]") # Плейсхолдер "Все текущие заказы готовы!"

class LoginPageLocators:

    HEADER = (By.XPATH, ".//h2[text() = 'Вход']") # Заголовок "Вход"
    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']") # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Пароль']") # Поле ввода пароля
    LOGIN_BUTTON = (By.XPATH, ".//button[text() = 'Войти']") # Кнопка "Войти"
    RECOVER_PASSWORD = (By.XPATH, ".//a[@href = '/forgot-password']") # Кнопка "Восстановить пароль"

class MainPageLocators:

    LOGIN_BUTTON = (By.XPATH, ".//button[text() = 'Войти в аккаунт']") # Кнопка "Войти в аккаунт"
    ACCOUNT_BUTTON = (By.XPATH, ".//p[text() = 'Личный Кабинет']") # Кнопка "Личный кабинет"
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text() = 'Конструктор']")  # Кнопка "Конструктор"
    FEED_BUTTON = (By.XPATH, ".//p[text() = 'Лента Заказов']") # Кнопка "Лента заказов"
    FLUORESCENT_BUN = (By.XPATH, ".//a[@href = '/ingredient/61c0c5a71d1f82001bdaaa6d']") # Флюоресцентная булка
    INGREDIENT_COUNTER = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]") # Счётчик ингредиентов
    BASKET = (By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket__list')]") # Корзина
    ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']") # Кнопка "Оформить заказ"
    POPUP_WINDOW = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]") # Всплывающее окно
    ORDER_NUMBER = (By.XPATH, ".//h2[contains(@class, 'text_type_digits-large')]") # Номер заказа
    POPUP_CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]") # Кнопка закрытия всплывающего окна
    OVERLAY = (By.CLASS_NAME, "Modal_modal__loading__3534A") # Оверлей

class PasswordRecoveryLocators:

    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']") # Поле ввода email
    RECOVER_BUTTON = (By.XPATH, ".//button[text() = 'Восстановить']") # Кнопка "Восстановить"
    SHOW_PASSWORD_BUTTON = (By.XPATH, ".//div[contains(@class, 'input__icon-action')]") # Кнопка "Показать пароль"
    PASSWORD_FIELD_IN_FOCUS = (By.XPATH, ".//div[contains(@class, 'input_status_active')]") # Подсвеченное поле ввода пароля
    SAVE_BUTTON = (By.XPATH, ".//button[text() = 'Сохранить']") # Кнопка "Сохранить"