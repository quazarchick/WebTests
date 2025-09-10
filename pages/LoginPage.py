import allure
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BY_QR = (By.XPATH, '//*[@data-l="t,get_qr"]')
    RESTORE_LINK = (By.XPATH, '//*[@data-l="t,restore"]')
    REGISTRATION_BUTTON = (By.XPATH, '//div[@class="external-oauth-login-footer"]/a[@data-l="t,register"]')
    QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    VK_REGISTRATION_BUTTON = (By.XPATH, '//*[@data-l = "t,vkc"]')
    MAIL_REGISTRATION_BUTTON = (By.XPATH, '//*[@data-l="t,mailru"]')
    YANDEX_REGISTRATION_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')
    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')
    GO_BACK_BUTTON = (By.XPATH, '//*[@data-l = "t,restore"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@class="external-oauth-login-help portlet_f"]')
    PROFILE_RECOVERY_BUTTON = (By.NAME, 'st.go_to_recovery')


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


    @allure.step('Нажать на кнопку "Войти" ')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Вводим данные в поле Логин')
    def send_login(self, login):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)

    @allure.step('Вводим данные в поле Пароль')
    def send_password(self, password):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('Переходим к восстановлению')
    def click_recovery(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.PROFILE_RECOVERY_BUTTON).click()

