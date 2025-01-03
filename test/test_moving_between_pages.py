import allure
from curl import *
from pages.order_page import OrderPage

class TestMovingToMainPageWithLogoScooterInHeader:
    @allure.title("Проверка успешного перехода на главную страницу кликом по логотипу Самокат в шапке")
    @allure.description("Из формы заказа кликаем по логотипу Самокат в шапке и проверяем, что попадаем на главную страницу приложения")
    def test_moving_to_main_page_with_scooter_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.click_order_button_in_header()
        order_page.click_logo_scooter()
        assert driver.current_url == main_site

class TestMovingToYandexDzenPageWithLogoYandexInHeader:
    @allure.title("Проверка успешного перехода на страницу Яндекс Дзена кликом по логотипу Яндекс в шапке")
    @allure.description("Проверяем переход на отдельную страницу яндекс Дзена при клике по логотипу Яндекс в шапке приложения")
    def test_moving_to_dzen_page_with_yandex_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.click_order_button_in_header()
        order_page.click_logo_yandex()
        assert driver.current_url == dzen_page_url

class TestMovingToOrderPageWithOrderButtonUnderDeliveryStepsSection:
    @allure.title("Проверка успешного перехода на страницу оформления заказа кликом по кнопке Заказать под секцией этапов доставки")
    @allure.description("На главной странице ищем кнопку Заказать и проверяем, что при клике по ней попадаем на страницу формирования заказа")
    def test_moving_to_order_page_with_button_order_under_delivery_steps_section(self, driver):
        order_page = OrderPage(driver)
        order_page.click_order_button_under_delivery_steps_section()
        assert driver.current_url == order_url