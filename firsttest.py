from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#open brower
driver =webdriver.Chrome()

#go to url
driver.get("https://www.saucedemo.com/")

time.sleep(4)

#element locate then value send
driver.find_element(By.ID, "user-name").send_keys("standard_user") 
driver.find_element(By.ID, "password").send_keys("secret_sauce")

driver.find_element(By.XPATH,"//input[@id ='login-button']").click()
time.sleep(4)



assert driver.current_url == "https://www.saucedemo.com/cart.html", "url mismatch after login"
assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
print("test passed")
driver.quit()

