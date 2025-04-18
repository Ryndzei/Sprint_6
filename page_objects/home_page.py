import allure
from locators.home_page_locators import HomePageLocators
from selenium.webdriver.support import expected_conditions as ec
from page_objects.base_page import BasePage
from urls import DZEN_URL


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликаем по кнопке Заказать вверху страницы')
    def click_top_order_button(self):
        self.find_element(HomePageLocators.TOP_ORDER_BUTTON).click()

    @allure.step('Кликаем по кнопке Заказать внизу страницы')
    def click_bottom_order_button(self):
        self.find_element(HomePageLocators.BOTTOM_ORDER_BUTTON).click()

    @allure.step('Кликаем по кнопке принятия использования куки')
    def accept_cookie_click(self):
        self.find_element(HomePageLocators.ACCEPT_COOKIE_BUTTON).click()

    @allure.step('Переключаемся на новую вкладку')
    def switch_to_new_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    @allure.step('Ждем пока страница редиректа прогрузится')
    def wait_until_url_contains_dzen(self, timeout=10):
        return self.wait_until(ec.url_contains(DZEN_URL), timeout)

    @allure.step('Нажимаем на {question_index} вопрос в FAQ')
    def click_question(self, question_index):
        elements = self.wait_until(ec.presence_of_all_elements_located(HomePageLocators.QUESTION_BUTTONS), timeout=3)
        return elements[question_index].click()

    @allure.step('Получаем текст ответа на вопрос {answer_index}')
    def get_answer_text(self, answer_index):
        answer_element = self.find_element(HomePageLocators.QUESTION_ANSWER(answer_index))
        return answer_element.text if answer_element.is_displayed() else None