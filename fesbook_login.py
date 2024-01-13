from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.ID,'Email address or phone number').send_keys("waghamarenandkishor2093@gmail.com")

