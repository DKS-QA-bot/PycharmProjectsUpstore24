import time
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from main_project.base.base_class import Base


class Catalog_page(Base):
    """Класс, содержащий локаторы и методы для главной страницы интернет-магазина."""

    def __init__(self,driver):
        self.driver = driver
        """Инициализация главной страницы."""
        super().__init__(self.driver)
        self.wait = WebDriverWait(self.driver, 30)
        self.actions = ActionChains(self.driver)
        self.sleep = 1.5

    # URL
    url = 'https://upstore24.ru/'

    #Locators
    hamburger = '//*[@class="hamburger__title"]'
    select_pc = '(//*[@data-nav-item="18771934"])[2]'
    cart = '//*[@data-test="shopping-cart-link"]'
    burger = '//button[@id="react-burger-menu-btn"]'
    button_about = '//a[@id="about_sidebar_link"]'
    toolbar_compare = '//*[@data-toolbar-item="compare"]'
    toolbar_in_cart = '//*[@data-toolbar-item="cart"]'
    price_min = '(//*[@class="noUi-touch-area"])[1]'
    price_max = '(//*[@class="noUi-touch-area"])[2]'
    checkbox_apple = '//*[@for="filter-item-109849115"]'
    checkbox_silver = '//*[@for="filter-item-109849120"]'
    filter_count = '//*[@data-filter-submit]'
    filter_ram = '//*[@for="filter-item-109849130"]'
    platform = '//*[@for="filter-item-109849269"]'
    processor = '//*[@for="filter-item-247481722"]'
    graphics = '//*[@for="filter-item-247481724"]'
    display_type = '//*[@for="filter-item-100526820"]'
    size_display = '//*[@data-filter-item="27132777"]'
    diagonal = '//*[@for="filter-item-114473190"]'
    by_default = '//*[@class="input js-order"]'
    by_size_sale = '//*[normalize-space()="По размеру скидки"]'
    icon = '(//*[@class="lazy entered loaded"])[6]'
    fast_see_1 = '(//*[normalize-space()="Быстрый просмотр"])[1]'
    compare = '(//*[@data-icon="compare"])[3]'
    in_cart = '(//*[@class="add-cart-counter"])[3]'
    in_cart_1 = '(//*[@class="add-cart-counter"])[2]'
    back = '//*[normalize-space()="Продолжить покупки"]'
    short_list = '//*[@class="collection__short-filters collection__short-filters-sidebar js-collection-short-filters"]'
    arrow_to_right = '(//*[@data-quickview-swipe="466495801"])[2]'
    spinner = '//*[@class="collection__loader-spinner"]'
    popup_louder = '//*[@class="cart-popup__loader"]'
    fancybox_close = '(//*[@data-fancybox-close])[2]'
    product_card_title = '(//*[@class="product-card__title"])[1]'
    product_card_title_1 = '(//*[@class="product-card__title"])[2]'
    card_price = '(//*[@data-product-card-price-from-cart])[1]'
    card_price_1 = '(//*[@data-product-card-price-from-cart])[2]'
    heart_icon = '(//*[@data-icon="heart"])[3]'
    heart_icon_main = '(//*[@data-icon="heart"])[1]'

    # Getters
    def get_toolbar_in_cart(self):
        """Возвращает кликабельный элемент иконки корзины в шапке сайта."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.toolbar_in_cart)))

    def get_heart_icon_main(self):
        """Возвращает кликабельный элемент иконки избранного в шапке сайта."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.heart_icon_main)))

    def get_heart_icon(self):
        """Возвращает кликабельный элемент иконки избранного на карточке товара."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.heart_icon)))

    def get_card_price_1(self):
        """Возвращает текст цены второго товара в каталоге."""
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.card_price_1))).text

    def get_card_price(self):
        """Возвращает текст цены первого товара в каталоге."""
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.card_price))).text

    def get_product_card_title_1(self):
        """Возвращает название второго товара в каталоге."""
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.product_card_title_1))).text

    def get_product_card_title(self):
        """Возвращает название первого товара в каталоге."""
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.product_card_title))).text

    def get_toolbar_compare(self):
        """Возвращает кликабельный элемент кнопки сравнения в шапке сайта."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.toolbar_compare)))

    def get_fancybox_close(self):
        """Возвращает кликабельный элемент кнопки закрытия модального окна."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.fancybox_close)))

    def get_in_cart_1(self):
        """Возвращает кликабельный элемент счетчика добавления второго товара в корзину."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.in_cart_1)))

    def get_popup_louder(self):
        """Ожидает исчезновения лоадера в попапе корзины."""
        return self.wait.until(EC.invisibility_of_element_located((By.XPATH, self.popup_louder)))

    def get_spinner(self):
        """Ожидает исчезновения лоадера загрузки товаров."""
        return self.wait.until(EC.invisibility_of_element_located((By.XPATH, self.spinner)))

    def get_arrow_to_right(self):
        """Возвращает кликабельный элемент стрелки листания карусели вправо."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.arrow_to_right)))

    def get_short_list(self):
        """Возвращает элемент блока с активными фильтрами."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.short_list)))

    def get_back(self):
        """Возвращает кликабельный элемент кнопки 'Продолжить покупки'."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.back)))

    def get_in_cart(self):
        """Возвращает кликабельный элемент счетчика добавления первого товара в корзину."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.in_cart)))

    def get_compare(self):
        """Возвращает кликабельный элемент кнопки сравнения на карточке товара."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.compare)))

    def get_icon(self):
        """Возвращает кликабельный элемент иконки товара для наведения мыши."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.icon)))

    def get_fast_see_1(self):
        """Возвращает кликабельный элемент кнопки 'Быстрый просмотр'."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.fast_see_1)))

    def get_by_size_sale(self):
        """Возвращает кликабельный элемент сортировки 'По размеру скидки'."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.by_size_sale)))

    def get_by_default(self):
        """Возвращает кликабельный элемент сортировки по умолчанию."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.by_default)))

    def get_diagonal(self):
        """Возвращает кликабельный элемент фильтра по диагонали."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.diagonal)))

    def get_size_display(self):
        """Возвращает кликабельный элемент фильтра по размеру/типу дисплея."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.size_display)))

    def get_display_type(self):
        """Возвращает кликабельный элемент фильтра по типу дисплея."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.display_type)))

    def get_graphics(self):
        """Возвращает кликабельный элемент фильтра по видеокарте."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.graphics)))

    def get_processor(self):
        """Возвращает кликабельный элемент фильтра по процессору."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.processor)))

    def get_platform(self):
        """Возвращает кликабельный элемент фильтра по платформе"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.platform)))

    def get_filter_ram(self):
        """Возвращает кликабельный элемент фильтра по оперативной памяти."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_ram)))

    def get_filter_count(self):
        """Возвращает кликабельный элемент кнопки применения фильтров."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_count)))

    def get_checkbox_silver(self):
        """Возвращает кликабельный элемент чекбокса цвета 'Серебристый'."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.checkbox_silver)))

    def get_checkbox_apple(self):
        """Возвращает кликабельный элемент чекбокса бренда 'Apple'."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.checkbox_apple)))

    def get_price_max(self):
        """Возвращает ползунок максимальной цены"""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.price_max)))

    def get_price_min(self):
        """Возвращает ползунок минимальной цены."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.price_min)))

    def get_select_hamburger(self):
        """Возвращает кликабельный элемент кнопки мобильного меню."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.hamburger)))

    def get_select_pc(self):
        """Возвращает кликабельный элемент категории 'Компьютеры' в меню."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.select_pc)))

    def get_cart(self):
        """Возвращает кликабельный элемент иконки корзины."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_burger(self):
        """Возвращает кликабельный элемент кнопки бургер-меню."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.burger)))

    def get_button_about(self):
        """Возвращает кликабельный элемент кнопки 'О нас'."""
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_about)))

    # Actions
    def click_toolbar_in_cart(self):
        """Кликает по иконке корзины в шапке сайта."""
        try:
            self.get_toolbar_in_cart().click()
            print("Click toolbar in cart")
        except Exception:
            time.sleep(0.5)
            self.get_toolbar_in_cart().click()
            print("Click toolbar in cart")

    def click_icon_heart_main(self):
        """
        Кликает по иконке избранного в шапке сайта.
        """
        try:
            self.get_heart_icon_main().click()
            print("Click heart icon main")
        except Exception:
            time.sleep(0.5)
            self.get_heart_icon_main().click()
            print("Click heart icon main")

    def click_icon_heart(self):
        """
        Кликает по иконке избранного на карточке товара.
        """
        try:
            self.get_heart_icon().click()
            print("Click heart icon")
        except Exception:
            time.sleep(0.5)
            self.get_heart_icon().click()
            print("Click heart icon")

    def click_toolbar_compare(self):
        """
        Кликает по кнопке сравнения в шапке сайта.
        """
        try:
            self.get_toolbar_compare().click()
            print("Click toolbar compare")
        except Exception:
            time.sleep(0.5)
            self.get_toolbar_compare().click()
            print("Click toolbar compare")

    def click_fancybox_close(self):
        """
        Закрывает модальное окно и ожидает исчезновения лоадера.
        """
        try:
            self.get_fancybox_close().click()
            self.get_popup_louder()
            print("Click close")
        except Exception:
            time.sleep(0.5)
            self.get_fancybox_close().click()
            self.get_popup_louder()
            print("Click close")

    def click_in_cart_1(self):
        """
        Добавляет второй товар в корзину и ожидает лоадер.
        """
        try:
            self.get_in_cart_1().click()
            self.get_popup_louder()
            print("Click in cart")
        except Exception:
            self.get_in_cart_1().click()
            self.get_popup_louder()
            print("Click in cart")

    def wait_popup(self):
        """
        Ожидает исчезновения лоадера попапа. При таймауте делает повторную попытку.
        """
        try:
            self.get_popup_louder()
        except TimeoutException:
            time.sleep(0.5)
            self.get_popup_louder()
            raise Exception("Попап не исчез!")

    def wait_for_all_elements(self):
        """
        Ожидает полной загрузки списка товаров после применения фильтров.
        """
        try:
            self.get_spinner()
            print(f"Загрузились товары по фильтрам : \n{self.get_short_list().text}.\n{self.get_filter_count().text}\n")
        except TimeoutException:
            raise Exception("Не все товары успели загрузиться!")

    def click_arrow_to_right(self):
        """
        Листает карусель товаров вправо.
        """
        try:
            self.get_arrow_to_right().click()
            self.get_popup_louder()
            print("Click arrow to right")
        except Exception:
            time.sleep(0.5)
            self.get_arrow_to_right().click()
            self.get_popup_louder()
            print("Click arrow to right")

    def print_short_list(self):
        """
        Выводит в консоль текст активных фильтров.
        """
        print(self.get_short_list().text)

    def click_back(self):
        """
        Нажимает 'Продолжить покупки' в попапе корзины.
        """
        try:
            self.get_back().click()
            self.get_popup_louder()
            print("Click back")
        except Exception:
            time.sleep(0.5)
            self.get_back().click()
            self.get_popup_louder()
            print("Click back")

    def click_in_cart(self):
        """
        Добавляет первый товар в корзину.
        """
        try:
            self.get_in_cart().click()
            self.get_popup_louder()
            print("Click in cart")
        except Exception:
            self.get_in_cart().click()
            self.get_popup_louder()
            print("Click in cart")

    def click_compare(self):
        """
        Кликает по кнопке сравнения на карточке товара.
        """
        self.get_compare().click()
        print("Click compare")

    def click_fast_see_1(self):
        """
        Открывает быстрый просмотр первого товара.
        """
        try:
            self.actions.move_to_element(self.get_icon()).perform()
            self.get_fast_see_1().click()
            print("Click fast see")
        except Exception:
            self.get_fast_see_1().click()
            print("Click fast see")

    def click_by_size_sale(self):
        """
        Применяет сортировку по размеру скидки.
        """
        try:
            self.get_by_size_sale().click()
            self.wait_for_all_elements()
            print("Click by size sale")
        except Exception:
            self.get_by_size_sale().click()
            self.wait_for_all_elements()
            print("Click by size sale")

    def click_by_default(self):
        """
        Применяет сортировку по умолчанию.
        """
        try:
            self.get_by_default().click()
            self.wait_for_all_elements()
            print("Click by default")
        except Exception:
            self.get_by_default().click()
            self.wait_for_all_elements()
            print("Click by default")

    def click_diagonal(self):
        """
        Фильтрует товары по диагонали экрана.
        """
        try:
            self.get_diagonal().click()
            self.wait_for_all_elements()
            print("Click filter diagonal")
        except Exception:
            self.get_diagonal().click()
            self.wait_for_all_elements()
            print("Click filter diagonal")

    def click_size_display(self):
        """
        Фильтрует товары по типу/размеру дисплея.
        """
        try:
            self.get_size_display().click()
            self.wait_for_all_elements()
            print("Click filter size display")
        except Exception:
            self.get_size_display().click()
            self.wait_for_all_elements()
            print("Click filter size display")

    def click_display_type(self):
        """
        Фильтрует товары по типу дисплея.
        """
        try:
            self.get_display_type().click()
            self.wait_for_all_elements()
            print("Click filter display type")
        except Exception:
            self.get_display_type().click()
            self.wait_for_all_elements()
            print("Click filter display type")

    def click_graphics(self):
        """
        Фильтрует товары по видеокарте.
        """
        try:
            self.get_graphics().click()
            self.wait_for_all_elements()
            print("Click filter graphics")
        except Exception:
            self.get_graphics().click()
            self.wait_for_all_elements()
            print("Click filter graphics")

    def click_processor(self):
        """
        Фильтрует товары по процессору.
        """
        try:
            self.get_processor().click()
            self.wait_for_all_elements()
            print("Click filter processor")
        except Exception:
            self.get_processor().click()
            self.wait_for_all_elements()
            print("Click filter processor")

    def click_platform(self):
        """
        Фильтрует товары по платформе (ОС).
        """
        try:
            self.get_platform().click()
            self.wait_for_all_elements()
            print("Click filter platform")
        except Exception:
            self.get_platform().click()
            self.wait_for_all_elements()
            print("Click filter platform")

    def move_to_window_dawn(self):
        """
        Прокручивает страницу вниз.
        """
        try:
            self.driver.execute_script("window.scrollTo(0,1000)")
            print('move')
        except Exception:
            self.driver.execute_script("window.scrollTo(0,1000)")
            print('move')

    def click_filter_ram(self):
        """
        Фильтрует товары по объему оперативной памяти.
        """
        try:
            self.get_filter_ram().click()
            self.wait_for_all_elements()
            print("Click filter ram")
        except Exception:
            self.get_filter_ram().click()
            self.wait_for_all_elements()
            print("Click filter ram")

    def click_filter_count(self):
        """
        Применяет выбранные фильтры.
        """
        try:
            self.get_filter_count().click()
            self.wait_for_all_elements()
            print("Click filter count")
        except Exception:
            self.get_filter_count().click()
            self.wait_for_all_elements()
            print("Click filter count")

    def click_to_checkbox_silver(self):
        """
        Фильтрует товары по цвету 'Серебристый'.
        """
        try:
            self.get_checkbox_silver().click()
            self.wait_for_all_elements()
            print("Click filter silver")
        except Exception:
            self.get_checkbox_silver().click()
            self.wait_for_all_elements()
            print("Click filter silver")

    def click_select_hamburger(self):
        """
        Открывает мобильное меню.
        """
        try:
            self.get_select_hamburger().click()
            print("Click hamburger")
        except Exception:
            self.get_select_hamburger().click()
            print("Click hamburger")

    def click_select_pc(self):
        """
        Переходит в категорию 'Компьютеры'.
        """
        try:
            self.get_select_pc().click()
            print("Click select product")
        except Exception:
            self.get_select_pc().click()
            print("Click select product")

    def select_price_min(self):
        """
        Сдвигает ползунок минимальной цены вправо.
        """
        self.actions.click_and_hold(self.get_price_min()).move_by_offset(50, 0).release().perform()
        self.wait_for_all_elements()
        print("Click select price min")

    def select_price_max(self):
        """
        Сдвигает ползунок максимальной цены влево.
        """
        self.actions.click_and_hold(self.get_price_max()).move_by_offset(-50, 0).release().perform()
        self.wait_for_all_elements()
        print("Click select price max")

    def click_checkbox_apple(self):
        """
        Фильтрует товары по бренду 'Apple'.
        """
        try:
            self.get_checkbox_apple().click()
            self.wait_for_all_elements()
            print("Click checkbox apple")
        except Exception:
            self.get_checkbox_apple().click()
            self.wait_for_all_elements()
            print("Click checkbox apple")

    # Method
    def select_product(self):
        """
        Полный сценарий: навигация, фильтрация, проверка товаров,
        добавление в избранное/сравнение/корзину.

        :return: tuple (название_товара_1, название_товара_2, цена_товара_1, цена_товара_2)
        """
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()

        self.click_select_hamburger()
        self.click_select_pc()

        self.select_price_min()
        self.select_price_max()

        self.click_checkbox_apple()
        self.click_to_checkbox_silver()
        self.click_filter_count()
        self.click_filter_ram()

        self.move_to_window_dawn()

        self.click_platform()
        self.click_processor()
        self.click_graphics()

        self.move_to_window_dawn()

        self.click_display_type()
        self.click_size_display()
        self.click_diagonal()
        self.click_filter_count()

        self.click_by_default()
        self.click_by_size_sale()


        bc = Base(self.driver)
        bc.get_screenshot()
        # Получение данных первого (индекс 1) и второго (индекс 2) товаров и их цен
        prod1 = self.get_product_card_title()
        prod = self.get_product_card_title_1()
        card_price = self.get_card_price()
        card_price_1 = self.get_card_price_1()


        self.click_icon_heart()
        time.sleep(self.sleep)
        self.click_compare()
        time.sleep(self.sleep)
        self.click_icon_heart()
        time.sleep(self.sleep)
        self.click_compare()

        self.click_fast_see_1()
        self.click_in_cart()
        self.click_back()

        self.click_arrow_to_right()
        self.click_in_cart_1()
        self.click_back()

        self.click_fancybox_close()
        self.click_icon_heart_main()

        return prod1, prod, card_price, card_price_1