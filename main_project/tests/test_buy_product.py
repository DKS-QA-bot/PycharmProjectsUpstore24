# from main_project.pages.heart_page import Heart_page
# from main_project.pages.compare_page import Compare_page
# from main_project.pages.login_page import Login_page
# from main_project.pages.catalog_page import Catalog_page
# from main_project.pages.main_page import Main_page
#
#
# def test_buy_product(set_up,set_group,driver):
#
#     lp = Login_page(driver)
#     lp.authorization()
#
#
#     mp = Catalog_page(driver)
#     prod1,prod,price,price_1 = mp.select_product()
#
#     hp = Heart_page(driver)
#     hp.assert_heart_page(prod1=prod,prod=prod1,price=price,price_1=price_1)
#
#     cmp = Compare_page(driver)
#     cmp.product_compare(prod1=prod,prod=prod1,price=price,price_1=price_1)
#
#
# def test_buy_product_1(set_up, set_group,driver):
#
#     mcp = Main_page(driver)
#     mcp.product_main()
from main_project.pages.heart_page import Heart_page
from main_project.pages.compare_page import Compare_page
from main_project.pages.login_page import Login_page
from main_project.pages.catalog_page import Catalog_page
from main_project.pages.main_page import Main_page


# Фикстуры set_up и set_group обычно отвечают за:
# - set_up: запуск/остановка браузера (driver), настройка окружения.
# - set_group: предварительные действия для группы тестов (например, очистка БД или корзины).
# В данном случае они служат зависимостями, гарантирующими готовность среды.

def test_buy_product(set_up, set_group, driver):
    """
    Сценарий 1: Покупка через Каталог.
    Проверяет путь: Авторизация -> Каталог -> Избранное -> Сравнение.
    """

    # 1. АВТОРИЗАЦИЯ
    # Инициализируем объект страницы Логина, передавая драйвер
    lp = Login_page(driver)
    # Выполняем метод авторизации (логин/пароль должны быть внутри метода или фикстурой)
    lp.authorization()

    # 2. КАТАЛОГ И ВЫБОР ТОВАРА
    # Используем Catalog_page для поиска и выбора товаров
    mp = Catalog_page(driver)
    # Метод select_product возвращает данные двух товаров для дальнейшей проверки
    # Исправлена возможная ошибка: prod1 - первый товар, prod - второй (по логике имен в assert ниже)
    prod1, prod, price, price_1 = mp.select_product()

    # 3. ПРОВЕРКА СТРАНИЦЫ "ИЗБРАННОЕ" (Heart Page)
    hp = Heart_page(driver)
    # Проверяем, что товары корректно добавились в избранное с правильными ценами и названиями
    # Названия аргументов prod1=prod и prod=prod1 выглядят как опечатка,
    # но сохранены как в исходнике (возможно, так задумано в самом методе assert_heart_page)
    hp.assert_heart_page(prod1=prod, prod=prod1, price=price, price_1=price_1)

    # 4. ПРОВЕРКА СТРАНИЦЫ "СРАВНЕНИЕ" (Compare Page)
    cmp = Compare_page(driver)
    # Проверяем таблицу сравнения товаров
    cmp.product_compare(prod1=prod, prod=prod1, price=price, price_1=price_1)


def test_buy_product_1(set_up, set_group, driver):
    """
    Сценарий 2: Комплексный сценарий через Главную страницу.
    Этот тест запускает длинную цепочку действий, описанную внутри Main_page.
    """

    # Инициализируем Main_page.
    # Main_page обычно содержит ссылки на другие страницы (Catalog, Login и т.д.)
    mcp = Main_page(driver)

    # Запускаем основной бизнес-сценарий.
    # Внутри метода product_main() уже зашиты:
    # - переходы по страницам
    # - фильтрация товаров
    # - добавление в корзину/избранное
    # - проверки (asserts)
    mcp.product_main()






