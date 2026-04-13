from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """This class represents functions for the Login Page"""
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @staticmethod
    def send_control_keys(element: WebElement, value:str) -> None:
        """Select all pre-existing values."""
        element.send_keys(Keys.CONTROL, value)

    @staticmethod
    def tap_backspace(element: WebElement) -> None:
        """Tap backspace."""
        element.send_keys(Keys.BACKSPACE)

    def wait_until_element_visible(self, widget) -> None:
        """Wait until element is vivible."""
        self.wait.until(EC.visibility_of_element_located(widget))

    def is_element_visible(self,element) -> bool:
        """Return True if element is displayed, else False."""
        return self.wait.until(EC.visibility_of_element_located(element)).is_displayed()