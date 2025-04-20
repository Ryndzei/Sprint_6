import allure
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def wait_until(self, condition, timeout=10):
        return WebDriverWait(self.driver, timeout).until(condition)

    def open(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переключаемся на новую вкладку')
    def switch_to_new_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])