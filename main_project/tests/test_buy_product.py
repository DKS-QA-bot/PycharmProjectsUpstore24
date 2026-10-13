from selenium import webdriver
from main_project.pages.cart_page import Cart_page
from main_project.pages.heart_page import Heart_page
from main_project.pages.compare_page import Compare_page
from main_project.pages.main_page import Main_page

def test_buy_product(set_up,set_group):
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)

    # lp = Login_page(driver)
    # lp.authorization()


    mp = Main_page(driver)
    prod1,prod,price,price_1 = mp.select_product()

    hp = Heart_page(driver)
    hp.assert_heart_page(prod1=prod,prod=prod1,price=price,price_1=price_1)

    cp = Compare_page(driver)
    cp.product_compare(prod1=prod,prod=prod1,price=price,price_1=price_1)


    cp = Cart_page(driver)
    cp.assert_product_cart(prod1=prod,prod=prod1,price=price,price_1=price_1)


    driver.quit()




