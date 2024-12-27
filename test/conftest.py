import pytest
import sys
import os
from selenium import webdriver
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from curl import main_site

@pytest.fixture (scope='function')
def driver():
    # Инициализация веб-драйвера
    driver = webdriver.Firefox()
    driver.get(main_site)
    yield driver
    driver.quit()