from pages.base_page import BasePage
from locators import FeedPageLocators
from urls import Urls
from data import OrderData
import allure

class FeedPage(BasePage):

    @allure.step('Открыть ленту заказов')
    def open_orders_feed(self):
        self.go_to_url(Urls.orders_feed)

    @allure.step('Нажать на первый заказ в списке')
    def open_order_details(self):
        self.click_element(FeedPageLocators.FIRST_ORDER)

    @allure.step('Получить список заказов')
    def get_orders_list(self):
        orders = self.get_element(FeedPageLocators.ORDERS_LIST).text
        return orders

    @allure.step('Получить список заказов в работе')
    def get_orders_in_progress_list(self):

        orders_in_progress = self.get_element(FeedPageLocators.ORDERS_IN_PROGRESS).text
        return orders_in_progress

    @allure.step('Получить количество заказов, выполненных за всё время')
    def get_total_orders_count(self):
        self.wait_for_element(FeedPageLocators.TOTAL_ORDERS_COUNTER)
        total_orders = self.get_element(FeedPageLocators.TOTAL_ORDERS_COUNTER).text
        return total_orders

    @allure.step('Получить количество заказов, выполненных сегодня')
    def get_today_orders_count(self):
        self.wait_for_change_of_text_in_element(FeedPageLocators.ALL_ORDERS_READY, OrderData.all_orders_ready_placeholder)
        today_orders = self.get_element(FeedPageLocators.TODAY_ORDERS_COUNTER).text
        return today_orders