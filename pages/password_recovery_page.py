from pages.base_page import BasePage
from locators import PasswordRecoveryLocators
from urls import Urls
import allure

class PasswordRecoveryPage(BasePage):

    @allure.step('Открыть страницу восстановления пароля')
    def open_password_recovery_page(self):
        self.go_to_url(Urls.password_recovery)

    @allure.step('Ввести email')
    def enter_email(self, email):
        self.get_element(PasswordRecoveryLocators.EMAIL_INPUT).send_keys(email)

    @allure.step('Нажать на кнопку "Восстановить"')
    def click_recover_password(self):
        self.click_element(PasswordRecoveryLocators.RECOVER_BUTTON)

    @allure.step('Нажать на кнопку "Показать пароль"')
    def click_show_password_button(self):
        self.click_element(PasswordRecoveryLocators.SHOW_PASSWORD_BUTTON)