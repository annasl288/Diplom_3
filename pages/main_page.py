from pages.base_page import BasePage
from locators import MainPageLocators
from urls import Urls
from seletools.actions import drag_and_drop
import allure

class MainPage(BasePage):

    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.go_to_url(Urls.main_page)

    @allure.step('Нажать на кнопку "Конструктор"')
    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Нажать на кнопку "Лента заказов"')
    def click_orders_feed_button(self):
        self.click_element(MainPageLocators.FEED_BUTTON)

    @allure.step('Нажать на кнопку "Личный кабинет"')
    def click_account_button(self):
        self.click_element(MainPageLocators.ACCOUNT_BUTTON)

    @allure.step('Нажать на ингредиент')
    def open_ingredient_details(self):
        self.click_element(MainPageLocators.FLUORESCENT_BUN)

    @allure.step('Нажать на крестик во всплывающем окне')
    def close_popup_window(self):
        self.click_element(MainPageLocators.POPUP_CLOSE_BUTTON)

    @allure.step('Добавить ингредиент в заказ')
    def add_ingredient_to_order(self):
        source = self.get_element(MainPageLocators.FLUORESCENT_BUN)
        target = self.get_element(MainPageLocators.BASKET)
        drag_and_drop(self.driver, source, target)

    @allure.step('Получить количество ингредиента')
    def get_ingredient_count(self):
        count = self.get_element(MainPageLocators.INGREDIENT_COUNTER).text
        return count

    @allure.step('Нажать на кнопку "Оформить заказ"')
    def click_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        number = self.get_element(MainPageLocators.ORDER_NUMBER).text
        return number