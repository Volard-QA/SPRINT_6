from selenium.webdriver.common.by import By

class BasePageLocators:
    DELIVERY_STEPS_SECTION_ORDER_BUTTON = (By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    HEADER_ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')
    HEADER_SCOOTER_LOGO_LINK = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR" and @href="/"]')
    HEADER_YANDEX_LOGO_LINK = (By.XPATH, '//a[@class="Header_LogoYandex__3TSOI" and @href="//yandex.ru"]')
    COOKIE_ACCEPT_BUTTON = (By.XPATH, '//button[@class="App_CookieButton__3cvqF" and @id="rcc-confirm-button"]')