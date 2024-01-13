from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options =Options()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://brightinfo.in/check%20box.html")
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="myCheck"]').click()