from pages.main_page import MainPage
from locators import MainPageLocators
from urls import Urls
import allure

class TestConstructor:

    @allure.title('Переход к разделу "Конструктор"')
    def test_go_to_constructor_success(self, driver):

        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.click_constructor_button()

        assert main_page.get_current_url() == Urls.main_page

    @allure.title('Переход к разделу "Лента заказов"')
    def test_jump_to_orders_feed_success(self, driver):

        main_page = MainPage(driver)
        main_page.click_orders_feed_button()

        assert main_page.get_current_url() == Urls.orders_feed

    @allure.title('Открытие окна с информацией об ингредиенте')
    def test_open_ingredient_details_success(self, driver):

        main_page = MainPage(driver)
        main_page.open_ingredient_details()

        assert main_page.get_element(MainPageLocators.POPUP_WINDOW).is_displayed

    @allure.title('Закрытие окна с информацией об ингредиенте')
    def test_close_ingredient_details_success(self, driver):

        main_page = MainPage(driver)
        main_page.open_ingredient_details()
        main_page.close_popup_window()

        assert main_page.get_elements(MainPageLocators.POPUP_WINDOW) == []

    @allure.title('Каунтер ингредиента увеличивается при добавлении этого ингредиента в заказ')
    def test_ingredients_added_to_counter(self, driver):

        main_page = MainPage(driver)
        main_page.add_ingredient_to_order()

        assert main_page.get_ingredient_count() == "2"

    @allure.title('Авторизованный пользователь может оформить заказ')
    def test_authorized_user_can_place_order(self, driver, login):

        main_page = MainPage(driver)
        main_page.wait_for_element(MainPageLocators.FLUORESCENT_BUN)
        main_page.add_ingredient_to_order()
        main_page.click_order_button()

        assert main_page.get_element(MainPageLocators.POPUP_WINDOW).is_displayed