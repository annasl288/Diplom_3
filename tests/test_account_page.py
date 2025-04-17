from pages.account_page import AccountPage
from pages.main_page import MainPage
from locators import AccountPageLocators, LoginPageLocators
from urls import Urls
import allure
class TestAccountPage:

    @allure.title('Переход в личный кабинет по клику на кнопку "Личный кабинет"')
    def test_go_to_account_page_by_account_button_click_success(self, driver, login):

        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.wait_for_url(Urls.account_page)

        assert main_page.get_current_url() == Urls.account_page

    @allure.title('Переход к истории заказов')
    def test_go_to_order_history_success(self, driver, login):

        main_page = MainPage(driver)
        main_page.click_account_button()

        account_page = AccountPage(driver)
        account_page.wait_for_element(AccountPageLocators.ORDER_HISTORY_BUTTON)
        account_page.go_to_order_history()
        account_page.wait_for_element(AccountPageLocators.PREVIOUS_ORDERS)

        assert account_page.get_current_url() == Urls.order_history

    @allure.title('Выход из аккаунта')
    def test_sign_out_success(self, driver, login):

        main_page = MainPage(driver)
        main_page.click_account_button()

        account_page = AccountPage(driver)
        account_page.wait_for_element(AccountPageLocators.SIGN_OUT_BUTTON)
        account_page.click_sign_out_button()
        account_page.wait_for_element(LoginPageLocators.HEADER)

        assert account_page.get_current_url() == Urls.login_page
