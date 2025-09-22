import allure
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class AdvetisementCabinetHelpLocators:
    TITLE = (By.XPATH, '//span[text()="Рекламный кабинет"]')

class AdvetisementCabinetHelpHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(AdvetisementCabinetHelpLocators.TITLE)