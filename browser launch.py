import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

chrome_options = Options()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://brightinfo.in/login.html")
driver.maximize_window()
#driver.find_element(By.XPATH,'//*[@id=footer"]/div[2]/div/div/a/').click()  #'''automatic click on demo button'''
driver.find_element(By.ID,'username').send_keys("Bright@123")
driver.find_element(By.ID,'password').send_keys("pass123")
driver.find_element(By.XPATH,'/html/body/div[1]/div/form/div[3]/div/button').click()
driver.find_element(By.XPATH,'//*[@id="homeSubmenu"]/li[1]/a').click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='fname']").send_keys("Nandkishor")
driver.find_element(By.XPATH,'//*[@id="lname"]').send_keys("Waghmare")
a = Select(driver.find_element(By.XPATH,"//*[@id='country']"))
a.select_by_index("0")
driver.find_element(By.XPATH,'//*[@id="subject"]').send_keys("Automestion Testing")
button = driver.find_element(By.XPATH,'//*[@id="content"]/div/form/div[5]/input').click()
button.click()
driver.get("https://brightinfo.in/Text%20Box.html")
driver.back()


