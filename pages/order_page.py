import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):

    @allure.step("Заполнение полей формы Для кого самокат")
    def fill_data_into_fields_in_for_whom_scooter_form(self, name, surname, address, metro, phone):
        self.insert_keys_into_input(OrderPageLocators.NAME_FIELD,name)
        self.insert_keys_into_input(OrderPageLocators.SURNAME_FIELD,surname)
        self.insert_keys_into_input(OrderPageLocators.ADDRESS_FIELD, address)
        self.insert_keys_into_input(OrderPageLocators.METRO_FIELD, metro)
        self.insert_keys_into_input(OrderPageLocators.PHONE_FIELD, phone)
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнение полей формы Про аренду")
    def fill_data_into_fields_in_form_about_rent(self, data, comm):
        self.insert_keys_into_input(OrderPageLocators.DATA_FIELD,data)
        self.click_on_element(OrderPageLocators.PERIOD_FIELD)
        self.click_on_element(OrderPageLocators.OPTION_PERIOD_FIELD)
        self.insert_keys_into_input(OrderPageLocators.COMM_FIELD,comm)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтверждение заказа")
    def click_yes_button_in_submit_order_form(self):
        self.wait_element(OrderPageLocators.YES_BUTTON_IN_SUBMIT_ORDER_FORM)
        self.click_on_element(OrderPageLocators.YES_BUTTON_IN_SUBMIT_ORDER_FORM)

    @allure.step("Ожидание появления окна с подтвержденным заказом")
    def wait_for_window_with_order_information(self):
        self.wait_element(OrderPageLocators.TITLE_OF_SUCCESSFUL_ORDER_WINDOW)

