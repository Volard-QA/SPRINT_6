import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.base_page_locators import BasePageLocators

class OrderPage(BasePage):

    @allure.step("Клик по кнопке Заказать в шапке")
    def click_order_button_in_header(self):
        self.click_on_element(BasePageLocators.HEADER_ORDER_BUTTON)

    @allure.step("Клик по кнопке Заказать под разделом с описанием этапов доставки")
    def click_order_button_under_delivery_steps_section(self):
        self.scroll_to_element(BasePageLocators.DELIVERY_STEPS_SECTION_ORDER_BUTTON)
        self.click_on_element(BasePageLocators.DELIVERY_STEPS_SECTION_ORDER_BUTTON)
        self.wait_for_order_page_load()

    @allure.step("Клик по логотипу Самокт в шапке")
    def click_logo_scooter(self):
        self.click_on_element(BasePageLocators.HEADER_SCOOTER_LOGO_LINK)
        self.wait_for_main_page_load()


    @allure.step("Клик по логотипу Яндекс в шапке")
    def click_logo_yandex(self):
        self.click_on_element(BasePageLocators.HEADER_YANDEX_LOGO_LINK)
        self.wait_for_dzen_page_load()

    @allure.step("Заполнение полей формы Для кого самокат")
    def fill_data_into_fields_in_for_whom_scooter_form(self, name, surname, address, phone):
        self.click_on_element(BasePageLocators.COOKIE_ACCEPT_BUTTON)
        self.insert_keys_into_input(OrderPageLocators.NAME_FIELD,name)
        self.insert_keys_into_input(OrderPageLocators.SURNAME_FIELD,surname)
        self.insert_keys_into_input(OrderPageLocators.ADDRESS_FIELD, address)
        self.click_on_element(OrderPageLocators.METRO_FIELD)
        self.click_on_element(OrderPageLocators.METRO_FIELD_IN_FOCUS)
        self.insert_keys_into_input(OrderPageLocators.PHONE_FIELD, phone)
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнение полей формы Про аренду")
    def fill_data_into_fields_in_form_about_rent(self, comm):
        self.click_on_element(OrderPageLocators.DATE_FIELD)
        self.click_on_element(OrderPageLocators.NEXT_MONTH_BUTTON)
        self.click_on_element(OrderPageLocators.DAY_VALUE)
        self.click_on_element(OrderPageLocators.PERIOD_FIELD)
        self.click_on_element(OrderPageLocators.OPTION_PERIOD_FIELD)
        self.insert_keys_into_input(OrderPageLocators.COMM_FIELD,comm)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтверждение заказа")
    def click_yes_button_in_submit_order_form(self):
        self.click_on_element(OrderPageLocators.YES_BUTTON_IN_SUBMIT_ORDER_FORM)

    @allure.step("Получение текста кнопки просмотра статуса заказа в окне успешного оформления заказа")
    def check_title_text_for_order_status_button(self):
        try:
            self.wait_element(OrderPageLocators.TEXT_IN_ORDER_STATUS_BUTTON)
            return self.get_text_in_element(OrderPageLocators.TEXT_IN_ORDER_STATUS_BUTTON)
        except Exception as e:
            print(f"Ошибка: {e}")
            return None
