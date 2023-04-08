from conftest import (webdriver_wait,
                      SITE_URL,
                      TEST_LOGIN,
                      TEST_PASSWORD)
from locators import (Home,
                      Profile,
                      Login)

#  У меня все тесты не могут пройти дальше логина и регистрации. Не понимаю почему.
#  Высылаю задание, чтобы получить хоть какую-то помощь и объяснение, почему там падает.


class TestNavigateToProfile:
    def test_navigate_to_profile(self, driver):
        driver.get(SITE_URL)
        driver.find_element(*Home.ENTRY_BTN).click()
        webdriver_wait(driver, Login.ENTRY_TITLE)
        driver.find_element(*Login.EMAIL_FIELD).send_keys(TEST_LOGIN)
        driver.find_element(*Login.PASSWORD_FIELD).send_keys(TEST_PASSWORD)
        driver.find_element(*Login.SIGN_IN_BTN).click()
        webdriver_wait(driver, Home.PROFILE_BTN)
        driver.find_element(*Home.PROFILE_BTN).click()
        webdriver_wait(driver, Profile.SIGN_IN_BTN)
        driver.find_element(*Profile.CONSTRUCTOR_BTN).click()
        webdriver_wait(driver, Home.CONSTRACTOR_TITLE)
        check = driver.find_element(*Home.CONSTRACTOR_TITLE).text
        assert check == 'Соберите бургер'