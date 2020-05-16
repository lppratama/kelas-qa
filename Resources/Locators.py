from selenium.webdriver.common.by import By

class Locators():
    # --- Home Page Locators ---
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "a.login")

    # --- Authentication Page Locators ---
    REGISTERED_EMAIL_INPUT = (By.ID, "email")
    REGISTERED_PASSWORD_INPUT = (By.ID, "passwd")
    REGISTERED_SIGNIN_BUTTON = (By.ID, "SubmitLogin")

    # --- My Account Page Locators ---
    MY_ACCOUNT_PAGE_HEADER = (By.CSS_SELECTOR, "h1.page-heading")