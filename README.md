# Тема "UI тестирование с POM" курс ЯндексПрактикум | Sprint_6
Тема "Page Object" курс ЯндексПрактикум | Sprint_6
Для тестирования был выбран сервис [«Яндекс.Самокат»](https://qa-scooter.praktikum-services.ru/) 
В связи с грядущим релизом были созданы проверки: 


---
### О репозитиории
#### В директории [utils](utils) лежат треубемые для тестов [Локаторы](utils/locators.py), [Тестовые данные user-a](utils/data.py) ,[urls](utils/urls.py).

#### В директории [pages](pages) лежат actions [для "Домашней страницы"](pages/main_page.py), [для "Страницы заказа самоката"](pages/order_page.py)



### [Домашняя страница](tests/test_main.page.py) 
- Проверка что, на домашней верхней кнопке "Заказать", просходит корректный переход на страницу "Оформления заказа"
```
def test_click_top_order_button_show_order_page(self, driver: webdriver)
```

- Проверка что, на домашней нижней кнопке "Заказать", просходит корректный переход на страницу "Оформления заказа"
```
def test_click_bottom_order_button_show_order_page(self, driver: webdriver)
```

- Проверка что, на домашней странице по кнопке "ЯндексСамокат" происходит корреткный редирект на страницу "ЯндексДзен"
```
def test_click_yandex_button_go_to_yandex(self, driver: webdriver)
```

 ### [Оформление заказа](tests/test_order_page.py)
- Проверка на некорректно заполненное имя
```
def test_order_page_first_name_input_incorrect_show_error_message(self, driver)
```

- Проверка на некорректно заполненный фамилию
```
 def test_order_page_last_name_input_incorrect_show_error_message(self, driver)
```

- Проверка на некорректно заполненный адрес
```
def test_order_page_address_input_incorrect_show_error_message(self, driver)
```

- Проверка на некорректно заполненное метро
```
def test_order_page_subway_input_empty_show_error_message(self, driver)
```

- Проверка на некорректно заполненный телефон
```
def test_order_page_telephone_number_input_incorrect_show_error_message(self, driver)
```
- Проверка что при корректных заполненных данных на этапе "Для кого самокат", нажатии "Далее" происходит переход на следующий этап "Про аренду"
```
def test_order_page_go_to_choose_scooter_user_data_correct_open_about_rent(self, driver)
```
- Проверка что при корреткных заполненных данных на этапе "Про аренду", нажатии на кнопку "Заказать", происходит оформление заказа, открывается модальное окно с подтверждением об успешном создании заказа и присвоенным номером
```
def test_order_page_about_rent_input_correct_data_and_order_show_order_number(self, driver, data_set)
```
- Проверка что при успешном оформлении заказа, заказ отображается на странице "Статус заказа"
```
def test_order_page_create_order_and_go_order_status(self, driver, data_set)
```

### [Вопросы о важном](tests/test_question.py)
- Перебор ответов и вопросов в FAQ
```
def test_questions(self, driver: webdriver, faq_button, faq_ansver, faq_text)
```

### Тестовый Фреймворк 
- pytest / selenium / allure
---

Перед работой с репозиторием требуется установить зависимости 
``` shell
pip3 install -r requirements.txt
```
Запустить все тесты из директории tests
```shell
pytest tests --alluredir=allure_results
```
Посмотреть отчет в веб версии пройденного прогона
``` shell
allure serve allure_results
```