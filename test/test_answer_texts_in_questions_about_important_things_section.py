import allure
import pytest
import data
from pages.main_page import MainPage

class TestAnswersForQuestionsInQuestionAboutImportantThingsSection:
    @allure.title("Проверка текстов ответов на вопросы в секции Вопросы о важном")
    @pytest.mark.parametrize('answer_number, expected_answer', data.Answers.answers_text)
    def test_answers_texts(self,driver,answer_number, expected_answer):
        main_page = MainPage(driver)
        main_page.click_question_in_questions_about_important_things_section(answer_number)
        main_page.check_answer_text_in_question(expected_answer)