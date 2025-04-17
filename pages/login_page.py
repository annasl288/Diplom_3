from pages.base_page import BasePage
from locators import LoginPageLocators
from urls import Urls
import allure

class LoginPage(BasePage):

    @allure.step('Открыть страницу входа в аккаунт')
    def open_login_page(self):
        self.go_to_url(Urls.login_page)

    @allure.step('Нажать на кнопку "Восстановить пароль"')
    def click_recover_password(self):
        self.click_element(LoginPageLocators.RECOVER_PASSWORD)

    @allure.step('Ввести email')
    def enter_email(self, email):
        self.get_element(LoginPageLocators.EMAIL_INPUT).send_keys(email)

    @allure.step('Ввести пароль')
    def enter_password(self, password):
        self.get_element(LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    @allure.step('Нажать на кнопку "Войти"')
    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)