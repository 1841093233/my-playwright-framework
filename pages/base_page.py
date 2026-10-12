"""所有页面对象的基类。"""
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self, locator):
        """点击。"""
        locator.click()

    def wait_for_url(self, url: str):
        """等待页面跳转到指定 URL。"""
        self.page.wait_for_url(url)