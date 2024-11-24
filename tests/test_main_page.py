import data
import allure
import pytest

from pages.main_page import MainPage
from locators.main_page_locators import (MainPageLocators)


class TestMainPage:

    @allure.title('Проверка вопросов о важном')
    @allure.description('Проверка появления текста ответа соответствующему каждому вопросу')
    @pytest.mark.parametrize(
        'num, result',
        [
            (0, data.ANSWER_0),
            (1, data.ANSWER_1),
            (2, data.ANSWER_2),
            (3, data.ANSWER_3),
            (4, data.ANSWER_4),
            (5, data.ANSWER_5),
            (6, data.ANSWER_6),
            (7, data.ANSWER_7)
        ]
    )
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.open_page(data.MAIN_PAGE_URL)
        main_page.accept_cookies(MainPageLocators.ACCEPT_COOKIE_BUTTON)
        assert main_page.get_answer_text(num) == result