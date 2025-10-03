from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.HelpPage import HelpPageHelper, HelpPageLocators
from pages.LoginPage import LoginPageHelper
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
    BasePage(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scrollToItem(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvetisementCabinetHelpHelper(browser)