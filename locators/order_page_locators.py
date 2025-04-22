from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = [By.XPATH, ".//input[@placeholder='* Имя']"]
    SURNAME_INPUT = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    ADDRESS_INPUT = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    SUBWAY_INPUT = [By.XPATH, ".//input[contains(@placeholder,'метро')]"]

    @staticmethod
    def SUBWAY_HINT_BUTTON(subway_name):
        return [By.XPATH, f".//div[text()='{subway_name}']/parent::button"]

    PHONE_INPUT = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]
    DATE_INPUT = [By.XPATH, ".//input[contains(@placeholder,'Когда')]"]
    RENTAL_PERIOD_INPUT = [By.XPATH, ".//span[@class='Dropdown-arrow']"]
    RENTAL_PERIOD_LIST = [By.XPATH, ".//div[@class='Dropdown-option']"]
    COLOR_CHECKBOXES = [By.XPATH, ".//div[contains(text(),'Цвет')]/parent::div//input"]
    ORDER_BUTTON = [By.XPATH, ".//button[text()='Назад']/parent::div/button[text()='Заказать']"]
    CONFIRM_ORDER_BUTTON = [By.XPATH, ".//button[text()='Да']"]
    ORDER_MADE_SCREEN = [By.XPATH, "//div[contains(text(), 'Заказ оформлен')]"]