from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main_project.base.base_class import Base
from main_project.pages.main_page import Main_page


class Heart_page(Base):
    """
    Класс, содержащий локаторы и методы для страницы 'Избранное' (Wishlist/Heart).
    Наследуется от базового класса Base.
    """

    def __init__(self, driver):
        """
        Инициализация страницы избранного.

        :param driver: Экземпляр WebDriver.
        """
        super().__init__(driver)
        self.driver = driver
        # Инициализация явного ожидания с таймаутом 30 секунд
        self.wait = WebDriverWait(self.driver, 30)

    # Локаторы (Locators)
    # XPath-выражения для поиска элементов на странице избранного.
    # Индексы [1] и [2] указывают на первый и второй элементы в списке товаров.
    alert_info = '//*[@class="alert-info__text"]'
    product_card_title_heart = '(//*[@class="product-card__title"])[1]'
    product_card_title_heart_1 = '(//*[@class="product-card__title"])[2]'
    card_price_from_heart = '(//*[@data-product-card-price-from-cart])[1]'
    card_price_from_heart_1 = '(//*[@data-product-card-price-from-cart])[2]'

    # Геттеры (Getters)
    # Методы для получения текста из элементов с использованием явного ожидания.

    def get_product_card_title_heart(self):
        """Возвращает название первого товара в избранном."""
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.product_card_title_heart))
        ).text

    def get_product_card_title_heart_1(self):
        """Возвращает название второго товара в избранном."""
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.product_card_title_heart_1))
        ).text

    def get_alert_info(self):
        """Возвращает текст информационного сообщения (алерта) на странице."""
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.alert_info))
        ).text

    def get_card_price_from_heart(self):
        """Возвращает цену первого товара в избранном."""
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.card_price_from_heart))
        ).text

    def get_card_price_from_heart_1(self):
        """Возвращает цену второго товара в избранном."""
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.card_price_from_heart_1))
        ).text

    # Проверки (Assertions)
    # Методы для валидации данных. Используют assert для прерывания теста при ошибке.

    def assert_alert_info(self):
        """
        Проверяет наличие и текст информационного сообщения об ограничении
        количества товаров в избранном (не более 20).
        """
        assert self.get_alert_info() == 'Обратите внимание! Добавить в избранное можно не более 20 товаров. Чтобы сохранить подборку, авторизуйтесь в личном кабинете.'
        print("Вы на странице избранное\n")

    def assert_card_price_from_heart(self, price):
        """
        Проверяет цену первого товара.
        Внимание: в теле метода используется геттер второго товара (get_card_price_from_heart_1).
        Это может быть логической ошибкой, если предполагалась проверка первого товара.
        """
        assert self.get_card_price_from_heart_1() == price
        print(
            f"Цена на товар 1 с главной страницы - {price} совпадает с ценой товара на странице избранного - {self.get_card_price_from_heart_1()} success\n")

    def assert_card_price_from_heart_1(self, price_1):
        """
        Проверяет цену второго товара.
        Внимание: в теле метода используется геттер первого товара (get_card_price_from_heart).
        Это может быть логической ошибкой, если предполагалась проверка второго товара.
        """
        assert self.get_card_price_from_heart() == price_1
        print(
            f"Цена на товар 2 с главной страницы - {price_1} совпадает с ценой товара на странице избранного - {self.get_card_price_from_heart()} success\n")

    def click_toolbar_compare(self):
        """
        Переход на страницу сравнения товаров через шапку сайта.
        Создает экземпляр главной страницы и вызывает метод клика по кнопке сравнения.
        """
        mp = Main_page(self.driver)
        mp.click_toolbar_compare()
        print("Click toolbar compare\n")

    def assert_product_heart(self, prod):
        """
        Проверяет название первого товара.
        Внимание: в теле метода используется геттер второго товара (get_product_card_title_heart_1).
        Это может быть логической ошибкой, если предполагалась проверка первого товара.
        """
        assert self.get_product_card_title_heart_1() == prod
        print(
            f"выбранный товар 1 - {self.get_product_card_title_heart_1()} с главной страницы совпадает с выбранным товаром на странице избранного - {prod} success\n")

    def assert_product_heart_1(self, prod_1):
        """
        Проверяет название второго товара.
        Внимание: в теле метода используется геттер первого товара (get_product_card_title_heart).
        Это может быть логической ошибкой, если предполагалась проверка второго товара.
        """
        assert self.get_product_card_title_heart() == prod_1
        print(
            f"выбранный товар 2 - {self.get_product_card_title_heart()} с главной страницы совпадает с выбранным товаром на странице избранного - {prod_1} success\n")

    # Сценарный метод (Composite Action)
    # Объединяет последовательность действий в один вызов для тест-кейса.

    def assert_heart_page(self, price, price_1, prod, prod1):
        """
        Выполняет полную проверку страницы избранного: URL, алерт, названия и цены товаров,
        а затем переходит на страницу сравнения.

        :param price: Ожидаемая цена (проверяется вторым товаром из-за ошибки в коде).
        :param price_1: Ожидаемая цена (проверяется первым товаром из-за ошибки в коде).
        :param prod: Ожидаемое название (проверяется вторым товаром из-за ошибки в коде).
        :param prod1: Ожидаемое название (проверяется первым товаром из-за ошибки в коде).
        """
        self.get_current_url()
        self.assert_alert_info()
        self.assert_product_heart(prod)
        self.assert_product_heart_1(prod1)
        self.assert_card_price_from_heart(price)
        self.assert_card_price_from_heart_1(price_1)
        self.click_toolbar_compare()
        bc = Base(self.driver)
        bc.get_screenshot()