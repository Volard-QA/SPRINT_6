import allure
import pytest
import data
from pages.order_page import OrderPage

class TestSuccessfulProcessOrderingScooter:
    @allure.title("Проверка сценария успешного заказа самоката")
    @pytest.mark.parametrize('name, surname, address, phone, date, comm', data.OrderFields.order_fields)
    def test_successful_ordering_scooter_flou(self, driver, name, surname, address, phone, date, comm):
        order_page = OrderPage(driver)
        order_page.click_order_button_in_header()
        order_page.fill_data_into_fields_in_for_whom_scooter_form(name, surname, address, phone)
        order_page.fill_data_into_fields_in_form_about_rent(data, comm)
        order_page.click_yes_button_in_submit_order_form()

        assert order_page.wait_for_window_with_order_information()
