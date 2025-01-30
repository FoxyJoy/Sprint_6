import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import YaScooterBasePage
from utils.data import *
import utils.locators as locators
from pages.base_page import YaScooterBasePage

class YaScooterMainPage(YaScooterBasePage):
    @allure.step("Нажать на кнопку 'Заказать' вверху страницы")
    def click_on_top_order_button(self):
        self.find_element(locators.top_order_button).click()

    @allure.step("Нажать на кнопку 'Заказать' внизу страницы")
    def click_on_bottom_order_button(self):
        self.find_element(locators.bottom_order_button).click()

    @allure.step('Перейти на страницу яндекса')
    def click_yandex_button(self):
        self.find_element(locators.ya_site_button).click()

    @allure.step('Принять куки')
    def click_cookie_accept(self):
        if  self.find_element(locators.cookie_accept):
             self.find_element(locators.cookie_accept).click()
    
    @allure.step('Нажать на вопрос в FAQ')
    def click_faq_button(self, faq_button):
        self.find_element(faq_button).click()

    @allure.step('Получить ответ')
    def get_selected_ansver(self, faq_ansver):
        return self.find_element(faq_ansver).text
    
    @allure.step('Ожидание кнопки далее')
    def wait_next_button(self):
        self.find_element_clickable(locators.next_button)

    @allure.step('Ожидание перехода на Дзен')
    def wait_dzen_in_button(self):
        self.find_element(locators.dzen_in_button)

    
