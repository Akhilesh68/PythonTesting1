# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/#google_vignette")
#
#
# # driver.navigate().refresh()
# # driver.refresh()
# drp = Select(driver.find_element(By.XPATH,'//select'))
# # drp.select_by_index(1)
# drp.select_by_value('ASM  ')
# # drp.select_by_visible_text('Male')
# sleep(3)
#

def func(n1,n2):
    return n1 + n2

print(func(4,5))
print(func(4,'A'))
