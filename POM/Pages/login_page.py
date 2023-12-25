from selenium.webdriver.common.by import By
from assertpy import assert_that, soft_assertions

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def goToLogin(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

    def setUsername(self, UserVal):
        username = self.driver.find_element(By.ID, "username")
        username.clear()
        username.send_keys(UserVal)

    def setPassword(self, PassVal):
        password = self.driver.find_element(By.ID, "password")
        password.clear()
        password.send_keys(PassVal)

    def clickSubmit(self):
        submitButton = self.driver.find_element(By.ID, "submit")
        submitButton.click()
    
    def verifyLoginTitle(self):
        title = self.driver.find_element(By.CSS_SELECTOR, "h1.post-title")
        with soft_assertions():
            assert_that(title).is_true()
        