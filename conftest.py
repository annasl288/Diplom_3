import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from urls import Urls
from data import ExistingUser

@allure.step('Открыть браузер, перейти на главную страницу / Закрыть браузер')
@pytest.fixture(params = ["chrome", "firefox"])
def driver(request):

    driver = None
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    driver.get(Urls.main_page)
    yield driver
    driver.quit()

@allure.step('Авторизоваться существующим пользователем')
@pytest.fixture
def login(driver):

    main_page = MainPage(driver)
    main_page.click_login_button()

    login_page = LoginPage(driver)
    login_page.enter_email(ExistingUser.email)
    login_page.enter_password(ExistingUser.password)
    login_page.click_login_button()

    return driver