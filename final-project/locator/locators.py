from selenium.webdriver.common.by import By

class HomeLocators:
    logo = (By.XPATH, "/html/body/div[3]/nav[1]/div/div/div[1]/a/img")
    homePageTitle = (By.CSS_SELECTOR, "head > title")

class AboutLocators:
    aboutPageTitle = (By.CSS_SELECTOR, "head > title")
    navbarItems = (By.CSS_SELECTOR, "#site-header > div.container > div > div.center.column > ul > li")