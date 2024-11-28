from selenium.webdriver.common.by import By

class MainPageLocators:

    QUESTION_LOCATOR = By.ID, 'accordion__heading-{}'
    QUESTION_LOCATOR_LAST = By.ID, 'accordion__heading-7'
    QUESTION_LOCATOR_FIRST = By.ID, 'accordion__heading-0'
    ANSWER_LOCATOR = By.ID, 'accordion__panel-{}'
    ACCEPT_COOKIE_BUTTON = By.ID, 'rcc-confirm-button'

