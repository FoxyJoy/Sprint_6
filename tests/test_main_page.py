import allure
import pytest

from selenium import webdriver
from pages.main_page import YaScooterMainPage
from utils.urls import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestYaScooterMainPage:
    @allure.title('Проверка что, на домашней верхней кнопке "Заказать", просходит корректный переход на страницу "Оформления заказа"')
    def test_click_top_order_button_show_order_page(self, driver: webdriver):
        main_page = YaScooterMainPage(driver)
        main_page.go_to_site()
        main_page.click_cookie_accept()
        main_page.click_on_top_order_button()
        main_page.wait_next_button()

        assert main_page.current_url() == Urls.url_order_page

    @allure.title('Проверка что, на домашней нижней кнопке "Заказать", просходит корректный переход на страницу "Оформления заказа"')
    def test_click_bottom_order_button_show_order_page(self, driver: webdriver):
        main_page = YaScooterMainPage(driver)
        main_page.go_to_site()
        main_page.click_cookie_accept()
        main_page.click_on_bottom_order_button()
        main_page.wait_next_button()

        assert main_page.current_url() == Urls.url_order_page

    @allure.title('Проверка что, на домашней странице по кнопке "ЯндексСамокат" происходит корреткный редирект на страницу "ЯндексДзен"')
    def test_click_yandex_button_go_to_yandex(self, driver: webdriver):
        main_page = YaScooterMainPage(driver)
        main_page.go_to_site()
        main_page.click_cookie_accept()
        main_page.click_yandex_button()
        main_page.switch_window(1)
        main_page.wait_url_until_not_about_blank()

        main_page.wait_dzen_in_button()

        current_url = main_page.current_url()

        assert (Urls.url_dzen_page in current_url) or (Urls.url_yandex_capcha_page in current_url) or (Urls.url_yandex_home_page in current_url)
