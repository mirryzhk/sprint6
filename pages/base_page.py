from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы по URL')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Принятие кук')
    def accept_cookies(self, locator):
        self.click_on_element(locator)

    @allure.step('Найти элемент с ожиданием')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Добавление текста в элемент')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получение текста из элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Форматирование локатора')
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator

    @allure.step('Переключение на следующую вкладку с ожидаемым URL')
    def switch_to_next_tab(self, url):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 5).until(EC.url_to_be(url))
