import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://brightinfo.in/Upload%20and%20Download.html")
driver.maximize_window()
driver.find_element(By.ID,"//*[@id='uploadFile']").send_keys("D:\\4k\\DEN.JPEG")