import random
from typing import Generator, Any
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

from pages.slider import Slider
from pages.web_table import WebTable
from pages.login import LoginPage
from pages.dropdown import DropDownPage
from pages.date_picker import DatePicker
from pages.file_upload import FileUpload
from resources.selenium_data import SeleniumData


def pytest_addoption(parser):
    parser.addoption(
        "--on-browser",
        action="store",
        default="chrome",
        help="Browser to run tests against"
    )


@fixture
def browser(request) -> str:
    """Get terminal option for which browser to use."""
    return request.config.getoption("--on-browser")

@fixture
def get_driver(browser) -> Generator[WebDriver | WebDriver, Any, None]:
    """
    This fixture initializes a WebDriver for the specified browser,
     and ensures proper cleanup after the test execution by quitting the driver.
    """
    if browser == "chrome":
        options = Options()
        # Important options for CI
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    yield driver
    driver.quit()

@fixture
def slider(get_driver: WebDriver) -> Slider:
    """Instantiate Slider class."""
    return Slider(get_driver)

@fixture
def drop_down(get_driver: WebDriver) -> DropDownPage:
    """Instantiate DropDownPage class."""
    return DropDownPage(get_driver)

@fixture
def file_upload(get_driver: WebDriver) -> FileUpload:
    """Instantiate FileUpload class."""
    return FileUpload(get_driver)

@fixture
def date_picker(get_driver: WebDriver) -> DatePicker:
    """Instantiate DatePicker class."""
    return DatePicker(get_driver)

@fixture
def web_table(get_driver: WebDriver) -> WebTable:
    """Instantiate WebTable class."""
    return WebTable(get_driver)

@fixture
def login(get_driver: WebDriver) -> LoginPage:
    """Instantiate LoginPage class."""
    return LoginPage(get_driver)

@fixture(params=SeleniumData.calendar_months, ids=lambda c: c)
def months(request) -> str:
    """Fixture returns Calendar months one at a time.'"""
    return request.param

@fixture()
def all_calendar_months() -> str:
    """Fixture returns Calendar months.'"""
    return SeleniumData.calendar_months

@fixture
def random_months(all_calendar_months :str) -> list[str]:
    """Fixture returns 5 Calendar months one at a time.'"""
    random_months = 5
    return random.sample(all_calendar_months, random_months)
