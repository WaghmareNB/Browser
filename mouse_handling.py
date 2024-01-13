from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://brightinfo.in/Button.html")
act=ActionChains(driver)
#menu=driver.find_element(By.XPATH,"//*[@id='content']/button[1]")
menu=driver.find_element(By.XPATH,"//*[@id='content']/button[3]")
#act.double_click(menu).perform()
act.context_click(menu).perform()

