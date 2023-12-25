from selenium.webdriver.common.by import By

class LoginLocators:
    username = (By.ID, "username")
    password = (By.ID, "password")
    submit = (By.ID, "submit")
    loginTitle = (By.CSS_SELECTOR, "h1.post-title")
    