"""登录功能测试。"""
from playwright.sync_api import expect
from config import INVENTORY_URL, BASE_URL


class TestLogin:

    def test_valid_login(self, login_page, test_users):
        """正常登录：验证跳转到商品列表页。"""
        user = test_users["valid_user"]
        login_page.login(user["username"], user["password"])
        expect(login_page.page).to_have_url(INVENTORY_URL)

    def test_invalid_password(self, login_page, test_users):
        """密码错误：验证显示错误提示。"""
        user = test_users["invalid_user"]
        login_page.login(user["username"], user["password"])
        assert "Username and password do not match" in login_page.get_error_message()

    def test_locked_out_user(self, login_page, test_users):
        """锁定用户：验证显示锁定提示。"""
        user = test_users["locked_out_user"]
        login_page.login(user["username"], user["password"])
        assert "locked out" in login_page.get_error_message().lower()

    def test_logout(self, login_page, inventory_page, test_users):
        """登出：验证登录后能正常退出。"""
        user = test_users["valid_user"]
        login_page.login(user["username"], user["password"])
        expect(login_page.page).to_have_url(INVENTORY_URL)

        inventory_page.logout()
        expect(login_page.page).to_have_url(BASE_URL)