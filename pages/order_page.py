from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import data
import allure


class OrderPage(BasePage):


    @allure.step('Открытие страницы заказа через верхнюю кнопку')
    def open_order_page_top(self):
        self.open_page(data.MAIN_PAGE_URL)
        self.accept_cookies(OrderPageLocators.ACCEPT_COOKIE_BUTTON)
        self.click_on_element(OrderPageLocators.ORDER_TOP_BUTTON)

    @allure.step('Открытие страницы заказа через нижнюю кнопку')
    def open_order_page_bottom(self):
        self.open_page(data.MAIN_PAGE_URL)
        self.accept_cookies(OrderPageLocators.ACCEPT_COOKIE_BUTTON)
        self.click_on_element(OrderPageLocators.ORDER_BOTTOM_BUTTON)


    @allure.step('Создание заказа')
    def set_order(self, name, surname, address, metro_station_index, phone, cell, comment):
        self.add_text_to_element(OrderPageLocators.NAME_INPUT_FIELD, name)
        self.add_text_to_element(OrderPageLocators.SURNAME_INPUT_FIELD, surname)
        self.add_text_to_element(OrderPageLocators.ADDRESS_INPUT_FIELD, address)
        #self.click_on_element(OrderPageLocators.METRO_STATION_INPUT_FIELD)
        self.select_metro_station(metro_station_index)
        self.add_text_to_element(OrderPageLocators.PHONE_INPUT_FIELD, phone)
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)
        self.click_on_the_specific_cell_of_calendar(cell)
        self.click_on_element(OrderPageLocators.DROPDOWN_FIELD)
        self.click_on_element(OrderPageLocators.DROPDOWN_MENU)
        self.click_on_element(OrderPageLocators.COLOUR_FIELD)
        self.add_text_to_element(OrderPageLocators.COMMENT_INPUT_FIELD, comment)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)
        self.click_on_element(OrderPageLocators.YES_BUTTON)

    @allure.step('Выбор станции метро по локатору')
    def select_metro_station(self, index):
        """Выбор метропункта по индексу (или любому другому критерию)."""
        metro_stations = [
            OrderPageLocators.METRO_STATION_1,
            OrderPageLocators.METRO_STATION_2,
        ]
        if index < len(metro_stations):
            self.click_on_element(OrderPageLocators.METRO_STATION_INPUT_FIELD)
            self.click_on_element(metro_stations[index])  # Выбор нужного локатора по индексу
        else:
            raise ValueError("Индекс станции метро вне допустимого диапазона.")

    @allure.step('Проверка создания заказа')
    def check_order(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_DONE)


    @allure.step('Клик по ячейке календаря с индексом {cell_index}')
    def click_on_the_specific_cell_of_calendar(self, cell_index):
        self.click_on_element(OrderPageLocators.DATE_INPUT_FIELD)
        formatted_specific_cell = self.format_locators(OrderPageLocators.CALENDAR_DAY, cell_index)
        self.click_on_element(formatted_specific_cell)

    @allure.step('Клик по кнопке статуса')
    def click_on_status_button(self):
        self.click_on_element(OrderPageLocators.STATUS_BUTTON)

    @allure.step('Клик по логотипу яндекс')
    def click_on_yandex_button(self):
        self.click_on_element(OrderPageLocators.YANDEX_LOGO)

    @allure.step('Клик по логотипу самоката')
    def click_on_scooter_button(self):
        self.click_on_element(OrderPageLocators.SCOOTER_LOGO)
