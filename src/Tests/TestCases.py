import unittest
from src.POM.HomePage import HomePage
from src.POM.MoisturizerPage import MoisturizerPage
from src.Tests.BaseTest import BaseTest
import pytest

pytest.mark.usefixtures("setUp")
class TestCases(BaseTest):

    def test_page_load(self):
        page = HomePage(self.driver)
        #page.get_url()
        #self.assertTrue(page.check_page_loaded())

    def test_validate_mainpage(self):
        page = HomePage(self.driver)
        page.select_options_based_on_temperature()

    def test_validate_add_to_cart(self):
        add_to_cart_page = MoisturizerPage(self.driver)
        add_to_cart_page.add_to_cart()


    '''def test_page_load(self):
        print("\n" + str(test_cases(0)))
        page = HomePage(self.driver)
        self.assertTrue(page.check_page_loaded())

    def test_search_item(self):
        print("\n" + str(test_cases(1)))
        page = HomePage(self.driver)
        search_result = page.search_item("iPhone")
        self.assertIn("iPhone", search_result)

    def test_sign_up_button(self):
        print("\n" + str(test_cases(2)))
        page = HomePage(self.driver)
        sign_up_page = page.click_sign_up_button()
        self.assertIn("ap/register", sign_up_page.get_url())

    def test_sign_in_button(self):
        print("\n" + str(test_cases(3)))
        page = HomePage(self.driver)
        login_page = page.click_sign_in_button()
        self.assertIn("ap/signin", login_page.get_url())

    def test_sign_in_with_valid_user(self):
        print("\n" + str(test_cases(4)))
        main_page = HomePage(self.driver)
        login_page = main_page.click_sign_in_button()
        result = login_page.login_with_valid_user("valid_user")
        self.assertIn("yourstore/home", result.get_url())

    def test_sign_in_with_in_valid_user(self):
        print("\n" + str(test_cases(5)))
        main_page = HomePage(self.driver)
        login_page = main_page.click_sign_in_button()
        result = login_page.login_with_in_valid_user("invalid_user")
        self.assertIn("There was a problem with your request", result)'''