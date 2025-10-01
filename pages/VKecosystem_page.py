import allure
from selenium.webdriver.common.by import By
from pages.BasePage import BasePageHelper

class VKEcosystemPageLocators:
    pass

class VKEcosystemPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(VKEcosystemPageLocators)