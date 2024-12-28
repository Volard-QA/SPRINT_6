import allure
import pytest
import data
from pages.order_page import OrderPage

class TestSuccessfulProcessOrderingScooter:
    @allure.title("Проверка сценария успешного заказа самоката")
    @allure.description("На главной странице кликаем по кнопке Заказать в шапке приложения и заполняем поля формы заказа валидными данными, проверяя в конце, что открылось окно с успешной регистрацией заказа")
    @pytest.mark.parametrize('name, surname, address, phone, comm', data.OrderFields.order_fields)
    def test_successful_ordering_scooter_flow(self, driver, name, surname, address, phone, comm):
        order_page = OrderPage(driver)
        order_page.click_order_button_in_header()
        order_page.fill_data_into_fields_in_for_whom_scooter_form(name, surname, address, phone)
        order_page.fill_data_into_fields_in_form_about_rent(comm)
        order_page.click_yes_button_in_submit_order_form()
        assert order_page.check_title_text_for_order_status_button() == 'Посмотреть статус'
