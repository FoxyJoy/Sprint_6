import allure
from utils.urls import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YaScooterBasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Найти элемент")
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    @allure.step("Найти элементы")
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")

    @allure.step("Найти элемент clickable")
    def find_element_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator), message=f"Can't find element by locator {locator}")

    @allure.step('Перейти на сайт')
    def go_to_site(self, url=None):
        if url is None:
            url = Urls.url_main_page
        self.driver.get(url)

    @allure.step('Получить текущий урл')
    def current_url(self):
        return self.driver.current_url
    
    @allure.step('Скролл')
    def scroll_to_element(self, element):
        self.find_element(element).location_once_scrolled_into_view

    @allure.step('Переключиться на вкладку браузера')
    def switch_window(self, window_number: int = 1):
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    def wait_url_until_not_about_blank(self, time=10):
        WebDriverWait(self.driver, time).until_not(EC.url_to_be('about:blank'))