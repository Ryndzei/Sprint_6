import allure
from test_data import OrderPageDataSets
from urls import *


class TestOrderPageMakeOrder:

    @allure.title('Проверка на успешное создание заказа через кнопку Заказать вверху главной страницы')
    def test_successful_order_from_top_order_button(self, home_page, order_page):
        home_page.open(BASE_URL)
        home_page.accept_cookie_click()
        home_page.click_top_order_button()
        order_page.fill_user_data(OrderPageDataSets.data_sets['data_set1'])
        order_page.click_next_button()
        order_page.fill_rent_data(OrderPageDataSets.data_sets['data_set1'])
        order_page.click_order_button()
        order_page.click_confirm_order_button()

        assert order_page.is_order_made_screen_displayed(), "Экран успешного заказа не отобразился"

    @allure.title('Проверка на успешное создание заказа через кнопку Заказать внизу главной страницы')
    def test_successful_order_from_bottom_order_button(self, home_page, order_page):
        home_page.open(BASE_URL)
        home_page.accept_cookie_click()
        home_page.click_bottom_order_button()
        order_page.fill_user_data(OrderPageDataSets.data_sets['data_set2'])
        order_page.click_next_button()
        order_page.fill_rent_data(OrderPageDataSets.data_sets['data_set2'])
        order_page.click_order_button()
        order_page.click_confirm_order_button()

        assert order_page.is_order_made_screen_displayed, "Экран успешного заказа не отобразился"