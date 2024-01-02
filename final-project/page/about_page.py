from assertpy import assert_that, soft_assertions
from locator.locators import AboutLocators
from selenium.webdriver.common.by import By


class AboutPage:
    def __init__(self, driver):
        self.driver = driver

    def goToAbout(self):
        self.driver.get("https://about.emag.ro/")  
        self.driver.maximize_window() 
        
    def verifyTitle(self):
        title = self.driver.title
        assert_that(title).contains("eMAG")

    def verifyNavigation(self):
        navbar = self.driver.find_elements(*AboutLocators.navbarItems)
        elements = ("Grupul eMAG", "eMAG Teams", "Sustenabilitate", "Media")
        for i in range(len(navbar)):
            for j in range(len(elements)):
                with soft_assertions():
                    assert_that(navbar[i].text).is_equal_to(elements[j])
                i = i+1
            break