import data
import allure
import pytest
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators


class TestOrderPage:

    @allure.title('Проверка успешного оформления заказа и перехода на главную страницу')
    @allure.description('Проверка создания заказа через верхнюю кнопку Заказать и клика по лого самоката для проверки перехода на главную страницу.')
    def test_making_order_then_click_on_scooter_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.open_to_order_page(MainPageLocators.ORDER_TOP_BUTTON)
        order_page.set_order(
            data.NAME_1,
            data.SURNAME_1,
            data.ADDRESS_1,
            OrderPageLocators.METRO_STATION_1,
            data.PHONE_1,
            data.CELL_1,
            data.COMMENT_1
        )
        order_done_text = order_page.check_order(OrderPageLocators.ORDER_DONE)
        assert data.SUCCESS_ORDER_TEXT in order_done_text
        order_page.click_on_element(OrderPageLocators.STATUS_BUTTON)
        order_page.click_on_element(OrderPageLocators.SCOOTER_LOGO)
        assert order_page.check_url(data.MAIN_PAGE_URL)

    @allure.title('Проверка успешного оформления заказа и перехода на страницу Дзена')
    @allure.description('Проверка создания заказа через нижнюю кнопку Заказать и клика по лого Яндекса для проверки перехода на страницу Дзен.')
    def test_making_order_then_click_on_yandex_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.open_to_order_page(MainPageLocators.ORDER_BOTTOM_BUTTON)
        order_page.set_order(
            data.NAME_2,
            data.SURNAME_2,
            data.ADDRESS_2,
            OrderPageLocators.METRO_STATION_2,
            data.PHONE_2,
            data.CELL_2,
            data.COMMENT_2
        )
        order_done_text = order_page.check_order(OrderPageLocators.ORDER_DONE)
        assert data.SUCCESS_ORDER_TEXT in order_done_text
        order_page.click_on_element(OrderPageLocators.STATUS_BUTTON)
        order_page.click_on_element(OrderPageLocators.YANDEX_LOGO)
        order_page.switch_to_next_tab(data.DZEN_URL)
        assert order_page.check_url(data.DZEN_URL)