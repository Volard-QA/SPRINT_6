import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from curl import *

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидать видимость элемента")
    def wait_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Скролл до нужного элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть по элементу")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_element(locator, timeout)
        element.click()

    @allure.step("Ввести текст в поле")
    def insert_keys_into_input(self, locator, keys, timeout=10):
        element = self.wait_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст из элемента")
    def get_text_in_element(self, locator, timeout=10):
        element = self.wait_element(locator, timeout)
        return element.text

    @allure.step("Ожидание прогрузки главной страницы")
    def wait_for_main_page_load(self, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(main_site))

    @allure.step("Ожидание прогрузки страницы оформления заказа")
    def wait_for_order_page_load(self, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(order_url))

    @allure.step("Ожидание прогрузки страницы Дзен")
    def wait_for_dzen_page_load(self, timeout=10):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(dzen_page_url))
