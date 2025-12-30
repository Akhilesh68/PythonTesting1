# import configparser
from configparser import ConfigParser
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

config = ConfigParser()

# Absolute project path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(PROJECT_ROOT, "config.ini")

print("Config file path:", config_path)
print("File exists:", os.path.exists(config_path))

config.read(config_path)

print("Available sections:", config.sections())

url = config.get("basic info", "url")
print("url:", url)
browser = config.get("basic info","browser")
print(browser)

username = config.get("locator login","username")
pwd = config.get("locator login","pwd")
print(username)
print(pwd)

driver =  webdriver.Chrome()
driver.get(url)
driver.maximize_window()
sleep(3)
driver.find_element(By.XPATH,username).send_keys("akhileshpatel597@gmail.com")
sleep(3)
driver.find_element(By.XPATH,pwd).send_keys("a@k551993")

wait = WebDriverWait(driver,15)
login_btn = wait.until(expected_conditions.element_to_be_clickable((By.ID,"loginbutton")))
login_btn.click()

sleep(5)


