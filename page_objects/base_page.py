
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from tests.conftest import driver


class BasePage:
    #Locators
    __url = "https://sampleapp.tricentis.com/101/index.php"
    __header_get_your = (By.XPATH,"//div[@id='site-content']//ul[@class='slides']/li[2]//h2[@class='slide-title']")
    __automobile_button=(By.XPATH, "//div[@class='main-navigation']//a[@id='nav_automobile']")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(self.__url)

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, time: int = 10) -> object:
       # self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def find_get_your_header(self):
        self._driver.find_element(self.__header_get_your)

    def is_get_your_header_displayed(self) -> bool:
        #return self._is_displayed(self.__header_get_your)
        return self._driver.find_element(By.XPATH,"//div[@id='site-content']//ul[@class='slides']/li[2]//h2[@class='slide-title']").is_displayed()

    def _click(self, locator: tuple):
        self._find(locator).click()

    def click_on_automobile_button(self):
        self._click(self.__automobile_button)


    #def field_contains_text(self) ->bool: