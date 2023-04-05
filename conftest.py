import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


from locators import (Home,
                      Login)

SITE_URL = "https://stellarburgers.nomoreparties.site/"

NAME = "Test User"
USER_NAME = "testtestov"
DOMAIN = "@mail.ru"

TEST_LOGIN = "example@mail.ru"
TEST_PASSWORD = "1234567"
INCORRECT_PASSWORD = "777"

WAIT_TIME = 10


def webdriver_wait(driver_use, locator):  # Время ожидания веб-драйвера
    WebDriverWait(driver_use, WAIT_TIME).until(expected_conditions.visibility_of_element_located(locator))


@pytest.fixture()
def driver():  # Запуск и оставновка веб-драйвера
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(SITE_URL)
    yield driver
    driver.quit()






