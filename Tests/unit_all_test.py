from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner

base_url = "http://automationpractice.com/index.php"
username = "extract1234@yopmail.com"
password = "12345"

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Glintz\kelon\qa-python\Drivers\chromedriver.exe")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

class LandingPageTest(BaseTest):

    def test_launch(self):
        """Test Case untuk launch URL"""
        # Memasukkan URL
        self.driver.get(base_url)

        # Verifikasi title page
        assert "My Store" in self.driver.title


    def test_login(self):
        """Test Case untuk login"""
        self.driver.get(base_url)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.login"))).click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "email"))).send_keys(username)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "passwd"))).send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "SubmitLogin"))).click()

        # driver.find_element_by_id("passwd").send_keys(password)
        # driver.find_element_by_id("SubmitLogin").click()

        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.page-heading")))

        assert "MY ACCOUNT" == element.text


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(open_in_browser=True,
                                                           output='report'))