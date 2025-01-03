from selenium.webdriver.common.by import By

class MainPageLocators:

    TEXT_IN_ANSWER = (By.CLASS_NAME, 'accordion__panel')

    @staticmethod
    def question_number(question):
        return By.XPATH, f'//div[@class="accordion__item"][{question}]'

    @staticmethod
    def answer_number(answer):
        return By.XPATH, f'//div[@class="accordion__item"][{answer}]/div[@class="accordion__panel"]'