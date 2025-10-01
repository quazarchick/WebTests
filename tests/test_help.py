from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageHelperHelper, HelpPageLocators
from pages.LoginPage import LoginPageHelperHelper
from pages.AdvetisementCabinetHelp import AdvetisementCabinetHelpHelper
import allure
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

BASE_URL = 'https://ok.ru/help'

@allure.suite("Проверка страницы помощи")
@allure.title("Проверка перехода в рекламный кабинет со страницы Помощь")
def test_help_test(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelperHelper(browser)
    HelpPage.scrollToItem(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvetisementCabinetHelpHelper(browser)