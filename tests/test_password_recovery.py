from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage
from locators import PasswordRecoveryLocators
from urls import Urls
import allure

class TestPasswordRecovery:

    @allure.title('Переход к странице восстановления пароля')
    def test_go_to_password_recovery_page_success(self, driver):

        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.click_recover_password()

        assert login_page.get_current_url() == Urls.password_recovery

    @allure.title('Переход к странице смены пароля')
    def test_go_to_password_reset_page_success(self, driver):

        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.open_password_recovery_page()
        password_recovery_page.enter_email()
        password_recovery_page.click_recover_password()
        password_recovery_page.wait_for_element(PasswordRecoveryLocators.SAVE_BUTTON)

        assert password_recovery_page.get_current_url() == Urls.password_reset

    @allure.title('Поле ввода пароля подсвечивается при нажатии на кнопку "Показать пароль"')
    def test_password_field_is_in_focus_after_show_password_button_click(self, driver):

        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.open_password_recovery_page()
        password_recovery_page.enter_email()
        password_recovery_page.click_recover_password()
        password_recovery_page.wait_for_element(PasswordRecoveryLocators.SAVE_BUTTON)
        password_recovery_page.click_show_password_button()

        assert password_recovery_page.get_element(PasswordRecoveryLocators.PASSWORD_FIELD_IN_FOCUS).is_displayed