from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
import data
import allure


class OrderPage(BasePage):

    @allure.step('Открытие страницы заказа')
    def open_to_order_page(self, locator):
        self.open_page(data.MAIN_PAGE_URL)
        self.accept_cookies(MainPageLocators.ACCEPT_COOKIE_BUTTON)
        self.click_on_element(locator)

    @allure.step('Создание заказа')
    def set_order(self, name, surname, address, metro_station, phone, cell, comment):
        self.add_text_to_element(OrderPageLocators.NAME_INPUT_FIELD, name)
        self.add_text_to_element(OrderPageLocators.SURNAME_INPUT_FIELD, surname)
        self.add_text_to_element(OrderPageLocators.ADDRESS_INPUT_FIELD, address)
        self.click_on_element(OrderPageLocators.METRO_STATION_INPUT_FIELD)
        self.click_on_element(metro_station)
        self.add_text_to_element(OrderPageLocators.PHONE_INPUT_FIELD, phone)
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)
        self.click_on_the_specific_cell_of_calendar(cell)
        self.click_on_element(OrderPageLocators.DROPDOWN_FIELD)
        self.click_on_element(OrderPageLocators.DROPDOWN_MENU)
        self.click_on_element(OrderPageLocators.COLOUR_FIELD)
        self.add_text_to_element(OrderPageLocators.COMMENT_INPUT_FIELD, comment)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)
        self.click_on_element(OrderPageLocators.YES_BUTTON)

    @allure.step('Проверка создания заказа')
    def check_order(self, locator):
        return self.get_text_from_element(locator)

    @allure.step('Проверка соответствия текущего URL ожидаемому')
    def check_url(self, expected_url):
        return self.driver.current_url == expected_url

    @allure.step('Клик по ячейке календаря с индексом {cell_index}')
    def click_on_the_specific_cell_of_calendar(self, cell_index):
        self.click_on_element(OrderPageLocators.DATE_INPUT_FIELD)
        formatted_specific_cell = self.format_locators(OrderPageLocators.CALENDAR_DAY, cell_index)
        self.click_on_element(formatted_specific_cell)