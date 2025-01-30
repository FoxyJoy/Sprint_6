import allure
import pytest

from utils.urls import *
from utils.data import *
import utils.locators as locators

from pages.main_page import YaScooterMainPage
from pages.order_page import YaScooterOrderPage


class TestYaScooterOrderPage:
    @allure.title('Проверка на некорректно заполненное имя')
    def test_order_page_first_name_input_incorrect_show_error_message(self, driver):
        order_page = YaScooterOrderPage(driver)
        main_page = YaScooterMainPage(driver)
        main_page.go_to_site(Urls.url_order_page)
        main_page.click_cookie_accept()
        main_page.click_on_top_order_button()
        order_page.input_first_name('Any')
        order_page.go_next()
        
        assert order_page.find_element(locators.incorrect_first_name_message).is_displayed()

    @allure.title('Проверка на некорректно заполненный фамилию')
    def test_order_page_last_name_input_incorrect_show_error_message(self, driver):
        order_page = YaScooterOrderPage(driver)
        main_page = YaScooterMainPage(driver)
        main_page.go_to_site(Urls.url_order_page)
        main_page.click_cookie_accept()
        main_page.click_on_top_order_button()
        order_page.input_last_name('Any')
        order_page.go_next()
         
        assert order_page.find_element(locators.incorrect_last_name_message).is_displayed()

    @allure.title('Проверка на некорректно заполненный адрес')
    def test_order_page_address_input_incorrect_show_error_message(self, driver):
        order_page = YaScooterOrderPage(driver)
        main_page = YaScooterMainPage(driver)
        main_page.go_to_site(Urls.url_order_page)
        main_page.click_cookie_accept()
        main_page.click_on_top_order_button()
        order_page.input_address('Any')
        order_page.go_next()
         
        assert order_page.find_element(locators.incorrect_adress_message).is_displayed()

    @allure.title('Проверка на некорректно заполненное метро')
    def test_order_page_subway_input_empty_show_error_message(self, driver):
        order_page = YaScooterOrderPage(driver)
        main_page = YaScooterMainPage(driver)
        main_page.go_to_site(Urls.url_order_page)
        main_page.click_cookie_accept()
        main_page.click_on_top_order_button()
        order_page.go_next()
         
        assert order_page.find_element(locators.incorrec_subway_message).is_displayed()

    @allure.title('Проверка на некорректно заполненный телефон')
    def test_order_page_telephone_number_input_incorrect_show_error_message(self, driver):
        order_page = YaScooterOrderPage(driver)
        main_page = YaScooterMainPage(driver)
        main_page.go_to_site(Urls.url_order_page)
        main_page.click_cookie_accept()
        main_page.click_on_top_order_button()
        order_page.input_telephone_field('1567')
        order_page.go_next()
         
        assert order_page.find_element(locators.incorrect_telephone_message).is_displayed()

    @allure.title('Проверка что при корректных заполненных данных на этапе "Для кого самокат", нажатии "Далее" происходит переход на следующий этап "Про аренду"')
    def test_order_page_go_to_choose_scooter_user_data_correct_open_about_rent(self, driver):
        order_page = YaScooterOrderPage(driver)
        main_page = YaScooterMainPage(driver)
        main_page.go_to_site(Urls.url_order_page)
        main_page.click_cookie_accept()
        main_page.click_on_top_order_button()
        order_page.fill_user_data(YaScooterOrderPageData.data_sets['data_set1'])  
        order_page.go_next()

        assert order_page.find_element(locators.order_button).is_displayed()
    
    @allure.title('Проверка что при корреткных заполненных данных на этапе "Про аренду", нажатии на кнопку "Заказать", происходит оформление заказа, открывается модальное окно с подтверждением об успешном создании заказа и присвоенным номером')
    @pytest.mark.parametrize('data_set', ['data_set1', 'data_set2'])
    def test_order_page_about_rent_input_correct_data_and_order_show_order_number(self, driver, data_set):
        order_page = YaScooterOrderPage(driver)
        main_page = YaScooterMainPage(driver)
        main_page.go_to_site(Urls.url_order_page)
        main_page.click_cookie_accept()
        main_page.click_on_top_order_button()
        order_page.fill_user_data(YaScooterOrderPageData.data_sets[data_set])  
        order_page.go_next()
        order_page.fill_rent_data(YaScooterOrderPageData.data_sets[data_set])
        order_page.go_to_order_button()
        order_page.accept_to_order_button()

        assert order_page.find_element(locators.order_completed_info).is_displayed()

    @allure.title('Проверка что при успешном оформлении заказа, заказ отображается на странице "Статус заказа"')
    @pytest.mark.parametrize('data_set', ['data_set1', 'data_set2'])
    def test_order_page_create_order_and_go_order_status(self, driver, data_set):
        order_page = YaScooterOrderPage(driver)
        main_page = YaScooterMainPage(driver)
        main_page.go_to_site(Urls.url_order_page)
        main_page.click_cookie_accept()
        main_page.click_on_top_order_button()
        order_page.fill_user_data(YaScooterOrderPageData.data_sets[data_set])  
        order_page.go_next()
        order_page.fill_rent_data(YaScooterOrderPageData.data_sets[data_set])
        order_page.go_to_order_button()
        order_page.accept_to_order_button()
        order_number = order_page.get_order_number()
        order_page.order_status()
        current_url = order_page.current_url()
         
        assert (Urls.order_status_page in current_url) and (order_number in current_url)