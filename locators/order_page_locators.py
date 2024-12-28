from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_FIELD = (By.XPATH, '//div[@class="Input_InputContainer__3NykH"]//input[@placeholder="* Имя"]')
    SURNAME_FIELD =(By.XPATH, '//div[@class="Input_InputContainer__3NykH"]//input[@placeholder="* Фамилия"]')
    ADDRESS_FIELD = (By.XPATH, '//div[@class="Input_InputContainer__3NykH"]//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_FIELD = (By.XPATH, '//div[@class="select-search__value"]//input[@class="select-search__input"]')
    METRO_FIELD_IN_FOCUS = (By.XPATH, '//div[@class="select-search__select"]//ul[@class="select-search__options"]//li[@class="select-search__row" and @data-value="3"]')
    PHONE_FIELD = (By.XPATH, '//div[@class="Input_InputContainer__3NykH"]//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//div[@class="Order_NextButton__1_rCA"]//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    DATE_FIELD = (By.XPATH, '//div[@class="react-datepicker__input-container"]//input[@placeholder="* Когда привезти самокат"]')
    NEXT_MONTH_BUTTON = (By.XPATH, '//div[@class="react-datepicker"]//button[@class="react-datepicker__navigation react-datepicker__navigation--next"]')
    DAY_VALUE = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[5]/div[7]')
    PERIOD_FIELD = (By.XPATH, '//div[@class="Dropdown-root"]//div[@class="Dropdown-control"]')
    OPTION_PERIOD_FIELD = (By.XPATH, f'//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[3]')
    COMM_FIELD = (By.XPATH, '//div[@class="Input_InputContainer__3NykH"]//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    YES_BUTTON_IN_SUBMIT_ORDER_FORM = (By.XPATH, '//div[@class="Order_Modal__YZ-d3"]//div[@class="Order_Buttons__1xGrp"]//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    TEXT_IN_ORDER_STATUS_BUTTON = (By.XPATH, '//div[@class="Order_NextButton__1_rCA"]//button[@class="Button_Button__ra12g Button_Middle__1CSJM"][1]')
