from pages.base_page import BasePage
from locators import LoginPageLocators
from urls import Urls
# from data import ExistingUser
import allure

class LoginPage(BasePage):

    @allure.step('Открыть страницу входа в аккаунт')
    def open_login_page(self):
        self.go_to_url(Urls.login_page)

    @allure.step('Нажать на кнопку "Восстановить пароль"')
    def click_recover_password(self):
        self.click_element(LoginPageLocators.RECOVER_PASSWORD)

    # def enter_email(self):
    #     self.get_element(LoginPageLocators.EMAIL_INPUT).send_keys(ExistingUser.email)
    #
    # def enter_password(self):
    #     self.get_element(LoginPageLocators.PASSWORD_INPUT).send_keys(ExistingUser.password)
    #
    # def click_login_button(self):
    #     self.click_element(LoginPageLocators.LOGIN_BUTTON)
    #
    # @allure.step('Авторизоваться существующим пользователем')
    # def login(self):
    #     self.enter_email()
    #     self.enter_password()
    #     self.click_login_button()