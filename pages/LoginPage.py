from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BY_QR = (By.XPATH, '//*[@data-l="t,get_qr"]')
    REGISTRATION_BUTTON = (By.XPATH, '//*[@data-l="t,register"]')
    QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    VK_REGISTRATION_BUTTON = (By.XPATH, '//*[@data-l = "t,vkc"]')
    MAIL_REGISTRATION_BUTTON = (By.XPATH, '//*[@data-l="t,mailru"]')
    YANDEX_REGISTRATION_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')

class LoginPageHelper(BasePage):
    pass

