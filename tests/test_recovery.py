import allure
from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelperHelper
from pages.RecoveryPage import RecoveryPageHelperHelper
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

BASE_URL = 'https://ok.ru/'
LOGIN_TEXT = 'email'
PASSWORD_TEXT = '1'

@allure.suite("Проверка восстановления пользователя")
@allure.title("Проверка перехода к восстановлению после нескольких неудачных попыток авторизации")
def test_go_to_recovery_after_many_fails(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelperHelper(browser)
    LoginPage.send_login(LOGIN_TEXT)

    for i in range(3):
        LoginPage.send_password(PASSWORD_TEXT)
        LoginPage.click_login()

    LoginPage.click_recovery()
    RecoveryPage = RecoveryPageHelperHelper(browser)

