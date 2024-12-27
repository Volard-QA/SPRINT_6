import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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

    @allure.step("Подождать и проверить, что элемент содержит определенный текст")
    def wait_for_text_atribut(self, locator,attribute, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, value)
        )

    @allure.step("Выбрать одно из значений выпадающего списка")
    def chose_one_option_of_list(self,locator, option_text, timeout=10):
        option = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@class='Dropdown-option' and text()='{option_text}']"))
        )