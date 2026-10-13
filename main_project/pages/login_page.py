from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main_project.base.base_class import Base


class Login_page(Base):
    """Класс, содержащий локаторы и методы для страницы Авторизации."""

    # Базовый URL сайта.
    # В тестах может потребоваться переопределить на конкретный URL страницы входа (например, '/login').
    url = 'https://upstore24.ru/'

    def __init__(self,driver):
        self.driver = driver
        """
        Инициализация страницы авторизации.

        :param driver: Экземпляр WebDriver.
        """
        super().__init__(self.driver)

        # Инициализация явного ожидания с таймаутом 30 секунд
        self.wait = WebDriverWait(self.driver, 30)

    # Locators

    user_icon = '(//span[@data-icon="user"])[1]'
    user_email = '//*[@id="input-15"]'
    button_continue = '//button[@type="button"]'
    password = '//input[@type="password"]'
    button_enter = '//button[normalize-space()="Войти"]'

    # Getters


    def get_button_enter(self):
        """Возвращает кликабельный элемент кнопки 'Войти'."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_enter)))

    def get_password(self):
        """Возвращает кликабельное поле ввода пароля."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_user_icon(self):
        """Возвращает кликабельную иконку пользователя для открытия формы входа."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.user_icon)))

    def get_user_email(self):
        """Возвращает кликабельное поле ввода email."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.user_email)))

    def get_button_continue(self):
        """Возвращает кликабельную кнопку 'Продолжить' (после ввода email)."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_continue)))

    # Actions


    def click_button_enter(self):
        """Выполняет клик по кнопке 'Войти'."""
        self.get_button_enter().click()
        print('click enter')

    def click_user_icon(self):
        """Кликает по иконке пользователя, чтобы открыть форму авторизации."""
        self.get_user_icon().click()
        print("Click icon user")

    def input_user_email(self, email):
        """
        Вводит email в поле авторизации.

        :param email: Строка с адресом электронной почты.
        """
        self.get_user_email().send_keys(email)
        print("Input email")

    def click_go(self):
        """Кликает по кнопке 'Продолжить' после ввода email."""
        self.get_button_continue().click()
        print('click go')

    def input_password(self, password):
        """
        Вводит пароль в соответствующее поле.

        :param password: Строка с паролем.
        """
        self.get_password().send_keys(password)
        print("Input password")

    # Method


    def authorization(self):
        """
        Выполняет полную последовательность авторизации на сайте:
        1. Открывает главную страницу.
        2. Максимизирует окно браузера.
        3. Кликает по иконке пользователя.
        4. Вводит жестко заданный email.
        5. Нажимает кнопку продолжения.
        6. Вводит жестко заданный пароль.
        7. Нажимает кнопку входа.
        Метод только имитирует вход в личный кабинет, так как проект учебный
        """
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_user_icon()
        self.input_user_email('ragobom@ogzmail.com')
        self.click_go()
        self.input_password('*****')
        self.click_button_enter()

        self.get_screenshot()