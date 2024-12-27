import pytest
from selenium import webdriver
@pytest.fixture (scope='function')
def driver():
    # Инициализация веб-драйвера
    driver = webdriver.Firefox()
    driver.get("")
    yield driver
    driver.quit()