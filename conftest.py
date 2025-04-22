import pytest
from selenium import webdriver
from page_objects.home_page import HomePage
from page_objects.order_page import OrderPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture(scope="function", name="home_page")
def home_page(driver):
    home_page = HomePage(driver)
    return home_page

@pytest.fixture(scope="function", name="order_page")
def order_page(driver):
    order_page = OrderPage(driver)
    return order_page