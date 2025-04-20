import allure
from page_objects.home_page import HomePage
from page_objects.order_page import OrderPage
from urls import *


class TestHomePageLogo:

    @allure.title('Проверка на успешный редирект на страницу Дзена по нажатию на слово Яндекс в логотипе')
    def test_successful_redirect_to_dzen_on_click_yandex_logo(self, driver):
        home_page = HomePage(driver)
        home_page.open(BASE_URL)
        home_page.click_yandex_logo()
        home_page.switch_to_new_window()
        home_page.wait_until_url_contains_dzen()

        assert DZEN_URL in home_page.get_current_url(), "Не произошёл редирект на Dzen"

    @allure.title('Проверка на успешный редирект на главную страницу Я.Самоката по нажатию на слово Самокат в логотипе')
    def test_successful_redirect_to_main_page_on_click_scooter_logo(self, driver):
        order_page = OrderPage(driver)
        home_page = HomePage(driver)
        order_page.open(ORDER_URL)
        home_page.click_scooter_logo()

        assert BASE_URL == home_page.get_current_url(), "Не произошёл переход на главную страницу самоката"