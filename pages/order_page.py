import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import YaScooterBasePage
from utils.data import *
import utils.locators as locators
from utils.urls import *
import re


class YaScooterOrderPage(YaScooterBasePage):
    @allure.step('Ввод фамилии')
    def input_last_name(self, last_name: str):
        return self.find_element(locators.last_name_input).send_keys(last_name)
    
    @allure.step('Ввод имя')
    def input_first_name(self, first_name: str):
        return self.find_element(locators.first_name_input).send_keys(first_name)
    
    @allure.step('Ввод адреса')
    def input_address(self, address: str):
        return self.find_element(locators.adress_input).send_keys(address)
    
    @allure.step('Ввод метро')
    def input_subway_field(self, subway: str):
        self.find_element(locators.subway_field).click()
        return self.find_element(locators.subway_hint_button(subway)).click()

    @allure.step('Ввод номера телефона')
    def input_telephone_field(self, telephone):
        return self.find_element(locators.telephone_field).send_keys(telephone)

    @allure.step('Перейти на следующий этап заказа')
    def go_next(self):
        return self.find_element(locators.next_button).click()

    @allure.step('Ввод даты')
    def input_date(self, date: str):
        return self.find_element(locators.date_field).send_keys(date)
    
    @allure.step('Ввод время аренды')
    def input_rental_period(self, option: int):
        self.find_element(locators.rental_period).click()
        return self.find_elements(locators.rental_period_list)[option].click()
    
    @allure.step('цвет самоката')
    def input_colour_checkboxes(self, option: int):
        return self.find_elements(locators.colour_checkboxes)[option].click()

    @allure.step('Комментарий для курьера')
    def input_comment_for_courier_field(self, comment):
        return self.find_element(locators.comment_for_courier_field).send_keys(comment)

    @allure.step('Нажать "Заказать"')
    def go_to_order_button(self):
        return self.find_element(locators.order_button).click()

    @allure.step('Подтвердить заказ') 
    def accept_to_order_button(self):
        return self.find_element(locators.accept_order_button).click()
    
    @allure.step('Узнать номер заказа')
    def get_order_number(self):
        about_order_text = self.find_element(locators.order_completed_info).text
        return ''.join(re.findall('[0-9]', about_order_text))

    @allure.step('Перейти к "Cтатусу заказа"')
    def order_status(self):
        return self.find_element(locators.show_status_button).click()

    @allure.step('Заполнить данные на этапе "Для кого самокат"')
    def fill_user_data(self, data_set: dict):
        self.input_first_name(data_set['first_name'])
        self.input_last_name(data_set['last_name'])
        self.input_address(data_set['address'])
        self.input_subway_field(data_set['subway'])
        self.input_telephone_field(data_set['telephone'])

    @allure.step('Заполнить данные на этапе "Про аренду"')
    def fill_rent_data(self, data_set: dict):
        self.input_date(data_set['date'])
        self.input_rental_period(data_set['r_period'])
        for option in data_set['colour']:
            self.input_colour_checkboxes(option)
        self.input_comment_for_courier_field(data_set['comment'])
