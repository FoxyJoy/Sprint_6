from selenium.webdriver.common.by import By
from utils.data import *
    
# class YaScooterMainPageLocator:
top_order_button = [By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']"]
bottom_order_button = [By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']"]
ya_site_button = [By.XPATH, ".//img[@alt='Yandex']/parent::a"]
cookie_accept = [By.XPATH, ".//button[text()='да все привыкли']"]
f_question_about_imp = [By.XPATH, ".//div[text()='Вопросы о важном']"]
faq_answer = [By.CSS_SELECTOR, ".accordion__panel > p"]
faq_button = [By.XPATH, ".//div[@class='accordion__button']"]
faq = [By.XPATH, ".//div[@class='Home_FourPart__1uthg']"]
next_button = [By.XPATH, ".//button[text()='Далее']"]
dzen_in_button = [By.XPATH, ".//button[text()='Найти']"]



@staticmethod
# Возвращает локатор кнопки с вопросом FAQ (нумерация сверху вниз)
def get_faq_question_button(question_number):
    return [By.XPATH, f".//div[@class='accordion__button' and @id='accordion__heading-{question_number}']"]


@staticmethod
# Возвращает локатор дива с ответом FAQ (нумеерация сверху вниз). Сами тексты ответов находятся в utils/data.py
def get_faq_answer(answer_number):
    return [By.XPATH, f".//div[@id='accordion__panel-{answer_number}' and not(@hidden)]/p"]

# @staticmethod
def create_faq():
    qcount = len(faq_ansvers_text)

    result = []
    for i in range(qcount):
        tmp = []
        tmp.append(get_faq_question_button(i))
        tmp.append(get_faq_answer(i))
        tmp.append(faq_ansvers_text[i])
        result.append(tmp)

    return result
# class YaScooterOrderPageLocator:
first_name_input = [By.XPATH, ".//input[contains(@placeholder,'Имя')]"]
incorrect_first_name_message = [By.XPATH, ".//input[contains(@placeholder,'Имя')]/parent::div/div"]
last_name_input = [By.XPATH, ".//input[contains(@placeholder,'Фамилия')]"]
incorrect_last_name_message = [By.XPATH, ".//input[contains(@placeholder,'Фамилия')]/parent::div/div"]
adress_input = [By.XPATH, ".//input[contains(@placeholder,'Адрес')]"]
incorrect_adress_message = [By.XPATH, ".//input[contains(@placeholder,'Адрес')]/parent::div/div"]
subway_field = [By.XPATH, ".//input[contains(@placeholder,'метро')]"]  # /parent::div
incorrec_subway_message = [By.XPATH, ".//input[contains(@placeholder,'метро')]/parent::div/parent::div/parent::div/div[@class!='select-search']"]
telephone_field = [By.XPATH, ".//input[contains(@placeholder,'Телефон')]"]
incorrect_telephone_message = [By.XPATH, ".//input[contains(@placeholder,'Телефон')]/parent::div/div"]
date_field = [By.XPATH, ".//input[contains(@placeholder,'Когда')]"]
order_button = [By.XPATH, ".//button[text()='Назад']/parent::div/button[text()='Заказать']"]
accept_order_button = [By.XPATH, ".//button[text()='Нет']/parent::div/button[text()='Да']"]
show_status_order = [By.XPATH, ".//button[text()='Статус заказа']"]
order_completed_info = [By.XPATH, ".//div[contains(text(),'Номер заказа')]"]
show_status_button = [By.XPATH, ".//button[text()='Посмотреть статус']"]
back_button = [By.XPATH, ".//button[text()='Назад']"]
rental_period = [By.XPATH, ".//span[@class='Dropdown-arrow']"]
rental_period_list = [By.XPATH, ".//div[@class='Dropdown-option']"]
colour_checkboxes = [By.XPATH, ".//div[contains(text(),'Цвет')]/parent::div//input"]
comment_for_courier_field = [By.XPATH, ".//input[contains(@placeholder,'Комментарий для курьера')]"]
order_button = [By.XPATH, ".//button[text()='Назад']/parent::div/button[text()='Заказать']"]

@staticmethod
def subway_hint_button(subway: str):
    return [By.XPATH, f".//div[text()='{subway}']/parent::button"]
