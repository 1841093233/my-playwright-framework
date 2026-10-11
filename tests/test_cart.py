"""购物车功能测试。"""
from playwright.sync_api import expect
from config import INVENTORY_URL


class TestCart:

    def test_cart_badge_hidden_when_empty(self, login_page, inventory_page, test_users):
        """空购物车时，角标不应显示。"""
        user = test_users["valid_user"]
        login_page.login(user["username"], user["password"])
        expect(login_page.page).to_have_url(INVENTORY_URL)

        assert inventory_page.cart_count() == 0

    def test_add_product_increases_cart_count(self, login_page, inventory_page, test_users):
        """加购后，角标数量应为 1。"""
        user = test_users["valid_user"]
        login_page.login(user["username"], user["password"])

        inventory_page.add_product("Sauce Labs Backpack")
        assert inventory_page.cart_count() == 1

    def test_add_two_products(self, login_page, inventory_page, test_users):
        """加购两件商品，角标数量应为 2。"""
        user = test_users["valid_user"]
        login_page.login(user["username"], user["password"])

        inventory_page.add_product("Sauce Labs Backpack")
        inventory_page.add_product("Sauce Labs Bike Light")
        assert inventory_page.cart_count() == 2