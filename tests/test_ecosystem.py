from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageHelper, HelpPageLocators
from pages.LoginPage import LoginPageHelper
from pages.VKecosystem_page import VKEcosystemPageHelper
from pages.AdvetisementCabinetHelp import AdvetisementCabinetHelpHelper
import allure
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

BASE_URL = 'https://ok.ru/'

@allure.suite('Проверка тулбара')
@allure.title('Переход к проектам экосистемы VK')
def test_to_go_vk_ecosystem(browser):
    BasePage = BasePageHelper(browser)
    BasePage.get_url(BASE_URL)
    BasePage.check_page()
    LoginPage = LoginPageHelper(browser)
    current_window_id = LoginPage.get_window_id(0)
    LoginPage.click_vk_ecosystem()
    LoginPage.click_more_button()
    new_window_id = LoginPage.get_window_id(1)
    LoginPage.swith_window(new_window_id)
    VKEcosystemPage = VKEcosystemPageHelper(browser)
    VKEcosystemPage.swith_window(current_window_id)
    LoginPageHelper(browser)