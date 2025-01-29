import allure # импорировали библиотеку
import pytest
from selenium import webdriver
from utils.data import *
import utils.locators as locators
from pages.main_page import YaScooterMainPage

class TestQuestions:
    @pytest.mark.parametrize('faq_button, faq_ansver, faq_text', locators.create_faq())
    def test_questions(self, driver: webdriver, faq_button, faq_ansver, faq_text):
        main_page = YaScooterMainPage(driver)
        main_page.go_to_site()

        main_page.scroll_to_element(locators.faq)

        main_page.click_cookie_accept()
        main_page.click_faq_button(faq_button)

        ansver = main_page.get_selected_ansver(faq_ansver)

        assert ansver == faq_text
