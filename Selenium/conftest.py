import logging
import pytest
from pytest import fixture
from selenium import webdriver
from typing import Iterable, TypeVar

from Selenium.pages import LoginPage
from Selenium.pages.login import LoginPage
from Selenium.pages.dropdown import DropDownPage
from Selenium.pages.date_picker import DatePicker
from Selenium.pages.file_upload import FileUpload

from Selenium.pages.slider import Slider

T=TypeVar("T")
TARGET_URL: str = "https://www.selenium.dev/selenium/web/web-form.html"

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get(TARGET_URL)
    yield driver
    driver.quit()

@pytest.fixture
def slider(driver) -> Slider:
    return Slider(driver)

@pytest.fixture
def dropdown_page(driver) -> DropDownPage:
    return DropDownPage(driver)

@pytest.fixture
def file_upload(driver) -> FileUpload:
    return FileUpload(driver)

@pytest.fixture
def date_picker(driver) -> DatePicker:
    driver.refresh()
    return DatePicker(driver)

# @pytest.fixture
# def login_page(driver) -> Generator[LoginPage, Any, None]:
#     # driver.refresh()
#     yield LoginPage(driver)
#     driver.close()

@fixture
def login_page()-> Iterable[T]:
    """This fixture returns a WebDriver."""
    logging.debug("Initializing Chrome WebDriver")
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(TARGET_URL)
    login = LoginPage(chrome_driver)
    logging.debug("Starting test execution")
    yield login
    chrome_driver.close()

@fixture(
    params=['Jan', 'Feb', 'Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ids=lambda c: c)
def month(request):
    """, 'Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'"""
    return request.param
