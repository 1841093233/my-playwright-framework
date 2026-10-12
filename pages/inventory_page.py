"""商品列表页面对象。"""
from playwright.sync_api import Page
from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = page.locator(".title")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.products = page.locator(".inventory_item")
        self.burger_menu = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")

    def is_loaded(self) -> bool:
        """页面是否加载成功。"""
        return self.title.is_visible() and self.title.text_content() == "Products"

    def add_product(self, product_name: str):
        """按商品名加购。"""
        product = self.products.filter(has_text=product_name)
        product.get_by_role("button", name="Add to cart").click()

    def cart_count(self) -> int:
        """购物车角标数量。"""
        if self.cart_badge.is_visible():
            return int(self.cart_badge.inner_text())
        return 0

    def open_cart(self):
        self.click(self.cart_link)

    def logout(self):
        """退出登录。"""
        self.click(self.burger_menu)
        self.click(self.logout_link)