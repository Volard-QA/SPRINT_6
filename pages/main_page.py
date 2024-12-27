import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    @allure.step("Клик по кнопке Заказать в шапке")
    def click_order_button_in_header(self):
        self.click_on_element(MainPageLocators.HEADER_ORDER_BUTTON)

    @allure.step("Клик по кнопке Заказать под разделом с описанием этапов доставки")
    def click_order_button_under_delivery_steps_section(self):
       self.click_on_element(MainPageLocators.DELIVERY_STEPS_SECTION_ORDER_BUTTON)

    #@allure.step("Ожидание появления заголовка секции Вопросы о важном")
    #def wait_for_title_questions_about_important_things(self):
    #    self.wait_element(MainPageLocators.TITLE_OF_SECTION_QUESTIONS_ABOUT_IMPORTANT_THINGS)

    @allure.step("Выбор вопроса в разделе Вопросы о важном на главной странице")
    def click_question_in_questions_about_important_things_section(self, question_number):
        question_locator = MainPageLocators.question_number(question_number)
        self.scroll_to_element(question_locator)
        self.click_on_element(question_locator)

    @allure.step("Сравнение текста выбранного вопроса в разделе Вопросы о важном")
    def check_answer_text_in_question(self, expected_text):
        actual_text = self.get_text_in_element(MainPageLocators.TEXT_IN_ANSWER)
        return actual_text == expected_text
