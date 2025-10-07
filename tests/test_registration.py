import allure
from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.RegistrationPage import RegistrationPageHelper
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

BASE_URL = 'https://ok.ru/'

@allure.suite('Проверка формы регистрации')
@allure.title('Проверка регистрации с случайно выбранной страной')
def test_registration_random_country(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_registration()
    RegistrationPage = RegistrationPageHelper(browser)
    Select_country_code = RegistrationPage.selectRandomCountry()
    Actual_country_code = RegistrationPage.get_phone_field_value()
    assert Select_country_code == Actual_country_code