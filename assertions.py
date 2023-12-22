
from selenium import webdriver
from assertpy import assert_that, soft_assertions


driver = webdriver.Chrome()
driver.get("https://google.com")

pageTitle = driver.title

#assert_that(pageTitle).is_equal_to("Gogle") # not working
#print(pageTitle)

##assert_that(pageTitle).is_equal_to("Google") working
#print(pageTitle)


#assert_that(pageTitle).is_equal_to("Googe")
#assert_that(pageTitle).is_length(5)
#assert_that(pageTitle).contains("log")
# hard assertions - stops the app if one is broken



with soft_assertions():
    assert_that(pageTitle).is_equal_to("Googe")
    assert_that(pageTitle).is_length(5)
    assert_that(pageTitle).contains("ww")
#soft assertion - keeps running if any asserts breaks