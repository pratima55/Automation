from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#open brower
driver =webdriver.Chrome()

#go to url
driver.get("https://www.youtube.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@name='search_query']").send_keys("premier league")
time.sleep(4)
driver.find_element(By.XPATH, "(//span[@class='yt-icon-shape ytSpecIconShapeHost'])[2]").click()
time.sleep(4)
driver.find_element(By.XPATH, "(//video[@class='video-stream html5-main-video'])[2]").click()
