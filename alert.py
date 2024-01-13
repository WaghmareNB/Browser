import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://brightinfo.in/Alerts.html")
driver.maximize_window()

button = driver.find_element(By.XPATH, '//*[@id="content"]/button[1]')
button.click()

alert = driver.switch_to.alert
time.sleep(10)
alert.accept()