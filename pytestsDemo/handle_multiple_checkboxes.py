from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By



url = "https://testautomationpractice.blogspot.com/"
driver  = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

text_msg = driver.find_element(By.XPATH,"//label[text()='Days:']")
print(text_msg.text)

checkboxes= driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    names=checkbox.get_attribute("value")
    # print(names)

    if names=="monday":
        checkbox.click()
        print(checkbox.is_selected())


# OR

# day = "Sunday"
# checkbox= driver.find_element(By.XPATH, f"//label[normalize-space()='{day}']") # this will not click checkbox
# checkbox.click()
# print(checkbox.is_selected())

sleep(3)