from time import sleep
from selenium import webdriver
from threading import Thread




def test_testone():
    x = 10 + 10
    assert x == 20
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.maximize_window()
    print("Hello Python")
    driver.close()


def test_testtwo():
    y = 5 + 5
    assert y == 10
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/login/")
    driver.maximize_window()
    print("Hello Facebook")
    driver.close()
