import allure
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def wait_until(self, condition, timeout=10):
        return WebDriverWait(self.driver, timeout).until(condition)

    def open(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Кликаем в логотипе на слово самокат')
    def click_scooter_logo(self):
        self.find_element(BasePageLocators.SCOOTER_LOGO).click()

    @allure.step('Кликаем в логотипе на слово Яндекс')
    def click_yandex_logo(self):
        self.find_element(BasePageLocators.YANDEX_LOGO).click()