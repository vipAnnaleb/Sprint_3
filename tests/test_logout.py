from conftest import (webdriver_wait,
                      SITE_URL,
                      TEST_LOGIN,
                      TEST_PASSWORD)

from locators import (Login,
                      Profile,
                      Home)


class TestLogout:
    def test_logout(self, driver):
        driver.get(SITE_URL)
        driver.find_element(*Home.ENTRY_BTN).click()
        webdriver_wait(driver, Login.ENTRY_TITLE)
        driver.find_element(*Login.EMAIL_FIELD).send_keys(TEST_LOGIN)
        driver.find_element(*Login.PASSWORD_FIELD).send_keys(TEST_PASSWORD)
        driver.find_element(*Login.SIGN_IN_BTN).click()
        webdriver_wait(driver, Home.CONSTRACTOR_TITLE)
        driver.find_element(*Home.PROFILE_BTN).click()
        webdriver_wait(driver, Profile.SIGN_IN_BTN)
        driver.find_element(*Profile.LOGOUT_BTN).click()
        webdriver_wait(driver, Login.ENTRY_TITLE)
        check = driver.find_element(*Login.ENTRY_TITLE).text
        assert 'Вход' == check

