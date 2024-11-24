from selenium.webdriver.common.by import By


class OrderPageLocators:

    # Форма заказа часть №1
    NAME_INPUT_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_1 = (By.XPATH, '//li[4]')
    METRO_STATION_2 = (By.XPATH, '//li[9]')
    PHONE_INPUT_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(),'Далее')]")

    # Форма заказа часть №2
    DATE_INPUT_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    CALENDAR_MENU = (By.XPATH, "//div[contains(@class, 'react-datepicker__day')]")
    CALENDAR_DAY = (By.XPATH, "(//div[contains(@class, 'react-datepicker__day')])[{}]")
    DROPDOWN_FIELD = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    DROPDOWN_MENU = (By.XPATH, "//div[@class='Dropdown-menu']//div[2]")
    COLOUR_FIELD = (By.XPATH, "//label[contains(text(),'чёрный жемчуг')]")
    COMMENT_INPUT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    YES_BUTTON = (By.XPATH, "//button[contains(text(),'Да')]")

    # Окно "Заказ оформлен"
    ORDER_DONE = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
    STATUS_BUTTON = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]")

    # Логотипы на странице
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")