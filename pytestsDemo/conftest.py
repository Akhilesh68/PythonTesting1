import pytest
from selenium import webdriver
from configparser import ConfigParser
import os
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="session")
def config():
    config = ConfigParser()
    config.read("config.ini")
    return config


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")


def setup(request, browser):
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


