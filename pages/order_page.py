import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.data import *
import utils.locators as locators
from utils.urls import *
import re

class YaScooterOrderPage:
    def __init__(self, driver):
        self.driver = driver

    #Ввод фамилии
    def input_last_name(self, last_name: str):
        return self.find_element(locators.last_name_input).send_keys(last_name)
    
    # Ввод имя
    def input_first_name(self, first_name: str):
        return self.find_element(locators.first_name_input).send_keys(first_name)
    
    # Ввод адреса
    def input_address(self, address: str):
        return self.find_element(locators.adress_input).send_keys(address)
    
    def input_subway_field(self, subway: str):
        self.find_element(locators.subway_field).click()
        return self.find_element(locators.subway_hint_button(subway)).click()


    # Ввод номера телефона
    def input_telephone_field(self, telephone):
        return self.find_element(locators.telephone_field).send_keys(telephone)

    # Перейти на следующий этап заказа
    def go_next(self):
        return self.find_element(locators.next_button).click()

    # Ввод даты
    def input_date(self, date: str):
        return self.find_element(locators.date_field).send_keys(date)
    
    def input_rental_period(self, option: int):
        self.find_element(locators.rental_period).click()
        return self.find_elements(locators.rental_period_list)[option].click()
    
    def input_colour_checkboxes(self, option: int):
        return self.find_elements(locators.colour_checkboxes)[option].click()

    # Комментарий для курьера
    def input_comment_for_courier_field(self, comment):
        return self.find_element(locators.comment_for_courier_field).send_keys(comment)

    # Нажать "Заказать"
    def go_to_order_button(self):
        return self.find_element(locators.order_button).click()

    # Подтвердить заказ 
    def accept_to_order_button(self):
        return self.find_element(locators.accept_order_button).click()
    
    # Узнать номер заказа
    def get_order_number(self):
        about_order_text = self.find_element(locators.order_completed_info).text
        return ''.join(re.findall('[0-9]', about_order_text))

    # Перейти к 'Cтатусу заказа'
    def order_status(self):
        return self.find_element(locators.show_status_button).click()

    # Заполнить данные на этапе "Для кого самокат"
    def fill_user_data(self, data_set: dict):
        self.input_first_name(data_set['first_name'])
        self.input_last_name(data_set['last_name'])
        self.input_address(data_set['address'])
        self.input_subway_field(data_set['subway'])
        self.input_telephone_field(data_set['telephone'])

    # Заполнить данные на этапе "Про аренду"
    def fill_rent_data(self, data_set: dict):
        self.input_date(data_set['date'])
        self.input_rental_period(data_set['r_period'])
        for option in data_set['colour']:
            self.input_colour_checkboxes(option)
        self.input_comment_for_courier_field(data_set['comment'])

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")



