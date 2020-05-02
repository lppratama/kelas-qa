from selenium import webdriver

base_url = "http://automationpractice.com/index.php"
driver = webdriver.Chrome(executable_path=r"C:\Users\Glintz\kelon\qa-python\Drivers\chromedriver.exe")

driver.maximize_window()
driver.get(base_url)

assert "My Store" in driver.title

driver.quit()

