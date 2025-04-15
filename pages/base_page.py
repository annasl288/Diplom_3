from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_url(self, url):
        self.driver.get(url)

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))
        return self.get_element(locator)

    def wait_for_element_invisibility(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.invisibility_of_element(locator))

    def wait_for_url(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))

    def get_current_url(self):
        return self.driver.current_url

    def click_element(self, locator):
        self.wait_for_element_invisibility(MainPageLocators.OVERLAY)
        self.wait_for_element(locator).click()