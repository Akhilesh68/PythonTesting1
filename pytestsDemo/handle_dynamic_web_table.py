import os
from configparser import ConfigParser
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

config = ConfigParser()
# Absolute project path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(PROJECT_ROOT, "config.ini")
config.read(config_path)

config.read('config.ini')
url = config.get("basic info","url1")
print(url)

driver  = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

text_msg = driver.find_element(By.XPATH,"//h2[text()='Dynamic Web Table']")
print(text_msg.text)

# below are static xpath for web table
# //table[@id='productTable']//tbody//tr//td[text()='Smartphone'] # static xpath
# //table[@id='productTable']//tbody//tr//td[text()='Laptop']//following-sibling::td[2] # static xpath

# to make above xpath in dynamic
expected_name = 'Tablet '
sleep(3)
xpath_text = "//table[@id='productTable']//tbody//tr//td[text()= '"+expected_name+"']"
sleep(3)
checkbox= driver.find_element(By.XPATH,xpath_text+"//following-sibling::td[2]//input[@type='checkbox']")
checkbox.click()
print(checkbox.is_selected())
sleep(3)








