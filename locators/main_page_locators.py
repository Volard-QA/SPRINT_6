from selenium.webdriver.common.by import By

class MainPageLocators:

    TEXT_IN_ANSWER = (By.CLASS_NAME, 'accordion__panel')

    @staticmethod
    def question_number(question):
        return By.XPATH, f'/html/body/div/div/div/div[5]/div[2]/div/div[{question}]'

    @staticmethod
    def answer_number(answer):
        return By.XPATH, f'/html/body/div/div/div/div[5]/div[2]/div/div[{answer}]/div[2]'