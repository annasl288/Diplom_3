from pages.base_page import BasePage
from locators import AccountPageLocators
import allure

class AccountPage(BasePage):

    @allure.step('Перейти в раздел "История заказов"')
    def go_to_order_history(self):
        self.click_element(AccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Нажать на кнопку "Выход"')
    def click_sign_out_button(self):
        self.click_element(AccountPageLocators.SIGN_OUT_BUTTON)