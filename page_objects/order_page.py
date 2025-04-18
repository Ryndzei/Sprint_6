import allure
from locators.order_page_locators import OrderPageLocators
from page_objects.base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполняем поле Имя валидным значением')
    def set_first_name(self, first_name):
        self.find_element(OrderPageLocators.NAME_INPUT).send_keys(first_name)

    @allure.step('Заполняем поле Фамилия валидным значением')
    def set_last_name(self, last_name):
        self.find_element(OrderPageLocators.SURNAME_INPUT).send_keys(last_name)

    @allure.step('Заполняем поле Адрес валидным значением')
    def set_address(self, address):
        self.find_element(OrderPageLocators.ADDRESS_INPUT).send_keys(address)

    @allure.step('Выбираем станцию метро из списка')
    def set_subway(self, subway_name):
        self.find_element(OrderPageLocators.SUBWAY_INPUT).click()
        self.find_element(OrderPageLocators.SUBWAY_HINT_BUTTON(subway_name)).click()

    @allure.step('Заполняем поле Телефон валидным значением')
    def set_phone(self, phone):
        self.find_element(OrderPageLocators.PHONE_INPUT).send_keys(phone)

    @allure.step('Заполняем форму "Для кого самокат" валидными данными')
    def fill_user_data(self, data_set: dict):
        self.set_first_name(data_set['first_name'])
        self.set_last_name(data_set['last_name'])
        self.set_address(data_set['address'])
        self.set_subway(data_set['subway_name'])
        self.set_phone(data_set['telephone_number'])

    @allure.step('Кликаем по кнопке Далее')
    def click_next_button(self):
        self.find_element(OrderPageLocators.NEXT_BUTTON).click()

    @allure.step('Вводим валидную дату')
    def set_date(self, date):
        self.find_element(OrderPageLocators.DATE_INPUT).send_keys(date)

    @allure.step('Выбираем срок аренды из выпадающего меню')
    def set_rent_period(self, option):
        self.find_element(OrderPageLocators.RENTAL_PERIOD_INPUT).click()
        self.find_elements(OrderPageLocators.RENTAL_PERIOD_LIST)[option].click()

    @allure.step('Выбираем нужный цвет')
    def set_colour(self, option):
        self.find_elements(OrderPageLocators.COLOR_CHECKBOXES)[option].click()

    @allure.step('Заполняем форму "Про аренду" валидными данными')
    def fill_rent_data(self, data_set: dict):
        self.set_date(data_set['date'])
        self.set_rent_period(data_set['rental_period'])
        for option in data_set['color']:
            self.set_colour(option)

    @allure.step('Нажимаем кнопку Заказать')
    def click_order_button(self):
        self.find_element(OrderPageLocators.ORDER_BUTTON).click()

    @allure.step('Подтверждаем заказ')
    def click_confirm_order_button(self):
        self.find_element(OrderPageLocators.CONFIRM_ORDER_BUTTON).click()

    @allure.step('Проверяем, отображается ли экран успешного заказа')
    def is_order_made_screen_displayed(self):
        return self.find_element(OrderPageLocators.ORDER_MADE_SCREEN).is_displayed()