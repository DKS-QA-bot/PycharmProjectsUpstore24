from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main_project.base.base_class import Base


class Cart_page(Base):
    """Класс, содержащий локаторы и методы для страницы 'Корзина'."""

    def __init__(self, driver):
        """
        Инициализация страницы корзины.

        :param driver: Экземпляр WebDriver.
        """
        super().__init__(driver)
        self.driver = driver
        # Инициализация явного ожидания с таймаутом 30 секунд
        self.wait = WebDriverWait(self.driver, 30)

    # Локаторы (Locators)
    # Используются относительные XPath-выражения для поиска элементов на странице.
    # Индексы [1] и [2] указывают на первый и второй элементы в списке соответственно.
    section_title_kart = '(//*[@class="section__title"])[1]'
    cart_item_title = '(//*[@class="cart-item__title"])[1]'
    cart_item_title_1 = '(//*[@class="cart-item__title"])[2]'
    cart_item_total_price = '(//*[@data-cart-item-total-price])[1]'
    cart_item_total_price_1 = '(//*[@data-cart-item-total-price])[2]'

    # Геттеры (Getters)
    # Методы для получения текста из элементов.
    # Используют явное ожидание видимости элемента перед обращением к .text.

    def get_cart_item_total_price_1(self):
        """Возвращает текст общей цены второго товара в корзине."""
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.cart_item_total_price_1))
        ).text

    def get_cart_item_total_price(self):
        """Возвращает текст общей цены первого товара в корзине."""
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.cart_item_total_price))
        ).text

    def get_section_title_kart(self):
        """Возвращает текст заголовка секции корзины."""
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.section_title_kart))
        ).text

    def get_cart_item_title(self):
        """Возвращает название первого товара в корзине."""
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.cart_item_title))
        ).text

    def get_cart_item_title_1(self):
        """Возвращает название второго товара в корзине."""
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.cart_item_title_1))
        ).text

    # Проверки (Assertions)
    # Методы для валидации данных на странице.
    # Используют assert для прерывания теста при несовпадении и print для логирования в консоль.

    def assert_section_title_kart(self):
        """
        Проверяет, что заголовок страницы соответствует слову 'Корзина'.
        Срез [:self.get_section_title_kart().rindex('а')+1] используется для отсечения
        возможных дополнительных слов в заголовке (например, 'Корзина товаров').
        """
        assert self.get_section_title_kart()[:self.get_section_title_kart().rindex('а') + 1] == "Корзина"
        print("Вы находитесь в корзине\n")

    def assert_cart(self, prod):
        """
        Проверяет соответствие названия первого товара в корзине ожидаемому значению.

        :param prod: Ожидаемое название первого товара.
        """
        assert self.get_cart_item_title() == prod
        print(
            f"Выбранный товар 1 - {self.get_cart_item_title()} с главной страницы совпадает с выбранным товаром 1 в корзине - {prod} success\n")

    def assert_cart_1(self, prod1):
        """
        Проверяет соответствие названия второго товара в корзине ожидаемому значению.

        :param prod1: Ожидаемое название второго товара.
        """
        assert self.get_cart_item_title_1() == prod1
        print(
            f"Выбранный товар 2 - {self.get_cart_item_title_1()} с главной страницы совпадает с выбранным товаром 2 в корзине - {prod1} success\n")

    def assert_price_cart(self, price):
        """
        Проверяет соответствие цены первого товара ожидаемому значению.

        :param price: Ожидаемая цена первого товара.
        """
        assert self.get_cart_item_total_price() == price
        print(
            f"Цена на товар 1 с главной страницы - {price} совпадает с ценой товара на странице корзины - {self.get_cart_item_total_price()} success\n")

    def assert_price_cart_1(self, price_1):
        """
        Проверяет соответствие цены второго товара ожидаемому значению.

        :param price_1: Ожидаемая цена второго товара.
        """
        assert self.get_cart_item_total_price_1() == price_1
        print(
            f"Цена на товар 2 с главной страницы - {price_1} совпадает с ценой товара на странице корзины - {self.get_cart_item_total_price_1()} success\n")

    # Сценарный метод (Composite Action)
    # Объединяет последовательность проверок в один вызов для удобства использования в тестах.

    def assert_product_cart(self, prod, prod1, price, price_1):
        """
        Выполняет полную проверку состояния корзины: URL, заголовок, названия товаров и их цены.

        :param prod: Ожидаемое название первого товара.
        :param prod1: Ожидаемое название второго товара.
        :param price: Ожидаемая цена первого товара.
        :param price_1: Ожидаемая цена второго товара.
        """
        self.get_current_url()
        self.assert_section_title_kart()
        self.assert_cart(prod)
        self.assert_cart_1(prod1)
        self.assert_price_cart(price)
        self.assert_price_cart_1(price_1)
        bc = Base(self.driver)
        bc.get_screenshot()