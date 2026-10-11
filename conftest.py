"""Pytest 全局配置和 fixtures。"""
import json
from pathlib import Path
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    return InventoryPage(page)


@pytest.fixture(scope="session")
def test_users():
    """加载测试用户数据。"""
    root = Path(__file__).parent
    with open(root / "data" / "users.json", "r", encoding="utf-8") as f:
        return json.load(f)