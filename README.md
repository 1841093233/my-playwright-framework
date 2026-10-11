# My Playwright Framework

基于 Playwright + Pytest 的 UI 自动化测试框架，覆盖 SauceDemo 电商网站的核心业务流程。

## 技术栈

| 技术 | 用途 |
|---|---|
| Python | 开发语言 |
| Playwright | 浏览器自动化 |
| Pytest | 测试框架 |
| GitHub Actions | CI 持续集成 |

## 项目结构

```
.
├── .github/
│   └── workflows/
│       └── playwright.yml      # CI 配置
├── pages/                       # 页面对象（POM）
│   ├── base_page.py             # 基类
│   ├── login_page.py            # 登录页
│   └── inventory_page.py        # 商品列表页
├── tests/                       # 测试用例
│   ├── test_login.py            # 登录测试
│   └── test_cart.py             # 购物车测试
├── data/                        # 测试数据
│   └── users.json
├── config.py                    # 全局配置
├── conftest.py                  # Fixtures
├── pytest.ini                   # Pytest 配置
├── requirements.txt             # 依赖清单
└── README.md
```

## 核心特性

### 1. POM 分层

每个页面封装成一个类，页面元素作为属性，页面操作作为方法。

```python
login_page.login("standard_user", "secret_sauce")
inventory_page.add_product("Sauce Labs Backpack")
inventory_page.logout()
```

**好处**：定位器集中管理，页面改版只改一处。

### 2. Fixture 依赖注入

通过 pytest fixture 自动注入页面对象，测试函数不需要手动实例化。

```python
def test_valid_login(self, login_page, test_users):
    user = test_users["valid_user"]
    login_page.login(user["username"], user["password"])
```

**好处**：按需注入，自动准备和清理。

### 3. 失败自动诊断

配置了 `pytest.ini`：

- `--screenshot=only-on-failure`：失败时自动截图
- `--tracing=retain-on-failure`：失败时保留 Trace
- `--video=retain-on-failure`：失败时保留视频
- `--output=test-results`：产物统一输出到 `test-results/`

**Trace 怎么用**：

```bash
playwright show-trace test-results/xxx/trace.zip
```

能像视频一样回放整个测试过程，看每一步的 DOM 快照、网络请求、控制台日志。

### 4. CI 集成

GitHub Actions 自动执行测试，每次 push 或 PR 触发。

## 如何运行

### 环境要求

- Python 3.10+

### 安装

```bash
# 克隆仓库
git clone https://github.com/1841093233/my-playwright-framework.git
cd my-playwright-framework

# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 安装浏览器
playwright install chromium
```

### 运行测试

```bash
# 跑所有测试
pytest

# 跑指定文件
pytest tests/test_login.py

# 跑指定类
pytest tests/test_login.py::TestLogin

# 跑指定方法
pytest tests/test_login.py::TestLogin::test_valid_login

# 带浏览器界面跑（调试用）
pytest --headed
```

## 测试覆盖

| 模块 | 用例数 | 说明 |
|---|---|---|
| 登录 | 4 | 正常登录、密码错误、锁定用户、登出 |
| 购物车 | 3 | 空购物车、加购一件、加购两件 |
| **合计** | **7** | |

## 作者

- GitHub: [@1841093233](https://github.com/1841093233)