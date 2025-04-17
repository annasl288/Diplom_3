from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators
import allure

class BasePage:

    def __init__(self, driver):
        with allure.step('Запустить браузер'):
            self.driver = driver

    def go_to_url(self, url):
        with allure.step(f'Перейти по ссылке {url}'):
            self.driver.get(url)

    def get_element(self, locator):
        with allure.step(f'Найти элемент {locator}'):
            return self.driver.find_element(*locator)

    def get_elements(self, locator):
        with allure.step(f'Найти элементы {locator}'):
            return self.driver.find_elements(*locator)

    def wait_for_element(self, locator):
        with allure.step(f'Дождаться видимости элемента {locator}'):
            WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))
            return self.get_element(locator)

    def wait_for_element_invisibility(self, locator):
        with allure.step(f'Дождаться исчезновения элемента {locator}'):
            WebDriverWait(self.driver, 15).until(expected_conditions.invisibility_of_element(locator))

    def wait_for_text_in_element(self, locator, text):
        with allure.step(f'Дождаться текста в элементе {locator}'):
            WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(locator, text))

    def wait_for_change_of_text_in_element(self, locator, text):
        with allure.step(f'Дождаться смены текста в элементе {locator}'):
            WebDriverWait(self.driver, 10).until_not(expected_conditions.text_to_be_present_in_element(locator, text))

    def wait_for_url(self, url):
        with allure.step(f'Дождаться перехода к странице {url}'):
            WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))

    def get_current_url(self):
        with allure.step('Получить текущий url'):
            return self.driver.current_url

    def click_element(self, locator):
        with allure.step(f'Кликнуть по элементу {locator}'):
            self.wait_for_element_invisibility(MainPageLocators.OVERLAY)
            self.wait_for_element(locator).click()