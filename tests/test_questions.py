import allure
import pytest
from locators.home_page_locators import HomePageLocators
from test_data import HomePageAnswers
from page_objects.home_page import HomePage
from urls import *


class TestHomePageQuestions:

    @allure.title('Проверка на соответствие вопроса с индексом {question} и ответа с индексом {answer} в FAQ')
    @pytest.mark.parametrize(
        "question,answer,expected_answer",
        [
            (0, 0, HomePageAnswers.answer_1),
            (1, 1, HomePageAnswers.answer_2),
            (2, 2, HomePageAnswers.answer_3),
            (3, 3, HomePageAnswers.answer_4),
            (4, 4, HomePageAnswers.answer_5),
            (5, 5, HomePageAnswers.answer_6),
            (6, 6, HomePageAnswers.answer_7),
            (7, 7, HomePageAnswers.answer_8),
        ]
    )
    def test_faq_click_first_question_show_answer(self, driver, question, answer, expected_answer):
        driver.get(BASE_URL)
        home_page = HomePage(driver)
        home_page.accept_cookie_click()
        home_page.click_question(question_index=question)
        answer = home_page.find_element(HomePageLocators.QUESTION_ANSWER(answer_index=answer))

        assert answer.is_displayed() and answer.text == expected_answer, 'Ответ на вопрос не совпадает с ОР'