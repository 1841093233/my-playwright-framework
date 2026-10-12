"""登录页面对象。"""
from playwright.sync_api import Page
from pages.base_page import BasePage
from config import BASE_URL


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("h3[data-test='error']")

    def goto(self):
        self.page.goto(BASE_URL)

    def login(self, username: str, password: str):
        """执行登录操作。"""
        self.goto()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.click(self.login_button)

    def get_error_message(self) -> str:
        """获取错误提示文本。"""
        return self.error_message.text_content()