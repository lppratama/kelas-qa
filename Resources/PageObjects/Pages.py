from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from Locators import Locators
from TestData import TestData

class BasePage():
    """
    Kelas ini akan menjadi parent untuk kelas lainnya
    Kelas ini akan memuat elemen dan fungsi yg dapat digunakan
    di kelas lain
    """

    # fungsi ini dipanggil ketika objek baru di kelas BasePage dibuat
    def __init__(self, driver):
        self.driver = driver

    # fungsi ini akan mengeklik lokator elemen yang diberikan
    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    # fungsi enter teks
    def enter_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).send_keys(text)

    # fungsi untuk get teks
    def get_text(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).text

    # fungsi untuk get page title
    def get_title(self):
        return self.driver.title

    # fungsi untuk mengecek locator elemen yg diberikan terlihat (visible) atau tidak
    def is_visible(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return bool(element)
        except TimeoutException:
            return False

class HomePage(BasePage):
    """Automation Practice Home Page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def signin(self):
        #fungsi ini mnegeklik tombol Sign In
        self.click(Locators.SIGN_IN_BUTTON)
        self.is_visible(Locators.REGISTERED_EMAIL_INPUT)

class AuthenticationPage(BasePage):
    """Authentication Page"""

    def __init__(self, driver):
        super().__init__(driver)

    def signin_registered(self):
        self.enter_text(Locators.REGISTERED_EMAIL_INPUT, TestData.EMAIL)
        self.enter_text(Locators.REGISTERED_PASSWORD_INPUT, TestData.PASSWORD)
        self.click(Locators.REGISTERED_SIGNIN_BUTTON)
        self.is_visible(Locators.MY_ACCOUNT_PAGE_HEADER)