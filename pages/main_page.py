import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.data import *
import utils.locators as locators
from utils.urls import Urls


class YaScooterMainPage:
    def __init__(self, driver):
        self.driver = driver

    # Нажать на кнопку 'Заказать' вверху страницы
    def click_on_top_order_button(self):
        self.driver.find_element(*locators.top_order_button).click()

    # Нажать на кнопку 'Заказать' внизу страницы
    def click_on_bottom_order_button(self):
        self.driver.find_element(*locators.bottom_order_button).click()

    # Перейти на страницу яндекса
    def click_yandex_button(self):
        self.driver.find_element(*locators.ya_site_button).click()

    # Принять куки
    def click_cookie_accept(self):
        if self.driver.find_elements(*locators.cookie_accept):
            self.driver.find_element(*locators.cookie_accept).click()
    
    # Нажать на вопрос в FAQ
    def click_faq_button(self, faq_button):
       WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(faq_button)).click()
       self.driver.find_element(*faq_button).click()

    def get_selected_ansver(self, faq_ansver):
        return self.driver.find_element(*faq_ansver).text
    
    def scroll_to_element(self, element):
        bottom_element = self.driver.find_element(*element)
        bottom_element.location_once_scrolled_into_view

    # Переключиться на вкладку браузера
    def switch_window(self, window_number: int = 1):
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    def wait_url_until_not_about_blank(self, time=10):
        WebDriverWait(self.driver, time).until_not(EC.url_to_be('about:blank'))

    # Перейти на сайт
    def go_to_site(self, url=None):
        if url is None:
            url = Urls.url_main_page
        self.driver.get(url)

    # Получить текущий урл
    def current_url(self):
        return self.driver.current_url
 

