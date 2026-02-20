# navigate browser

from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com/")
    driver.save_screenshot("google.png")
    print("google open")
except:
    print("google not opening")

driver.close()
