from time import sleep
from selenium import webdriver
from threading import Thread

driver = webdriver.Chrome()


def open_google():
    # driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    print("Open google")
    sleep(2)
    driver.quit()

def open_facebook():
    # driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/login/")
    print("Open facebook")
    sleep(2)
    driver.quit()

t1 = Thread(target=open_google)
t2 = Thread(target=open_facebook)

t1.start()
t2.start()

t1.join()
t2.join()
