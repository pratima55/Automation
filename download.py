from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/download")
driver.find_element(By.LINK_TEXT, "some-file.txt").click()
time.sleep(3)
driver.quit()