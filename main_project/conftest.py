import time
import pytest
from selenium import webdriver


@pytest.fixture()
def set_up():
    print("Start test")
    yield
    print("\nFinish test")



@pytest.fixture(scope='module')
def set_group():
    print('\n'"Enter system")
    yield
    print('\n'"Exit system")