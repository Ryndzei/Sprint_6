import allure
from locators.home_page_locators import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from urls import DZEN_URL


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем по кнопке Заказать вверху страницы')
    def click_top_order_button(self):
        self.driver.find_element(*HomePageLocators.TOP_ORDER_BUTTON).click()

    @allure.step('Кликаем по кнопке Заказать внизу страницы')
    def click_bottom_order_button(self):
        self.driver.find_element(*HomePageLocators.BOTTOM_ORDER_BUTTON).click()

    @allure.step('Кликаем по кнопке принятия использования куки')
    def accept_cookie_click(self):
        self.driver.find_element(*HomePageLocators.ACCEPT_COOKIE_BUTTON).click()

    @allure.step('Переключаемся на новую вкладку')
    def switch_to_new_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    @allure.step('Ждем пока страница редиректа прогрузится')
    def wait_until_url_contains_dzen(self, time=10):
        return WebDriverWait(self.driver, time).until(ec.url_contains(DZEN_URL))

    @allure.step('Нажимаем на {question_index} вопрос в FAQ')
    def click_question(self, question_index):
        elements = WebDriverWait(self.driver, 3).until(ec.presence_of_all_elements_located(HomePageLocators.QUESTION_BUTTONS))
        return elements[question_index].click()

    def find_element(self, locator):
        return self.driver.find_element(*locator)