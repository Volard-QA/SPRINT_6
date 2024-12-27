from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_FIELD = (By.XPATH, '//div[@class="Input_InputContainer__3NykH"]//input[@placeholder="* Имя"]')
    SURNAME_FIELD =(By.XPATH, '//div[@class="Input_InputContainer__3NykH"]//input[@placeholder="* Фамилия"]')
    ADDRESS_FIELD = (By.XPATH, '//div[@class="Input_InputContainer__3NykH"]//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_FIELD = (By.XPATH, '//div[@class="select-search__value"]//input[@placeholder="* Станция метро"]')
    PHONE_FIELD = (By.XPATH, '//div[@class="Input_InputContainer__3NykH"]//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM')
    DATA_FIELD = (By.XPATH, '//div[@class="react-datepicker__input-container"]//input[@placeholder="* Когда привезти самокат"]')
    PERIOD_FIELD = (By.XPATH, '//div[@class="Dropdown-root Order_FilledDate__1pb8n"]//div[@class="Dropdown-control"]')
    OPTION_PERIOD_FIELD = (By.XPATH, f'//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[3]')
    COMM_FIELD = (By.XPATH, '//div[@class="Input_InputContainer__3NykH"]//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]//button[@class="Button_Button__ra12g Button_Middle__1CSJM"][2]')
    YES_BUTTON_IN_SUBMIT_ORDER_FORM = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]//button[@class="Button_Button__ra12g Button_Middle__1CSJM"][4]')
    TITLE_OF_SUCCESSFUL_ORDER_WINDOW = (By.XPATH, '//div[@class="Order_Modal__YZ-d3"]//div[@class="Order_ModalHeader__3FDaJ"]')
