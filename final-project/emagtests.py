from selenium import webdriver
from selenium.webdriver.common.by import By
from assertpy import assert_that

driver = webdriver.Chrome()
driver.get("https://emag.ro")
driver.maximize_window()

#test 1
# home
# logo & title
logo = driver.find_element(By.XPATH,"/html/body/div[3]/nav[1]/div/div/div[1]/a/img")
assert_that(logo.is_displayed()).is_true()

title = driver.title
assert_that(title).contains("eMAG")


#test 2 
# about
# title & nav
driver.get("https://about.emag.ro")
title = driver.title
assert_that(title).contains("eMAG")


navbar = driver.find_elements(By.CSS_SELECTOR, "#site-header > div.container > div > div.center.column > ul > li")

elements = ("Grupul eMAG", "eMAG Teams", "Sustenabilitate", "Media")


for i in range(len(navbar)):
    for j in range(len(elements)):
        assert_that(navbar[i].text).is_equal_to(elements[j])
        i = i+1
    break
