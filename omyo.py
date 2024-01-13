from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
chkbox= driver.find_element(By.ID,"checkbox1")
if chkbox.is_selected():
    pass
else:
    chkbox.click()
chkbox2 =driver.find_element(By.ID,"checkbox2")
if chkbox2.is_selected():
    pass
else:
    chkbox2.click()
chkredio = driver.find_element(By.ID,"radio1")
if chkredio.is_selected():
    pass
else:
    chkredio.click()
