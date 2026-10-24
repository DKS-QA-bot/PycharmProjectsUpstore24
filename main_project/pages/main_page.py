import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main_project.base.base_class import Base
from main_project.pages.catalog_page import Catalog_page
from main_project.pages.compare_page import Compare_page
from main_project.pages.heart_page import Heart_page
from main_project.utilites.logger import Logger


class Main_page(Base):
    """
    Класс Page Object для Главной страницы.
    Содержит методы для фильтрации товаров, добавления их в корзину/сравнение
    и проверки перехода на соответствующие страницы (Избранное, Сравнение).
    """

    def __init__(self,driver):

        self.driver = driver

        """
        Инициализация страницы.

        :param driver: Экземпляр WebDriver.
        """
        super().__init__(self.driver)
        self.wait = WebDriverWait(self.driver, 30)
        self.action = ActionChains(self.driver)

        # Инициализация других Page Objects для навигации
        self.hp = Heart_page(self.driver)  # Страница "Избранное"
        self.cmp = Compare_page(self.driver)  # Страница "Сравнение"
        self.cp = Catalog_page(self.driver)  # Страница "Каталог"

    # Locators


    in_cart_main = '(//*[@class="add-cart-counter__btn button button--primary button--block"])[1]'
    in_cart_main_1 = '(//*[@class="add-cart-counter__btn button button--primary button--block"])[2]'
    button_all_products = '(//*[@class="tabs__all-products"])[1]'
    button_up = '//*[@data-icon="chevron-up"]'
    color_burgundy = '//*[@for="filter-item-974079425"]'
    version = '//*[for="filter-item-251335371"]'
    icon_prod = '//*[@data-product-id="1917310689"]'
    icon_prod_1 = '//*[@data-product-id="1917318385"]'

    # Getters


    def get_icon_prod_1(self):
        """Возвращает кликабельную иконку добавления в корзину для второго товара."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.icon_prod_1)))

    def get_icon_prod(self):
        """Возвращает кликабельную иконку добавления в корзину для первого товара."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.icon_prod)))

    def get_in_cart_main_1(self):
        """Возвращает кнопку изменения количества/статуса в корзине для второго товара."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.in_cart_main_1)))

    def get_in_cart_main(self):
        """Возвращает кнопку изменения количества/статуса в корзине для первого товара."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.in_cart_main)))

    def get_color_burgundy(self):
        """Возвращает чекбокс фильтра цвета 'Бордовый'."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.color_burgundy)))

    def get_button_up(self):
        """Возвращает кнопку прокрутки страницы вверх."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_up)))

    def get_button_all_products(self):
        """Возвращает вкладку 'Все товары' в каталоге."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_all_products)))

    # Actions

    def click_in_cart_main(self):
        """Добавляет первый товар в корзину и возвращается назад."""
        self.action.move_to_element(self.get_icon_prod()).perform()
        self.get_in_cart_main().click()
        self.cp.click_back()

    def click_in_cart_main_1(self):
        """Добавляет второй товар в корзину и возвращается назад."""
        self.action.move_to_element(self.get_icon_prod_1()).perform()
        self.get_in_cart_main_1().click()
        self.cp.click_back()

    def move_window_dawn_main(self, pixels=1750):
        """
        Прокручивает страницу вниз на указанное количество пикселей.
        :param pixels: Расстояние прокрутки.
        """
        try:
            self.driver.execute_script(f"window.scrollTo(0, {pixels});")
        except Exception as e:
            print(f"Ошибка скролла: {e}")

    def click_color_burgundy(self):
        """Активирует фильтр по цвету 'Бордовый'."""
        self.get_color_burgundy().click()

    def click_button_all_products(self):
        """Переходит во вкладку 'Все товары'."""
        self.action.move_to_element(self.get_button_all_products()).perform()
        self.get_button_all_products().click()

    # Method
    def product_main(self):
        """
        Полный сценарий: фильтрация товаров в каталоге, добавление в корзину и сравнение.
        """

        # 1. Подготовка: Переход в каталог и фильтрация
        with allure.step("Product main"):
            Logger.add_start_step(method='product_main')
            self.driver.get(self.cp.url)
            self.driver.refresh()

            self.move_window_dawn_main()
            self.get_current_url()  # Метод вызывается, но результат никуда не сохраняется. Лишняя строка.

            self.click_button_all_products()

            # Применение фильтров через методы Catalog_page
            self.cp.select_price_min()
            self.cp.select_price_max()
            self.cp.click_checkbox_apple()
            self.click_color_burgundy()

            self.cp.wait_for_all_elements()  # Ожидание загрузки товаров после фильтрации

            self.move_window_dawn_main(500)
            self.cp.click_filter_ram()
            self.cp.click_filter_count()
            self.cp.click_by_default()
            self.cp.click_by_size_sale()

            # 2. Сбор данных о товарах для проверки
            prod1 = self.cp.get_product_card_title()  # Название 1-го товара
            prod = self.cp.get_product_card_title_1()  # Название 2-го товара
            card_price = self.cp.get_card_price()  # Цена 1-го товара
            card_price_1 = self.cp.get_card_price_1()  # Цена 2-го товара

            print(f'Выбранный товар 1 - {prod}, цена - {card_price},\nВыбранный товар 2 - {prod1}, цена - {card_price_1}')

            # 3. Взаимодействие: Добавление в корзину и Избранное
            self.click_in_cart_main()
            self.click_in_cart_main_1()


            self.cp.click_icon_heart()
            time.sleep(self.cp.sleep)
            self.cp.click_compare()

            time.sleep(self.cp.sleep)
            self.cp.click_icon_heart()
            time.sleep(self.cp.sleep)
            self.cp.click_compare()

            self.cp.click_icon_heart_main()

            # 4. Валидация (Проверки)
            # Проверка страницы Избранного
            self.hp.assert_heart_page(card_price_1, card_price, prod, prod1)

            # Проверка страницы Сравнения
            self.cmp.product_compare(prod, prod1, card_price_1, card_price)


            self.get_screenshot()
            Logger.add_end_step(url=self.get_current_url(), method='product_main')





