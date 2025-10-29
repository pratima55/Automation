from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")


file_input=driver.find_element(By.ID, "file-upload")
file_input.send_keys("D:\myfile.txt.txt")

driver.find_element(By.ID, "file-submit").click()

time.sleep(2)
driver.quit()