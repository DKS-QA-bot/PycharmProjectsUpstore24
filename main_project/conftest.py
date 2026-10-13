import time

import pytest
from selenium import webdriver


@pytest.fixture()
def set_up():
    print("Start test")
    # options = webdriver.ChromeOptions()
    # options.add_argument("--incognito")
    # driver = webdriver.Chrome(options=options)
    # url = 'https://www.saucedemo.com/'
    # driver.get(url)
    # driver.maximize_window()
    yield

    # driver.quit()
    print("Finish test")



@pytest.fixture(scope='module')
def set_group():
    print('\n'"Enter system")
    # options = webdriver.ChromeOptions()
    # options.add_argument("--incognito")
    # driver = webdriver.Chrome(options=options)
    # url = 'https://www.saucedemo.com/'
    # driver.get(url)
    # driver.maximize_window()
    yield

    # driver.quit()
    print('\n'"Exit system")