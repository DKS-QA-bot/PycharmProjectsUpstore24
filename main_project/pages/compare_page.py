
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main_project.base.base_class import Base
from main_project.pages.catalog_page import Catalog_page


class Compare_page(Base):
    """Класс, содержащий локаторы и методы для страницы сравнения товаров."""

    def __init__(self,driver):
        """
        Инициализация страницы сравнения.

        :param driver: Экземпляр WebDriver.
        """
        self.driver = driver
        super().__init__(self.driver)

        self.wait = WebDriverWait(self.driver, 30)

    # Locators

    button_similar = '//*[@class="form-element__toggle"]'
    compare_product_title = '(//*[@class="compare__product-title"])[1]'
    compare_product_title_1 = '(//*[@class="compare__product-title"])[2]'
    compare_product_price = '(//*[@class="compare__product-price"])[1]'
    compare_product_price_1 = '(//*[@class="compare__product-price"])[2]'

    # Getters


    def get_compare_product_price(self):
        """
        Возвращает текст цены первого товара в таблице сравнения.
        :return: str
        """
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.compare_product_price))).text

    def get_compare_product_price_1(self):
        """
        Возвращает текст цены второго товара в таблице сравнения.

        :return: str
        """
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.compare_product_price_1))
        ).text

    def get_button_similar(self):
        """
        Возвращает кликабельный элемент кнопки 'Показать похожие'.

        :return: WebElement
        """
        return self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.button_similar))
        )

    def get_compare_product_title(self):
        """
        Возвращает название первого товара в таблице сравнения.

        :return: str
        """
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.compare_product_title))
        ).text

    def get_compare_product_title_1(self):
        """
        Возвращает название второго товара в таблице сравнения.

        :return: str
        """
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.compare_product_title_1))
        ).text

    # Actions
    def assert_product(self, prod):
        """
        Проверяет, что название второго товара в таблице совпадает с ожидаемым.

        :param prod: Ожидаемое название второго товара.
        """
        assert self.get_compare_product_title_1() == prod
        print(
            f"выбранный товар 1 - {self.get_compare_product_title_1()} с главной страницы "
            f"совпадает с выбранным товаром на странице сравнения товаров - {prod} success\n"
        )

    def assert_product_1(self, prod1):
        """
        Проверяет, что название первого товара в таблице совпадает с ожидаемым.

        :param prod1: Ожидаемое название первого товара.
        """
        print(self.get_compare_product_title(), prod1)
        assert self.get_compare_product_title() == prod1
        print(
            f"выбранный товар 2 - {self.get_compare_product_title()} с главной страницы "
            f"совпадает с выбранным товаром на странице сравнения товаров - {prod1} success\n"
        )

    def click_button_similar(self):
        """
        Кликает по кнопке 'Показать похожие' для поиска аналогичных товаров.
        """
        self.get_button_similar().click()
        print("Click button similar")

    def assert_compare_product_price(self, price):
        """
        Проверяет, что цена второго товара в таблице совпадает с ожидаемой.

        :param price: Ожидаемая цена второго товара.
        """
        assert self.get_compare_product_price_1() == price
        print(
            f"Цена на товар 1 - {self.get_compare_product_price_1()} с главной страницы "
            f"совпадает с ценой товара на странице сравнения товаров - {price} success\n"
        )

    def assert_compare_product_price_1(self, price_1):
        """
        Проверяет, что цена первого товара в таблице совпадает с ожидаемой.

        :param price_1: Ожидаемая цена первого товара.
        """
        assert self.get_compare_product_price() == price_1
        print(
            f"Цена на товар 2 - {self.get_compare_product_price()} с главной страницы "
            f"совпадает с ценой на товар на странице сравнения товаров - {price_1} success\n"
        )

    # Method

    def product_compare(self, prod, prod1, price, price_1):
        """
        Выполняет полную проверку страницы сравнения: URL, названия товаров,
        нажатие на кнопку похожих, проверку цен, создание скриншота
        и переход в корзину.

        :param prod: Ожидаемое название второго товара.
        :param prod1: Ожидаемое название первого товара.
        :param price: Ожидаемая цена второго товара.
        :param price_1: Ожидаемая цена первого товара.
        """
        self.get_current_url()
        self.assert_product(prod)
        self.assert_product_1(prod1)
        self.click_button_similar()
        self.assert_compare_product_price(price)
        self.assert_compare_product_price_1(price_1)

        # Создание скриншота через базовый класс

        self.get_screenshot()

        # Переход в корзину через главную страницу
        mp = Catalog_page(self.driver)
        mp.click_toolbar_in_cart()

