from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):

    @allure.step('Получение текста ответа на вопрос')
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_LAST)
        self.click_on_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)