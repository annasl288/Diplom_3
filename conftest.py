import pytest
import allure
from selenium import webdriver
from locators import MainPageLocators, LoginPageLocators
from urls import Urls
from data import ExistingUser


@pytest.fixture(params = ["chrome", "firefox"])
@allure.step('Открыть браузер, перейти на главную страницу / Закрыть браузер')
def driver(request):

    driver = None
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    driver.get(Urls.main_page)
    yield driver
    driver.quit()


@pytest.fixture
@allure.step('Авторизоваться существующим пользователем')
def login(driver):

    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(ExistingUser.email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(ExistingUser.password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    return driver