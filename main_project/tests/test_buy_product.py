import time

import pytest
from selenium import webdriver

from main_project.pages.cart_page import Cart_page
from main_project.pages.client_information_page import Client_information_page
from main_project.pages.finish_page import Finish_page
from main_project.pages.login_page import Login_page
from main_project.pages.main_page import Main_page
from main_project.pages.payment_page import Payment_page

# @pytest.mark.run(order=3)
def test_buy_product_1(set_up,set_group):
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)

    print('Start Test 1')


    mp = Main_page(driver)
    mp.select_product()
    # login = Login_page(driver)
    # login.authorization()

    # mp = Main_page(driver)
    # mp.select_product_1()
    #
    # cp = Cart_page(driver)
    # cp.click_button_logout()
    #
    # cip = Client_information_page(driver)
    # cip.input_information()
    #
    # pay = Payment_page(driver)
    # pay.payment()
    #
    # f = Finish_page(driver)
    # f.finish()

    print("Finish Test")
    # time.sleep(3)
    driver.quit()

# @pytest.mark.run(order=1)
# def test_buy_product_2(set_up,set_group):
#     options = webdriver.ChromeOptions()
#     options.add_argument("--incognito")
#     driver = webdriver.Chrome(options=options)
#
#     print('Start Test 2')
#
#
#
#     login = Login_page(driver)
#     login.authorization()
#
#     mp = Main_page(driver)
#     mp.select_product_2()
#
#     cp = Cart_page(driver)
#     cp.click_button_logout()
#
#     print("Finish Test")
#     # time.sleep(3)
#     driver.quit()
#
# # @pytest.mark.run(order=2)
# def test_buy_product_3(set_up,set_group):
#     options = webdriver.ChromeOptions()
#     options.add_argument("--incognito")
#     driver = webdriver.Chrome(options=options)
#
#     print('Start Test 3')
#
#
#
#     login = Login_page(driver)
#     login.authorization()
#
#     mp = Main_page(driver)
#     mp.select_product_3()
#
#     cp = Cart_page(driver)
#     cp.click_button_logout()
#
#     print("Finish Test")
#     # time.sleep(3)
#     driver.quit()


