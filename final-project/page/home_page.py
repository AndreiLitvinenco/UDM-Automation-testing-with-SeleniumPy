from assertpy import assert_that, soft_assertions
from locator.locators import HomeLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def goToHome(self):
         self.driver.get("https://emag.ro")
         self.driver.maximize_window()

    def verifyLogo(self):
        logo = self.driver.find_element(*HomeLocators.logo)
        with soft_assertions():
            assert_that(logo.is_displayed()).is_true()

    def verifyTitle(self):
        #title = self.driver.find_element(*HomeLocators.homePageTitle)
        #with soft_assertions():
        #    assert_that(title.text).contains("eMAG")
        title = self.driver.title
        assert_that(title).contains("eMAG")

