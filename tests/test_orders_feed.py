from pages.main_page import MainPage
from pages.feed_page import FeedPage
from locators import FeedPageLocators, MainPageLocators
import allure

class TestOrdersFeed:

    @allure.title('Открытие окна с информацией о заказе')
    def test_open_order_details_success(self, driver):

        feed_page = FeedPage(driver)
        feed_page.open_orders_feed()
        feed_page.wait_for_element(FeedPageLocators.FIRST_ORDER)
        feed_page.open_order_details()

        assert feed_page.get_element(FeedPageLocators.POPUP_WINDOW).is_displayed

    @allure.title('Заказ пользователя отображается в ленте заказов')
    def test_user_orders_displayed_in_feed(self, driver, login):

        main_page = MainPage(driver)
        main_page.wait_for_element(MainPageLocators.FLUORESCENT_BUN)
        main_page.add_ingredient_to_order()
        main_page.click_order_button()
        order_number = main_page.get_order_number()
        main_page.close_popup_window()
        main_page.click_orders_feed_button()

        feed_page = FeedPage(driver)
        feed_page.wait_for_element(FeedPageLocators.ORDERS_LIST)
        orders_list = feed_page.get_orders_list()

        assert order_number in orders_list

    @allure.title('Счётчик заказов, выполненных за всё время, увеличивается после заказа')
    def test_total_orders_counter_goes_up_after_order(self, driver, login):

        main_page = MainPage(driver)
        main_page.click_orders_feed_button()

        feed_page = FeedPage(driver)
        feed_page.wait_for_element(FeedPageLocators.TOTAL_ORDERS_COUNTER)
        total_orders_before = feed_page.get_total_orders_count()

        main_page.open_main_page()
        main_page.wait_for_element(MainPageLocators.FLUORESCENT_BUN)
        main_page.add_ingredient_to_order()
        main_page.click_order_button()

        feed_page.open_orders_feed()
        total_orders_after = feed_page.get_total_orders_count()

        assert total_orders_after > total_orders_before

    @allure.title('Счётчик заказов, выполненных сегодня, увеличивается после заказа')
    def test_today_orders_counter_goes_up_after_order(self, driver, login):

        main_page = MainPage(driver)
        main_page.click_orders_feed_button()

        feed_page = FeedPage(driver)
        feed_page.wait_for_element(FeedPageLocators.TODAY_ORDERS_COUNTER)
        today_orders_before = feed_page.get_today_orders_count()

        main_page.open_main_page()
        main_page.wait_for_element(MainPageLocators.FLUORESCENT_BUN)
        main_page.add_ingredient_to_order()
        main_page.click_order_button()

        feed_page.open_orders_feed()
        feed_page.wait_for_element(FeedPageLocators.TODAY_ORDERS_COUNTER)
        today_orders_after = feed_page.get_today_orders_count()

        assert today_orders_after > today_orders_before

    @allure.title('Номер нового заказа добавляется в раздел "В работе" ленты заказов')
    def test_new_order_number_in_in_progress_section(self, driver, login):

        main_page = MainPage(driver)
        main_page.wait_for_element(MainPageLocators.FLUORESCENT_BUN)
        main_page.add_ingredient_to_order()
        main_page.click_order_button()
        order_number = main_page.get_order_number()
        main_page.close_popup_window()
        main_page.click_orders_feed_button()

        feed_page = FeedPage(driver)
        feed_page.wait_for_element(FeedPageLocators.ORDERS_IN_PROGRESS)
        feed_page.wait_for_text_in_element(FeedPageLocators.ORDERS_IN_PROGRESS, order_number)
        orders_in_progress = feed_page.get_orders_in_progress_list()

        assert order_number in orders_in_progress