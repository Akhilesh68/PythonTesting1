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

project = config.get("basic info", "project_name")
env = config.get("basic info", "environment")
url = config.get("basic info", "url")
browser = config.get("basic info","browser")
print(f"project name is: {project}")
print(f"Testing environment is: {env}")
print("url:", url)
print(f"Browser is: {browser}")

username = config.get("login cred","username")
pwd = config.get("login cred","pwd")
print(username)
print(pwd)

# Open browser and facebook website
driver =  webdriver.Chrome()
driver.get(url)
driver.maximize_window()
sleep(3)
driver.find_element(By.XPATH,"//input[@name='email']").send_keys(username)
sleep(3)
driver.find_element(By.XPATH,"//input[@name='pass']").send_keys(pwd)

wait = WebDriverWait(driver,15)
login_btn = wait.until(expected_conditions.element_to_be_clickable((By.ID,"loginbutton")))
login_btn.click()




