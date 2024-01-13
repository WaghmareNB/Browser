from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="name"]').send_keys('nandkishor waghmare')
driver.find_element(By.XPATH,'//*[@id="email"]').send_keys('waghamarenandkishor2093@gmail.com')
driver.find_element(By.XPATH,'//*[@id="phone"]').send_keys('+917391804531')
driver.find_element(By.XPATH,'//*[@id="Address"]').send_keys('lohgaon')
driver.find_element(By.XPATH,'//*[@id="male"]"]').click()



