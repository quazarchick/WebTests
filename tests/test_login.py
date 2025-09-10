import allure
from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



BASE_URL = 'https://ok.ru/'
EMPTY_LOGIN_ERROR = 'Введите логин'
EMPTY_PASSWORD_ERROR = 'Введите пароль'
LOGIN_TEXT = 'email'


@allure.suite("Проверка формы авторизации ")
@allure.title("Проверка ошибки при пустой форме авторизации")
def test_empty_login_and_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_login()
    assert LoginPage.get_error_text() == EMPTY_LOGIN_ERROR

@allure.title("Проверка ошибки при заполненном поле Логин и пустом поле Пароль")
def test_login_and_empty_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.send_login(LOGIN_TEXT)
    LoginPage.click_login()
    assert LoginPage.get_error_text() == EMPTY_PASSWORD_ERROR