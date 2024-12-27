from selenium.webdriver.common.by import By

class MainPageLocators:
    HEADER_ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')
    DELIVERY_STEPS_SECTION_ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM')
    TEXT_IN_ANSWER = (By.CLASS_NAME, 'accordion__panel')
    #TITLE_OF_SECTION_QUESTIONS_ABOUT_IMPORTANT_THINGS = (By.XPATH, '//div[@class="Home_SubHeader__zwi_E"][4]')

    @staticmethod
    def question_number(question):
        return By.XPATH, f'/html/body/div/div/div/div[5]/div[2]/div/div[{question}]'