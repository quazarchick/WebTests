from selenium.webdriver.common.by import By
import allure
import random
from pages.BasePage import BasePage

class RegistrationPageLocators:
    PHONE_FIELD = (By.XPATH, '//div[@data_l="t,phone"]')
    COUNTRY_ITEM = (By.XPATH, '//*[@class="country-select_i"]')
    COUNTRY_LIST = (By.XPATH, '//div[@data_l="t,country"]')
    SUBMIT_BUTTON = (By.XPATH, '//input[@data_l="t,submit"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@class="country-select_i"]')

class RegistrationPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверка корректности загрузки страницы"):
            self.find_element(RegistrationPageLocators.PHONE_FIELD)
            self.find_element(RegistrationPageLocators.COUNTRY_LIST)
            self.find_element(RegistrationPageLocators.SUBMIT_BUTTON)
            self.find_element(RegistrationPageLocators.SUPPORT_BUTTON)

    def selectRandomCountry(self):
        random_number = random.randint(0, 212)
        self.find_element(RegistrationPageLocators.COUNTRY_LIST).click()
        country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
        country_items[random_number].click()
        return country_items[random_number].text

