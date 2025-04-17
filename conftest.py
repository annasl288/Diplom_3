import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage
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

    MainPage.click_login_button()
    LoginPage.enter_email(ExistingUser.email)
    LoginPage.enter_password(ExistingUser.password)
    LoginPage.click_login_button()

    return driver