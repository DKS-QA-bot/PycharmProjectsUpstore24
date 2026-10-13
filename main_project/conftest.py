import pytest
from selenium import webdriver


@pytest.fixture()
def set_up():
    """Фикстура для отдельного теста."""
    print("Start test")

    yield

    print("\nFinish test")


@pytest.fixture(scope='module')
def set_group():
    """Общая фикстура."""
    print('\n'"Enter system")
    yield
    print('\n'"Exit system")

@pytest.fixture()
def driver():
    """Фикстура для создания и закрытия драйвера."""
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()