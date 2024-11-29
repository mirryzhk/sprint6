import data
import allure
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка успешного оформления заказа и перехода на главную страницу')
    @allure.description('Проверка создания заказа через верхнюю кнопку Заказать и клика по лого самоката для проверки перехода на главную страницу.')
    def test_making_order_then_click_on_scooter_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page_top()
        order_page.set_order(
            data.NAME_1,
            data.SURNAME_1,
            data.ADDRESS_1,
            0,
            data.PHONE_1,
            data.CELL_1,
            data.COMMENT_1
        )
        order_done_text = order_page.check_order()
        assert data.SUCCESS_ORDER_TEXT in order_done_text
        order_page.click_on_status_button()
        order_page.click_on_scooter_button()
        assert order_page.check_url(data.MAIN_PAGE_URL)

    @allure.title('Проверка успешного оформления заказа и перехода на страницу Дзена')
    @allure.description('Проверка создания заказа через нижнюю кнопку Заказать и клика по лого Яндекса для проверки перехода на страницу Дзен.')
    def test_making_order_then_click_on_yandex_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page_bottom()
        order_page.set_order(
            data.NAME_2,
            data.SURNAME_2,
            data.ADDRESS_2,
            0,
            data.PHONE_2,
            data.CELL_2,
            data.COMMENT_2
        )
        order_done_text = order_page.check_order()
        assert data.SUCCESS_ORDER_TEXT in order_done_text
        order_page.click_on_status_button()
        order_page.click_on_yandex_button()
        order_page.switch_to_next_tab(data.DZEN_URL)
        assert order_page.check_url(data.DZEN_URL)