from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner

import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir + '\Resources')
sys.path.insert(0, parentdir + '\Resources\PageObjects')

from TestData import TestData
from Locators import Locators
from Pages import HomePage, AuthenticationPage

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=TestData.CHROME_PATH)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

class HomePageTest(BaseTest):

    def test_launch(self):
        """Test Case untuk launch URL"""

        # Membuat objek kelas HomePage
        self.homePage = HomePage(self.driver)

        # Mengambil page title dari HomePage
        title = self.homePage.get_title()

        # Verifikasi title page
        assert TestData.WEB_TITLE in title


    def test_login(self):
        """Test Case untuk login"""

        # Membuuat objek kelas HomePage
        self.homePage = HomePage(self.driver)

        # Mengeklik tombol Sign In
        self.homePage.signin()

        # Membuat objek kelas AuthenticationPage
        self.authenticationPage = AuthenticationPage(self.homePage.driver)

        # Mengisi email, password, dan mngeklik tombol Sign In
        self.authenticationPage.signin_registered()

        # Mengambil teks dari elemen header page My Account
        element = self.authenticationPage.get_text(Locators.MY_ACCOUNT_PAGE_HEADER)

        # Verifikasi teks header
        assert TestData.MY_ACCOUNT_PAGE_HEADER == element


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(open_in_browser=True,
                                                           output='report'))