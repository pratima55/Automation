from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#open brower
driver =webdriver.Chrome()

#go to url
driver.get("https://www.saucedemo.com/")

time.sleep(10)

#element locate then value send
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

driver.find_element(By.XPATH,"//input[@id ='login-button']").click()
time.sleep(4)
print("login sucessful")

