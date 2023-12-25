import sys
sys.path.append("D:/proiecte_cc++/github/Udemy-course-automation-testing-with-Seleniumpy/POM")

from selenium import webdriver
import unittest
from Pages.login_page import LoginPage as LP

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        loginPage = LP(self.driver)

        loginPage.goToLogin()
        loginPage.setUsername()
        loginPage.setPassword()
        loginPage.clickSubmit()
        loginPage.verifyLoginTitle()

    def tearDown(self):
        self.driver.quit()

if __name__  == "__main__":
    unittest.main()