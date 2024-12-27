import pytest
from selenium import webdriver
from curl import main_site

@pytest.fixture (scope='function')
def driver():
    # Инициализация веб-драйвера
    driver = webdriver.Firefox()
    driver.get(main_site)
    yield driver
    driver.quit()