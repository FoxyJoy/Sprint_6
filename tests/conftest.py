import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from utils.urls import Urls
from selenium.webdriver.common.by import By
from pages.main_page import *

# Создание драйвера Firefox
@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.url_main_page)
    yield driver
    driver.quit()

