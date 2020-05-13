from selenium import webdriver
import unittest

class LaunchTest(unittest.TestCase):

    def test_login(self):
        """Test Case untuk launch URL"""

        # Membuka webdriver
        self.base_url = "http://automationpractice.com/index.php"
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Glintz\kelon\qa-python\Drivers\chromedriver.exe")

        #Memaksmumkan browser window
        self.driver.maximize_window()

        # Memasukkan URL
        self.driver.get(self.base_url)

        # Verifikasi title page
        assert "My Store" in self.driver.title

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
