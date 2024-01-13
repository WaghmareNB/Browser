from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

chrome_options = Options()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://omayo.blogspot.com/")
driver.maximize_window()
a = Select(driver.find_element(By.ID,"drop1"))
a.select_by_index("1")

