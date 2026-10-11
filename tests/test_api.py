"""API 测试：验证 HTTP 请求。"""
import pytest
from playwright.sync_api import expect


@pytest.fixture(scope="module")
def api_request(playwright):
    """创建一个 API 请求上下文。"""
    context = playwright.request.new_context(ignore_https_errors=True)
    yield context
    context.dispose()


class TestAPI:

    def test_get_returns_200(self, api_request):
        """GET 请求：验证状态码和返回结构。"""
        response = api_request.get("https://httpbin.org/get")
        expect(response).to_be_ok()
        body = response.json()
        assert "url" in body

    def test_post_returns_200(self, api_request):
        """POST 请求：验证返回内容。"""
        response = api_request.post(
            "https://httpbin.org/post",
            data={"title": "foo", "body": "bar"},
        )
        expect(response).to_be_ok()
        body = response.json()
        assert body["json"]["title"] == "foo"

    def test_status_code(self, api_request):
        """验证指定状态码。"""
        response = api_request.get("https://httpbin.org/status/200")
        assert response.status == 200