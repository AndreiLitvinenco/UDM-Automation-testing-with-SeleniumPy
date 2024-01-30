from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

#   Actions

driver.get("https://google.com") # opens a webpage

wait = WebDriverWait(driver, 10)

driver.maximize_window()


buttonLogin = driver.find_element(By.ID, "login_button") 
buttonLogin = wait.until(EC.presence_of_element_located(By.ID, "login_button"))
buttonLogin.click()
# clicks on an element

# buttonLogin = driver.find_element(By.ID, "login_button").click
# example of chaining


userInput = driver.find_element(By.ID, "user_input")
userInput.send_keys("This is a test")
userInput.send_keys(Keys.ENTER)
# writing text or pressing a button from keyboard


countryDropdown = driver.find_element(By.ID, "country_dropdown")
countryDropdown.select_by_value("Romania")
countryDropdown.select_by_index(185)
# interaction with a selectbox


driver.implicitly_wait(10) # global per session
wait = WebDriverWait(driver, 10)

time.sleep(5) #only if really needed
# await

driver.close() #closes 1 active browser
driver.quit() #closes the whole driver
