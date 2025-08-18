from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BY_QR = (By.XPATH, '//*[@data-l="t,get_qr"]')
    REGISTRATION_BUTTON = (By.XPATH, '//div[@class="external-oauth-login-footer"]/a[@data-l="t,register"]')
    QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    VK_REGISTRATION_BUTTON = (By.XPATH, '//*[@data-l = "t,vkc"]')
    MAIL_REGISTRATION_BUTTON = (By.XPATH, '//*[@data-l="t,mailru"]')
    YANDEX_REGISTRATION_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')
    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')

class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BY_QR)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.QR_TAB)
        self.find_element(LoginPageLocators.VK_REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.MAIL_REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_REGISTRATION_BUTTON)

    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def send_login(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys("dicky@mail.ru")

    def get_error_text(self):
        return self.find_element(LoginPageLocators.ERROR_TEXT).text