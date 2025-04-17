from selenium.webdriver.common.by import By


class HomePageLocators:
    TOP_ORDER_BUTTON = [By.XPATH, ".//div[@class='Header_Nav__AGCXC']//button[text()='Заказать']"]
    BOTTOM_ORDER_BUTTON = [By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']//button[text()='Заказать']"]
    ACCEPT_COOKIE_BUTTON = [By.ID, "rcc-confirm-button"]
    QUESTION_BUTTONS = [By.XPATH, ".//div[@class='accordion__button']"]
    QUESTION_ANSWERS = [By.CSS_SELECTOR, ".accordion__panel > p"]

    @staticmethod
    def QUESTION_ANSWER(answer_index):
        return [By.XPATH, f".//div[@class='accordion__panel' and @id='accordion__panel-{answer_index}']/p"]