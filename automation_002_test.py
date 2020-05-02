from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

base_url = "http://automationpractice.com/index.php"
username = "extract1234@yopmail.com"
password = "12345"
driver = webdriver.Chrome(executable_path=r"C:\Users\Glintz\kelon\qa-python\Drivers\chromedriver.exe")

driver.maximize_window()
driver.get(base_url)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.login"))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "email"))).send_keys(username)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "passwd"))).send_keys(password)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "SubmitLogin"))).click()

# driver.find_element_by_id("passwd").send_keys(password)
# driver.find_element_by_id("SubmitLogin").click()

element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.page-heading")))

assert "MY ACCOUNT" == element.text

driver.quit()