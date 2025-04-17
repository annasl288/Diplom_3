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